import uuid
from datetime import datetime, date, timezone
from decimal import Decimal

# In-memory storage - will be replaced by PostgreSQL + SQLAlchemy later
products: dict[uuid.UUID, dict] = {}
suppliers: dict[uuid.UUID, dict] = {}
batches: dict[uuid.UUID, dict] = {}
stock_adjustments: dict[uuid.UUID, dict] = {}
stock_movement_logs: list[dict] = []

def seed_sample_data():
    """Pre-populate some sample data for testing and development."""
    # Create 3 sample products
    p1_id = uuid.UUID("11111111-1111-1111-1111-111111111111")
    p2_id = uuid.UUID("22222222-2222-2222-2222-222222222222")
    p3_id = uuid.UUID("33333333-3333-3333-3333-333333333333")
    
    now = datetime.now(timezone.utc)
    
    products[p1_id] = {
        "id": p1_id,
        "code": "MED-PAR-500",
        "name": "Paracetamol 500mg",
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("60.00"),
        "default_purchase_price": Decimal("45.00"),
        "barcode": "8901234567890",
        "reorder_level": 15,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    
    products[p2_id] = {
        "id": p2_id,
        "code": "MED-AMX-250",
        "name": "Amoxicillin 250mg",
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("120.00"),
        "default_purchase_price": Decimal("85.00"),
        "barcode": "8901234567891",
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    
    products[p3_id] = {
        "id": p3_id,
        "code": "COS-FAC-001",
        "name": "Face Wash 100ml",
        "category": "Cosmetic",
        "unit": "Bottle",
        "mrp": Decimal("250.00"),
        "default_purchase_price": Decimal("180.00"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    
    # Create 1 sample supplier
    s1_id = uuid.UUID("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa")
    suppliers[s1_id] = {
        "id": s1_id,
        "name": "Nepal Pharma Distributors",
        "contact_person": "Ram Sharma",
        "phone": "9841234567",
        "email": "ram@nepalpharma.com",
        "address": "Kathmandu, Nepal",
        "pan_vat_number": "301234567",
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    
    # Create sample batches for products
    b1_id = uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbb01")
    b2_id = uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbb02")
    b3_id = uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbb03")
    b4_id = uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbb04")
    
    batches[b1_id] = {
        "id": b1_id,
        "product_id": p1_id,
        "batch_number": "BCH-2026-01",
        "expiry_date": date(2026, 11, 30),  # Expires soon (within 60 days)
        "purchase_cost": Decimal("42.00"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }
    
    batches[b2_id] = {
        "id": b2_id,
        "product_id": p1_id,
        "batch_number": "BCH-2026-02",
        "expiry_date": date(2027, 5, 15),
        "purchase_cost": Decimal("45.00"),
        "quantity": 25,
        "is_active": True,
        "created_at": now,
    }
    
    batches[b3_id] = {
        "id": b3_id,
        "product_id": p2_id,
        "batch_number": "BCH-2026-03",
        "expiry_date": date(2027, 3, 20),
        "purchase_cost": Decimal("85.00"),
        "quantity": 5,  # Low stock (below reorder_level of 10)
        "is_active": True,
        "created_at": now,
    }
    
    batches[b4_id] = {
        "id": b4_id,
        "product_id": p3_id,
        "batch_number": "BCH-2026-04",
        "expiry_date": date(2028, 1, 1),
        "purchase_cost": Decimal("180.00"),
        "quantity": 3,  # Low stock (below reorder_level of 5)
        "is_active": True,
        "created_at": now,
    }
