from datetime import timedelta
import jwt
from app.core.config import settings
from app.core.security import create_access_token


def test_login_success(client):
    """Test successful pharmacy user authentication using real bcrypt and database."""
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
    assert data["data"]["user"]["role"] == "Pharmacy System User"


def test_login_with_email(client):
    """Test successful pharmacy user authentication using email identifier."""
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "admin@pharmakon.com", "password": "SecurePassword123!"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
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


def test_login_nonexistent_user(client):
    """Test login rejection with nonexistent username."""
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "unknown_user", "password": "AnyPassword123!"},
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


def test_auth_me_with_valid_jwt(client):
    """Test /auth/me endpoint using real signed JWT token."""
    login_res = client.post(
        "/api/v1/auth/login",
        json={"username": "admin", "password": "SecurePassword123!"},
    )
    token = login_res.json()["data"]["access_token"]

    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["username"] == "admin"
    assert data["data"]["email"] == "admin@pharmakon.com"


def test_auth_me_unauthorized_without_token(client):
    """Test /auth/me rejection when Authorization header is absent."""
    response = client.get("/api/v1/auth/me")
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "UNAUTHORIZED"


def test_auth_me_invalid_token(client):
    """Test /auth/me rejection with invalid JWT token."""
    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": "Bearer not.a.valid.token"},
    )
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "INVALID_TOKEN"


def test_auth_me_expired_token(client):
    """Test /auth/me rejection with an expired JWT token."""
    expired_token = create_access_token(
        subject="00000000-0000-0000-0000-000000000001",
        role="Pharmacy System User",
        username="admin",
        expires_delta=timedelta(seconds=-10),
    )
    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {expired_token}"},
    )
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "TOKEN_EXPIRED"
