def test_login_success(client):
    """Test successful pharmacy user authentication."""
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "admin", "password": "SecurePassword123!"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "access_token" in data["data"]
    assert data["data"]["token_type"] == "bearer"
    assert data["data"]["user"]["username"] == "admin"


def test_login_invalid_credentials(client):
    """Test login rejection with invalid password."""
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "admin", "password": "WrongPassword!"},
    )
    assert response.status_code == 401
    data = response.json()
    assert data["success"] is False
    assert data["error"]["code"] == "INVALID_CREDENTIALS"


def test_login_missing_fields_validation_error(client):
    """Test validation error when password is missing."""
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "admin"},
    )
    assert response.status_code == 422
    data = response.json()
    assert data["success"] is False
    assert data["error"]["code"] == "VALIDATION_ERROR"
