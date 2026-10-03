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
