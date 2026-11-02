def test_list_batches(client):
    """Test retrieving list of batches."""
    response = client.get("/api/v1/inventory/batches")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert len(body["data"]) >= 4
    assert body["meta"]["total"] >= 4


def test_fefo_batch_ordering(client):
    """Test First Expiry, First Out (FEFO) batch ordering."""
    p_id = "11111111-1111-1111-1111-111111111111"
    response = client.get(f"/api/v1/inventory/fefo/{p_id}")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["product_name"] == "Paracetamol 500mg"

    batches = body["data"]["fefo_batches"]
    assert len(batches) == 2
    # First batch expires in 2026-11-30, second in 2027-05-15
    assert batches[0]["batch_number"] == "BCH-2026-01"
    assert batches[1]["batch_number"] == "BCH-2026-02"
    assert batches[0]["expiry_date"] < batches[1]["expiry_date"]


def test_low_stock_alerts(client):
    """Test fetching low stock alerts where stock <= reorder_level."""
    response = client.get("/api/v1/inventory/alerts/low-stock")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    # Amoxicillin (stock 5 <= reorder 10) and Face Wash (stock 3 <= reorder 5)
    alert_names = [a["product_name"] for a in body["data"]]
    assert "Amoxicillin 250mg" in alert_names
    assert "Face Wash 100ml" in alert_names


def test_expiry_risk_alerts(client):
    """Test fetching expiry risk alerts within threshold."""
    response = client.get("/api/v1/inventory/alerts/expiry-risk?days=60")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    # Batch BCH-2026-01 expires soon (2026-11-30)
    assert len(body["data"]) >= 1
    assert body["data"][0]["batch_number"] == "BCH-2026-01"


