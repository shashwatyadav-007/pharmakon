def test_list_suppliers(client):
    """Test retrieving list of registered suppliers."""
    response = client.get("/api/v1/suppliers")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert len(body["data"]) >= 1
    assert body["data"][0]["name"] == "Nepal Pharma Distributors"


def test_create_supplier_success(client):
    """Test creating a new supplier record."""
    payload = {
        "name": "Himalayan Med Supplies",
        "contact_person": "Sita Thapa",
        "phone": "9851098765",
        "email": "sita@himalayanmed.com",
        "address": "Lalitpur, Nepal",
        "pan_vat_number": "309876543",
    }
    response = client.post("/api/v1/suppliers", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["success"] is True
    assert body["data"]["name"] == "Himalayan Med Supplies"
    assert body["data"]["is_active"] is True
