def test_list_products(client):
    """Test retrieving list of products."""
    response = client.get("/api/v1/products")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert len(body["data"]) >= 3
    assert body["meta"]["total"] >= 3


def test_search_products_by_query(client):
    """Test searching products by name or code."""
    response = client.get("/api/v1/products?query=Paracetamol")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert len(body["data"]) == 1
    assert body["data"][0]["name"] == "Paracetamol 500mg"


def test_filter_products_by_category(client):
    """Test filtering products by category."""
    response = client.get("/api/v1/products?category=Cosmetic")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert len(body["data"]) == 1
    assert body["data"][0]["category"] == "Cosmetic"


def test_get_product_by_id_success(client):
    """Test retrieving product by valid ID."""
    p_id = "11111111-1111-1111-1111-111111111111"
    response = client.get(f"/api/v1/products/{p_id}")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["name"] == "Paracetamol 500mg"
    # Total stock from sample batches (8 + 25 = 33)
    assert body["data"]["total_stock"] == 33


def test_get_product_by_id_not_found(client):
    """Test 404 for non-existent product ID."""
    p_id = "00000000-0000-0000-0000-000000000000"
    response = client.get(f"/api/v1/products/{p_id}")
    assert response.status_code == 404
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "PRODUCT_NOT_FOUND"


def test_create_product_success(client):
    """Test creating a new valid product."""
    payload = {
        "code": "MED-IBU-400",
        "name": "Ibuprofen 400mg",
        "category": "Medicine",
        "unit": "Strip",
        "mrp": "85.00",
        "default_purchase_price": "60.00",
        "barcode": "8901234567899",
        "reorder_level": 20,
    }
    response = client.post("/api/v1/products", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["success"] is True
    assert body["data"]["code"] == "MED-IBU-400"
    assert body["data"]["total_stock"] == 0


def test_create_product_duplicate_code(client):
    """Test rejecting duplicate product SKU code."""
    payload = {
        "code": "MED-PAR-500",  # Already exists in sample data
        "name": "Another Paracetamol",
        "category": "Medicine",
        "unit": "Strip",
        "mrp": "60.00",
    }
    response = client.post("/api/v1/products", json=payload)
    assert response.status_code == 400
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "DUPLICATE_CODE"


def test_create_product_validation_error(client):
    """Test validation error for negative price or invalid category."""
    payload = {
        "code": "MED-ERR-001",
        "name": "Bad Medicine",
        "category": "InvalidCategory",
        "unit": "Strip",
        "mrp": "-10.00",  # Negative MRP violates ge=0
    }
    response = client.post("/api/v1/products", json=payload)
    assert response.status_code == 422
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "VALIDATION_ERROR"


def test_update_product(client):
    """Test updating product fields."""
    p_id = "11111111-1111-1111-1111-111111111111"
    response = client.put(
        f"/api/v1/products/{p_id}",
        json={"name": "Paracetamol 500mg Extra", "reorder_level": 25},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["name"] == "Paracetamol 500mg Extra"
    assert body["data"]["reorder_level"] == 25