def test_stock_adjustment_success(client):
    """Test recording a physical stock adjustment."""
    payload = {
        "product_id": "11111111-1111-1111-1111-111111111111",
        "batch_id": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbb01",
        "new_quantity": 12,  # Previous was 8
        "reason": "PHYSICAL_COUNT",
        "notes": "Verified count during weekly inventory check",
    }
    response = client.post("/api/v1/inventory/adjustments", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["success"] is True
    assert body["data"]["previous_quantity"] == 8
    assert body["data"]["new_quantity"] == 12
    assert body["data"]["adjustment_quantity"] == 4

    # Verify batch quantity was updated
    fefo_res = client.get("/api/v1/inventory/fefo/11111111-1111-1111-1111-111111111111")
    updated_batch = [b for b in fefo_res.json()["data"]["fefo_batches"] if b["batch_number"] == "BCH-2026-01"][0]
    assert updated_batch["available_quantity"] == 12


def test_stock_adjustment_invalid_batch_product(client):
    """Test rejecting adjustment when batch does not belong to product."""
    payload = {
        "product_id": "11111111-1111-1111-1111-111111111111",
        "batch_id": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbb03",  # Belongs to p2, not p1
        "new_quantity": 10,
        "reason": "CORRECTION",
    }
    response = client.post("/api/v1/inventory/adjustments", json=payload)
    assert response.status_code == 400
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "INVALID_BATCH_PRODUCT"


def test_list_batches_low_stock_evaluates_product_total_stock(client):
    """Test that low_stock filter on batches evaluates total product stock rather than individual batch quantities.
    
    A product with total stock > reorder_level (e.g., Paracetamol with 33 total units > 15 reorder level,
    where batch BCH-2026-01 has 8 units) must NOT be returned as low stock.
    An actual low stock product (Amoxicillin with 5 units <= 10 reorder level) must be returned.
    """
    response = client.get("/api/v1/inventory/batches?low_stock=true")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True

    returned_batch_numbers = [b["batch_number"] for b in body["data"]]
    returned_product_names = [b["product_name"] for b in body["data"]]

    # Paracetamol has 33 total stock across batches > 15 reorder level: must NOT be flagged
    assert "BCH-2026-01" not in returned_batch_numbers
    assert "BCH-2026-02" not in returned_batch_numbers
    assert "Paracetamol 500mg" not in returned_product_names

    # Amoxicillin has 5 total stock <= 10 reorder level: MUST be flagged
    assert "Amoxicillin 250mg" in returned_product_names


def test_expired_batches_excluded_from_usable_stock_and_trigger_low_stock(db_session):
    """Safety Test - Medicine A scenario:
    Product has reorder_level = 15.
    Batch A: 20 units, EXPIRED.
    Batch B: 5 units, VALID.
    
    Expected Safety Behavior:
    - Available dispensing stock must be 5 (NOT 25).
    - Product MUST be flagged in low-stock alerts because 5 <= 15.
    - Expired batch must NEVER be returned by FEFO dispensing recommendation.
    - Expired batch MUST appear in expiry risk alerts as EXPIRED.
    - AI tool get_product_stock_and_batches must report total_stock = 5 and expired_stock = 20.
    """
    import uuid
    from datetime import date, timedelta
    from app.models.product import Product
    from app.models.inventory import Batch
    from app.services import product_service, inventory_service
    from app.services.ai import tools as ai_tools

    today = date.today()
    p_id = uuid.uuid4()
    med_a = Product(
        id=p_id,
        code="MED-SAFETY-01",
        name="Medicine Safety A",
        category="Antibiotics",
        unit="Strip",
        mrp=100.0,
        reorder_level=15,
        is_active=True,
    )
    db_session.add(med_a)

    # Batch A: 20 units, expired 5 days ago
    batch_expired = Batch(
        id=uuid.uuid4(),
        product_id=p_id,
        batch_number="BCH-MEDA-EXP",
        expiry_date=today - timedelta(days=5),
        purchase_cost=50.0,
        quantity=20,
        is_active=True,
    )
    # Batch B: 5 units, valid (expires in 90 days)
    batch_valid = Batch(
        id=uuid.uuid4(),
        product_id=p_id,
        batch_number="BCH-MEDA-VAL",
        expiry_date=today + timedelta(days=90),
        purchase_cost=50.0,
        quantity=5,
        is_active=True,
    )
    db_session.add_all([batch_expired, batch_valid])
    db_session.flush()

    # 1. Product details: total_stock must be 5 (only usable stock)
    prod_data = product_service.get_product_by_id(db_session, p_id)
    assert prod_data["total_stock"] == 5

    # 2. FEFO dispensing: ONLY valid batch BCH-MEDA-VAL must be returned; BCH-MEDA-EXP must be omitted!
    fefo_data = inventory_service.get_fefo_batches(db_session, p_id)
    assert fefo_data["total_stock"] == 5
    fefo_batches = fefo_data["fefo_batches"]
    assert len(fefo_batches) == 1
    assert fefo_batches[0]["batch_number"] == "BCH-MEDA-VAL"

    # 3. Low stock alerts: Product MUST appear because usable stock 5 <= reorder_level 15
    low_alerts = inventory_service.get_low_stock_alerts(db_session)
    low_items = [a for a in low_alerts if a["product_name"] == "Medicine Safety A"]
    assert len(low_items) == 1
    assert low_items[0]["current_stock"] == 5
    assert low_items[0]["reorder_level"] == 15
    assert low_items[0]["shortfall"] == 10

    # 4. Expiry risk alerts: BCH-MEDA-EXP must appear with urgency EXPIRED
    exp_alerts = inventory_service.get_expiry_risk_alerts(db_session, days_threshold=60)
    exp_batches = [b for b in exp_alerts if b["batch_number"] == "BCH-MEDA-EXP"]
    assert len(exp_batches) == 1
    assert exp_batches[0]["urgency"] == "EXPIRED"
    assert exp_batches[0]["days_until_expiry"] < 0

    # 5. AI Tool get_product_stock_and_batches: total_stock must be 5, expired_stock 20
    ai_stock = ai_tools.get_product_stock_and_batches(db_session, product_name="Medicine Safety A")
    assert ai_stock["found"] is True
    assert ai_stock["total_stock"] == 5
    assert ai_stock["expired_stock"] == 20
    assert len(ai_stock["batches"]) == 1
    assert ai_stock["batches"][0]["batch_number"] == "BCH-MEDA-VAL"
    assert len(ai_stock["expired_batches"]) == 1
    assert ai_stock["expired_batches"][0]["batch_number"] == "BCH-MEDA-EXP"


