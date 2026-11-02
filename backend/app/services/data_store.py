import uuid
from datetime import datetime, date, timezone
from decimal import Decimal

# In-memory storage - operational store populated from Aayushman Pharmacy live records
products: dict[uuid.UUID, dict] = {}
suppliers: dict[uuid.UUID, dict] = {}
batches: dict[uuid.UUID, dict] = {}
stock_adjustments: dict[uuid.UUID, dict] = {}
stock_movement_logs: list[dict] = []

def seed_sample_data():
    """Pre-populate operational pharmacy records for Aayushman Pharmacy."""
    products.clear()
    suppliers.clear()
    batches.clear()
    stock_adjustments.clear()
    stock_movement_logs.clear()

    now = datetime.now(timezone.utc)

    # 1. Registered Suppliers
    s1_id = uuid.UUID("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa")
    s2_id = uuid.UUID("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaa02")
    s3_id = uuid.UUID("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaa03")
    suppliers[s1_id] = {
        "id": s1_id,
        "name": "Nepal Pharma Distributors",
        "contact_person": "Ram Sharma",
        "phone": "9841234567",
        "email": "ram@nepalpharma.com",
        "address": "Birgunj-8, Link Road, Nepal",
        "pan_vat_number": "301234567",
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    suppliers[s2_id] = {
        "id": s2_id,
        "name": "Himalayan Healthcare Wholesalers",
        "contact_person": "Sunil Shrestha",
        "phone": "9851087654",
        "email": "sales@himalayanhealth.com.np",
        "address": "Kathmandu, Nepal",
        "pan_vat_number": "309876543",
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    suppliers[s3_id] = {
        "id": s3_id,
        "name": "Lomus Med Supply Agencies",
        "contact_person": "Binod Koirala",
        "phone": "9801234568",
        "email": "info@lomusmed.com",
        "address": "Birgunj, Nepal",
        "pan_vat_number": "308765432",
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }

    # 2. Operational Products & Batches
    # Include test regression anchors first
    p1_id = uuid.UUID("11111111-1111-1111-1111-111111111111")
    p2_id = uuid.UUID("22222222-2222-2222-2222-222222222222")
    p3_id = uuid.UUID("33333333-3333-3333-3333-333333333333")
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

    # Regression batches - BCH-2026-01 expires soonest (2026-11-30)
    b1_id = uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbb01")
    b2_id = uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbb02")
    b3_id = uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbb03")
    b4_id = uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbb04")
    batches[b1_id] = {
        "id": b1_id,
        "product_id": p1_id,
        "batch_number": "BCH-2026-01",
        "expiry_date": date(2026, 11, 30),
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
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }
    batches[b4_id] = {
        "id": b4_id,
        "product_id": p3_id,
        "batch_number": "BCH-2026-04",
        "expiry_date": date(2028, 1, 1),
        "purchase_cost": Decimal("180.00"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # FLEXON TAB
    p_id_101 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000100")
    products[p_id_101] = {
        "id": p_id_101,
        "code": "MED-FLEXONTA",
        "name": 'FLEXON TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("26.34"),
        "default_purchase_price": Decimal("21.07"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_101 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000101")
    batches[b_id_101] = {
        "id": b_id_101,
        "product_id": p_id_101,
        "batch_number": "BCH-MEDFLE-28",
        "expiry_date": date(2028, 6, 21),
        "purchase_cost": Decimal("21.07"),
        "quantity": 48,
        "is_active": True,
        "created_at": now,
    }

    # DIVON GEL 30MG
    p_id_102 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000101")
    products[p_id_102] = {
        "id": p_id_102,
        "code": "12",
        "name": 'DIVON GEL 30MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("255.04"),
        "default_purchase_price": Decimal("204.03"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_102 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000102")
    batches[b_id_102] = {
        "id": b_id_102,
        "product_id": p_id_102,
        "batch_number": "BCH-12-27",
        "expiry_date": date(2027, 7, 22),
        "purchase_cost": Decimal("204.03"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # COUMADIN 2MG TAB
    p_id_103 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000102")
    products[p_id_103] = {
        "id": p_id_103,
        "code": "3628",
        "name": 'COUMADIN 2MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("41.49"),
        "default_purchase_price": Decimal("33.19"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_103 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000103")
    batches[b_id_103] = {
        "id": b_id_103,
        "product_id": p_id_103,
        "batch_number": "BCH-3628-28",
        "expiry_date": date(2028, 8, 23),
        "purchase_cost": Decimal("33.19"),
        "quantity": 29,
        "is_active": True,
        "created_at": now,
    }

    # TAB LOSPIL 50MG
    p_id_104 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000103")
    products[p_id_104] = {
        "id": p_id_104,
        "code": "MED-TABLOSPI",
        "name": 'TAB LOSPIL 50MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("78.31"),
        "default_purchase_price": Decimal("62.65"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_104 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000104")
    batches[b_id_104] = {
        "id": b_id_104,
        "product_id": p_id_104,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 24),
        "purchase_cost": Decimal("62.65"),
        "quantity": 23,
        "is_active": True,
        "created_at": now,
    }

    # TAB LOSPIL 75MG
    p_id_105 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000104")
    products[p_id_105] = {
        "id": p_id_105,
        "code": "MED-TABLOSPI-1",
        "name": 'TAB LOSPIL 75MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("123.64"),
        "default_purchase_price": Decimal("98.91"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_105 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000105")
    batches[b_id_105] = {
        "id": b_id_105,
        "product_id": p_id_105,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 25),
        "purchase_cost": Decimal("98.91"),
        "quantity": 18,
        "is_active": True,
        "created_at": now,
    }

    # TAB LOSPIL -H
    p_id_106 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000105")
    products[p_id_106] = {
        "id": p_id_106,
        "code": "MED-TABLOSPI-2",
        "name": 'TAB LOSPIL -H',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("183.78"),
        "default_purchase_price": Decimal("147.02"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_106 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000106")
    batches[b_id_106] = {
        "id": b_id_106,
        "product_id": p_id_106,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 26),
        "purchase_cost": Decimal("147.02"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB METOCARD 12.5 ER
    p_id_107 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000106")
    products[p_id_107] = {
        "id": p_id_107,
        "code": "MED-TABMETOC",
        "name": 'TAB METOCARD 12.5 ER',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("68.99"),
        "default_purchase_price": Decimal("55.19"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_107 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000107")
    batches[b_id_107] = {
        "id": b_id_107,
        "product_id": p_id_107,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 27),
        "purchase_cost": Decimal("55.19"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB METOCARD 25ER
    p_id_108 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000107")
    products[p_id_108] = {
        "id": p_id_108,
        "code": "MED-TABMETOC-1",
        "name": 'TAB METOCARD 25ER',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("107.15"),
        "default_purchase_price": Decimal("85.72"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_108 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000108")
    batches[b_id_108] = {
        "id": b_id_108,
        "product_id": p_id_108,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 1),
        "purchase_cost": Decimal("85.72"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB MYOXIN 0.25MG
    p_id_109 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000108")
    products[p_id_109] = {
        "id": p_id_109,
        "code": "MED-TABMYOXI",
        "name": 'TAB MYOXIN 0.25MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("30.82"),
        "default_purchase_price": Decimal("24.66"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_109 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000109")
    batches[b_id_109] = {
        "id": b_id_109,
        "product_id": p_id_109,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 2),
        "purchase_cost": Decimal("24.66"),
        "quantity": 19,
        "is_active": True,
        "created_at": now,
    }

    # CAP NEUROLIN 75MG
    p_id_110 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000109")
    products[p_id_110] = {
        "id": p_id_110,
        "code": "C005530",
        "name": 'CAP NEUROLIN 75MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("144.03"),
        "default_purchase_price": Decimal("115.22"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_110 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000110")
    batches[b_id_110] = {
        "id": b_id_110,
        "product_id": p_id_110,
        "batch_number": "BCH-C00553-27",
        "expiry_date": date(2027, 3, 3),
        "purchase_cost": Decimal("115.22"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # TAB VECOXIB 90MG
    p_id_111 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000110")
    products[p_id_111] = {
        "id": p_id_111,
        "code": "MED-TABVECOX",
        "name": 'TAB VECOXIB 90MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("263.49"),
        "default_purchase_price": Decimal("210.79"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_111 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000111")
    batches[b_id_111] = {
        "id": b_id_111,
        "product_id": p_id_111,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 4),
        "purchase_cost": Decimal("210.79"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # TAB VEGAMIN 1500MG
    p_id_112 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000111")
    products[p_id_112] = {
        "id": p_id_112,
        "code": "MED-TABVEGAM",
        "name": 'TAB VEGAMIN 1500MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("275.04"),
        "default_purchase_price": Decimal("220.03"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_112 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000112")
    batches[b_id_112] = {
        "id": b_id_112,
        "product_id": p_id_112,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 5),
        "purchase_cost": Decimal("220.03"),
        "quantity": 9,
        "is_active": True,
        "created_at": now,
    }

    # TAB OSTOVIT
    p_id_113 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000112")
    products[p_id_113] = {
        "id": p_id_113,
        "code": "MED-TABOSTOV",
        "name": 'TAB OSTOVIT',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("51.04"),
        "default_purchase_price": Decimal("40.83"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_113 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000113")
    batches[b_id_113] = {
        "id": b_id_113,
        "product_id": p_id_113,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 6),
        "purchase_cost": Decimal("40.83"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # CAP OXIL 500MG
    p_id_114 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000113")
    products[p_id_114] = {
        "id": p_id_114,
        "code": "C005534",
        "name": 'CAP OXIL 500MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("125.57"),
        "default_purchase_price": Decimal("100.46"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_114 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000114")
    batches[b_id_114] = {
        "id": b_id_114,
        "product_id": p_id_114,
        "batch_number": "BCH-C00553-27",
        "expiry_date": date(2027, 7, 7),
        "purchase_cost": Decimal("100.46"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB ROSAV 10MG
    p_id_115 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000114")
    products[p_id_115] = {
        "id": p_id_115,
        "code": "MED-TABROSAV",
        "name": 'TAB ROSAV 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("183.65"),
        "default_purchase_price": Decimal("146.92"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_115 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000115")
    batches[b_id_115] = {
        "id": b_id_115,
        "product_id": p_id_115,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 8),
        "purchase_cost": Decimal("146.92"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB ROSAV 20MG
    p_id_116 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000115")
    products[p_id_116] = {
        "id": p_id_116,
        "code": "MED-TABROSAV-1",
        "name": 'TAB ROSAV 20MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("326.51"),
        "default_purchase_price": Decimal("261.21"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_116 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000116")
    batches[b_id_116] = {
        "id": b_id_116,
        "product_id": p_id_116,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 9),
        "purchase_cost": Decimal("261.21"),
        "quantity": 1,
        "is_active": True,
        "created_at": now,
    }

    # TAB SGLIP -25
    p_id_117 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000116")
    products[p_id_117] = {
        "id": p_id_117,
        "code": "MED-TABSGLIP",
        "name": 'TAB SGLIP -25',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("153.01"),
        "default_purchase_price": Decimal("122.41"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_117 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000117")
    batches[b_id_117] = {
        "id": b_id_117,
        "product_id": p_id_117,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 10),
        "purchase_cost": Decimal("122.41"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB SGLIP -50MG
    p_id_118 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000117")
    products[p_id_118] = {
        "id": p_id_118,
        "code": "MED-TABSGLIP-1",
        "name": 'TAB SGLIP -50MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("202.95"),
        "default_purchase_price": Decimal("162.36"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_118 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000118")
    batches[b_id_118] = {
        "id": b_id_118,
        "product_id": p_id_118,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 11),
        "purchase_cost": Decimal("162.36"),
        "quantity": 7,
        "is_active": True,
        "created_at": now,
    }

    # TAB AMIP 10MG
    p_id_119 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000118")
    products[p_id_119] = {
        "id": p_id_119,
        "code": "MED-TABAMIP1",
        "name": 'TAB AMIP 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("49.01"),
        "default_purchase_price": Decimal("39.21"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_119 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000119")
    batches[b_id_119] = {
        "id": b_id_119,
        "product_id": p_id_119,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 12),
        "purchase_cost": Decimal("39.21"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB AMIP 25MG
    p_id_120 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000119")
    products[p_id_120] = {
        "id": p_id_120,
        "code": "MED-TABAMIP2",
        "name": 'TAB AMIP 25MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("76.51"),
        "default_purchase_price": Decimal("61.21"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_120 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000120")
    batches[b_id_120] = {
        "id": b_id_120,
        "product_id": p_id_120,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 13),
        "purchase_cost": Decimal("61.21"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB CINAR 75MG
    p_id_121 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000120")
    products[p_id_121] = {
        "id": p_id_121,
        "code": "MED-TABCINAR",
        "name": 'TAB CINAR 75MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("306.08"),
        "default_purchase_price": Decimal("244.86"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_121 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000121")
    batches[b_id_121] = {
        "id": b_id_121,
        "product_id": p_id_121,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 14),
        "purchase_cost": Decimal("244.86"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB LOSPO 25MG
    p_id_122 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000121")
    products[p_id_122] = {
        "id": p_id_122,
        "code": "MED-TABLOSPO",
        "name": 'TAB LOSPO 25MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("63.16"),
        "default_purchase_price": Decimal("50.53"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_122 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000122")
    batches[b_id_122] = {
        "id": b_id_122,
        "product_id": p_id_122,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 15),
        "purchase_cost": Decimal("50.53"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # METRO GEL
    p_id_123 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000122")
    products[p_id_123] = {
        "id": p_id_123,
        "code": "MED-METROGEL",
        "name": 'METRO GEL',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("76.50"),
        "default_purchase_price": Decimal("61.20"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_123 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000123")
    batches[b_id_123] = {
        "id": b_id_123,
        "product_id": p_id_123,
        "batch_number": "BCH-MEDMET-28",
        "expiry_date": date(2028, 4, 16),
        "purchase_cost": Decimal("61.20"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB TROV
    p_id_124 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000123")
    products[p_id_124] = {
        "id": p_id_124,
        "code": "MED-TABTROV",
        "name": 'TAB TROV',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("109.66"),
        "default_purchase_price": Decimal("87.73"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_124 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000124")
    batches[b_id_124] = {
        "id": b_id_124,
        "product_id": p_id_124,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 17),
        "purchase_cost": Decimal("87.73"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB AMLONG A 25
    p_id_125 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000124")
    products[p_id_125] = {
        "id": p_id_125,
        "code": "MED-TABAMLON",
        "name": 'TAB AMLONG A 25',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("119.06"),
        "default_purchase_price": Decimal("95.25"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_125 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000125")
    batches[b_id_125] = {
        "id": b_id_125,
        "product_id": p_id_125,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 18),
        "purchase_cost": Decimal("95.25"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB AMLONG H
    p_id_126 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000125")
    products[p_id_126] = {
        "id": p_id_126,
        "code": "MED-TABAMLON-1",
        "name": 'TAB AMLONG H',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("102.38"),
        "default_purchase_price": Decimal("81.90"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_126 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000126")
    batches[b_id_126] = {
        "id": b_id_126,
        "product_id": p_id_126,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 19),
        "purchase_cost": Decimal("81.90"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB ANGIZAAR -H
    p_id_127 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000126")
    products[p_id_127] = {
        "id": p_id_127,
        "code": "MED-TABANGIZ",
        "name": 'TAB ANGIZAAR -H',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("425.01"),
        "default_purchase_price": Decimal("340.01"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_127 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000127")
    batches[b_id_127] = {
        "id": b_id_127,
        "product_id": p_id_127,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 20),
        "purchase_cost": Decimal("340.01"),
        "quantity": 17,
        "is_active": True,
        "created_at": now,
    }

    # TAB ANGIZAR 50MG
    p_id_128 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000127")
    products[p_id_128] = {
        "id": p_id_128,
        "code": "MED-TABANGIZ-1",
        "name": 'TAB ANGIZAR 50MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("72.67"),
        "default_purchase_price": Decimal("58.14"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_128 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000128")
    batches[b_id_128] = {
        "id": b_id_128,
        "product_id": p_id_128,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 21),
        "purchase_cost": Decimal("58.14"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB HOPACE 5MG
    p_id_129 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000128")
    products[p_id_129] = {
        "id": p_id_129,
        "code": "MED-TABHOPAC",
        "name": 'TAB HOPACE 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("448.58"),
        "default_purchase_price": Decimal("358.86"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_129 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000129")
    batches[b_id_129] = {
        "id": b_id_129,
        "product_id": p_id_129,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 22),
        "purchase_cost": Decimal("358.86"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB MELMET 500MG
    p_id_130 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000129")
    products[p_id_130] = {
        "id": p_id_130,
        "code": "MED-TABMELME",
        "name": 'TAB MELMET 500MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("40.99"),
        "default_purchase_price": Decimal("32.79"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_130 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000130")
    batches[b_id_130] = {
        "id": b_id_130,
        "product_id": p_id_130,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 23),
        "purchase_cost": Decimal("32.79"),
        "quantity": 27,
        "is_active": True,
        "created_at": now,
    }

    # TAB LINICS 5MG
    p_id_131 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000130")
    products[p_id_131] = {
        "id": p_id_131,
        "code": "MED-TABLINIC",
        "name": 'TAB LINICS 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("206.32"),
        "default_purchase_price": Decimal("165.06"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_131 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000131")
    batches[b_id_131] = {
        "id": b_id_131,
        "product_id": p_id_131,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 24),
        "purchase_cost": Decimal("165.06"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB LINOX 5MG
    p_id_132 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000131")
    products[p_id_132] = {
        "id": p_id_132,
        "code": "MED-TABLINOX",
        "name": 'TAB LINOX 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("204.03"),
        "default_purchase_price": Decimal("163.22"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_132 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000132")
    batches[b_id_132] = {
        "id": b_id_132,
        "product_id": p_id_132,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 25),
        "purchase_cost": Decimal("163.22"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB LINOX -M 500MG
    p_id_133 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000132")
    products[p_id_133] = {
        "id": p_id_133,
        "code": "MED-TABLINOX-1",
        "name": 'TAB LINOX -M 500MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("214.22"),
        "default_purchase_price": Decimal("171.38"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_133 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000133")
    batches[b_id_133] = {
        "id": b_id_133,
        "product_id": p_id_133,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 26),
        "purchase_cost": Decimal("171.38"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELSARTAN 80MG
    p_id_134 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000133")
    products[p_id_134] = {
        "id": p_id_134,
        "code": "MED-TABTELSA",
        "name": 'TAB TELSARTAN 80MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("204.79"),
        "default_purchase_price": Decimal("163.83"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_134 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000134")
    batches[b_id_134] = {
        "id": b_id_134,
        "product_id": p_id_134,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 27),
        "purchase_cost": Decimal("163.83"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB DAFODIL 10MG
    p_id_135 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000134")
    products[p_id_135] = {
        "id": p_id_135,
        "code": "MED-TABDAFOD",
        "name": 'TAB DAFODIL 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("224.88"),
        "default_purchase_price": Decimal("179.90"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_135 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000135")
    batches[b_id_135] = {
        "id": b_id_135,
        "product_id": p_id_135,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 1),
        "purchase_cost": Decimal("179.90"),
        "quantity": 33,
        "is_active": True,
        "created_at": now,
    }

    # OROLYTE POWDER
    p_id_136 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000135")
    products[p_id_136] = {
        "id": p_id_136,
        "code": "MED-OROLYTEP",
        "name": 'OROLYTE POWDER',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("10.14"),
        "default_purchase_price": Decimal("8.11"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_136 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000136")
    batches[b_id_136] = {
        "id": b_id_136,
        "product_id": p_id_136,
        "batch_number": "BCH-MEDORO-27",
        "expiry_date": date(2027, 5, 2),
        "purchase_cost": Decimal("8.11"),
        "quantity": 432,
        "is_active": True,
        "created_at": now,
    }

    # TAB APICLOT 5MG
    p_id_137 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000136")
    products[p_id_137] = {
        "id": p_id_137,
        "code": "MED-TABAPICL",
        "name": 'TAB APICLOT 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("350.54"),
        "default_purchase_price": Decimal("280.43"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_137 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000137")
    batches[b_id_137] = {
        "id": b_id_137,
        "product_id": p_id_137,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 3),
        "purchase_cost": Decimal("280.43"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB GLYCIPHAGE SR 1GM
    p_id_138 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000137")
    products[p_id_138] = {
        "id": p_id_138,
        "code": "MED-TABGLYCI",
        "name": 'TAB GLYCIPHAGE SR 1GM',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("67.90"),
        "default_purchase_price": Decimal("54.32"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_138 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000138")
    batches[b_id_138] = {
        "id": b_id_138,
        "product_id": p_id_138,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 4),
        "purchase_cost": Decimal("54.32"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # TAB GLYCIPHAGE 850MG
    p_id_139 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000138")
    products[p_id_139] = {
        "id": p_id_139,
        "code": "MED-TABGLYCI-1",
        "name": 'TAB GLYCIPHAGE 850MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("38.21"),
        "default_purchase_price": Decimal("30.57"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_139 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000139")
    batches[b_id_139] = {
        "id": b_id_139,
        "product_id": p_id_139,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 5),
        "purchase_cost": Decimal("30.57"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # TAB GLYCIPHAGE
    p_id_140 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000139")
    products[p_id_140] = {
        "id": p_id_140,
        "code": "MED-TABGLYCI-2",
        "name": 'TAB GLYCIPHAGE',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("38.76"),
        "default_purchase_price": Decimal("31.01"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_140 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000140")
    batches[b_id_140] = {
        "id": b_id_140,
        "product_id": p_id_140,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 6),
        "purchase_cost": Decimal("31.01"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # TAB GLYCIPHAGE SR 500
    p_id_141 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000140")
    products[p_id_141] = {
        "id": p_id_141,
        "code": "MED-TABGLYCI-3",
        "name": 'TAB GLYCIPHAGE SR 500',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("39.77"),
        "default_purchase_price": Decimal("31.82"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_141 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000141")
    batches[b_id_141] = {
        "id": b_id_141,
        "product_id": p_id_141,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 7),
        "purchase_cost": Decimal("31.82"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB HAEMOGEN
    p_id_142 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000141")
    products[p_id_142] = {
        "id": p_id_142,
        "code": "MED-TABHAEMO",
        "name": 'TAB HAEMOGEN',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("34.21"),
        "default_purchase_price": Decimal("27.37"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_142 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000142")
    batches[b_id_142] = {
        "id": b_id_142,
        "product_id": p_id_142,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 8),
        "purchase_cost": Decimal("27.37"),
        "quantity": 24,
        "is_active": True,
        "created_at": now,
    }

    # TAB TURBOVAS 5MG
    p_id_143 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000142")
    products[p_id_143] = {
        "id": p_id_143,
        "code": "MED-TABTURBO",
        "name": 'TAB TURBOVAS 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("183.99"),
        "default_purchase_price": Decimal("147.19"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_143 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000143")
    batches[b_id_143] = {
        "id": b_id_143,
        "product_id": p_id_143,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 9),
        "purchase_cost": Decimal("147.19"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB VECOXBI 120MG
    p_id_144 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000143")
    products[p_id_144] = {
        "id": p_id_144,
        "code": "MED-TABVECOX-1",
        "name": 'TAB VECOXBI 120MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("307.67"),
        "default_purchase_price": Decimal("246.14"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_144 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000144")
    batches[b_id_144] = {
        "id": b_id_144,
        "product_id": p_id_144,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 10),
        "purchase_cost": Decimal("246.14"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB LINICS M 850
    p_id_145 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000144")
    products[p_id_145] = {
        "id": p_id_145,
        "code": "MED-TABLINIC-1",
        "name": 'TAB LINICS M 850',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("153.86"),
        "default_purchase_price": Decimal("123.09"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_145 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000145")
    batches[b_id_145] = {
        "id": b_id_145,
        "product_id": p_id_145,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 11),
        "purchase_cost": Decimal("123.09"),
        "quantity": 50,
        "is_active": True,
        "created_at": now,
    }

    # TAB IROCARE XT
    p_id_146 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000145")
    products[p_id_146] = {
        "id": p_id_146,
        "code": "MED-TABIROCA",
        "name": 'TAB IROCARE XT',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("143.39"),
        "default_purchase_price": Decimal("114.71"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_146 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000146")
    batches[b_id_146] = {
        "id": b_id_146,
        "product_id": p_id_146,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 12),
        "purchase_cost": Decimal("114.71"),
        "quantity": 16,
        "is_active": True,
        "created_at": now,
    }

    # TAB NOX 400
    p_id_147 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000146")
    products[p_id_147] = {
        "id": p_id_147,
        "code": "MED-TABNOX40",
        "name": 'TAB NOX 400',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("59.97"),
        "default_purchase_price": Decimal("47.98"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_147 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000147")
    batches[b_id_147] = {
        "id": b_id_147,
        "product_id": p_id_147,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 13),
        "purchase_cost": Decimal("47.98"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB MYOCIL 5MG
    p_id_148 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000147")
    products[p_id_148] = {
        "id": p_id_148,
        "code": "MED-TABMYOCI",
        "name": 'TAB MYOCIL 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("51.41"),
        "default_purchase_price": Decimal("41.13"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_148 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000148")
    batches[b_id_148] = {
        "id": b_id_148,
        "product_id": p_id_148,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 14),
        "purchase_cost": Decimal("41.13"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB SOBICA 300MG
    p_id_149 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000148")
    products[p_id_149] = {
        "id": p_id_149,
        "code": "MED-TABSOBIC",
        "name": 'TAB SOBICA 300MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("308.40"),
        "default_purchase_price": Decimal("246.72"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_149 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000149")
    batches[b_id_149] = {
        "id": b_id_149,
        "product_id": p_id_149,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 15),
        "purchase_cost": Decimal("246.72"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # TAB ROVISTA 10MG
    p_id_150 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000149")
    products[p_id_150] = {
        "id": p_id_150,
        "code": "MED-TABROVIS",
        "name": 'TAB ROVISTA 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("262.11"),
        "default_purchase_price": Decimal("209.69"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_150 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000150")
    batches[b_id_150] = {
        "id": b_id_150,
        "product_id": p_id_150,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 16),
        "purchase_cost": Decimal("209.69"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # TAB ROVISTA 5MG
    p_id_151 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000150")
    products[p_id_151] = {
        "id": p_id_151,
        "code": "MED-TABROVIS-1",
        "name": 'TAB ROVISTA 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("168.92"),
        "default_purchase_price": Decimal("135.14"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_151 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000151")
    batches[b_id_151] = {
        "id": b_id_151,
        "product_id": p_id_151,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 17),
        "purchase_cost": Decimal("135.14"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB ENVAS 5MG
    p_id_152 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000151")
    products[p_id_152] = {
        "id": p_id_152,
        "code": "MED-TABENVAS",
        "name": 'TAB ENVAS 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("61.39"),
        "default_purchase_price": Decimal("49.11"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_152 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000152")
    batches[b_id_152] = {
        "id": b_id_152,
        "product_id": p_id_152,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 18),
        "purchase_cost": Decimal("49.11"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # TAB VASTATIN 20MG
    p_id_153 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000152")
    products[p_id_153] = {
        "id": p_id_153,
        "code": "MED-TABVASTA",
        "name": 'TAB VASTATIN 20MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("209.26"),
        "default_purchase_price": Decimal("167.41"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_153 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000153")
    batches[b_id_153] = {
        "id": b_id_153,
        "product_id": p_id_153,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 19),
        "purchase_cost": Decimal("167.41"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # TAB VERSA -25MG
    p_id_154 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000153")
    products[p_id_154] = {
        "id": p_id_154,
        "code": "MED-TABVERSA",
        "name": 'TAB VERSA -25MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("66.11"),
        "default_purchase_price": Decimal("52.89"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_154 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000154")
    batches[b_id_154] = {
        "id": b_id_154,
        "product_id": p_id_154,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 20),
        "purchase_cost": Decimal("52.89"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # CAP Q-DOX
    p_id_155 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000154")
    products[p_id_155] = {
        "id": p_id_155,
        "code": "C005576",
        "name": 'CAP Q-DOX',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("59.35"),
        "default_purchase_price": Decimal("47.48"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_155 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000155")
    batches[b_id_155] = {
        "id": b_id_155,
        "product_id": p_id_155,
        "batch_number": "BCH-C00557-28",
        "expiry_date": date(2028, 12, 21),
        "purchase_cost": Decimal("47.48"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB DAFOZ 10MG
    p_id_156 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000155")
    products[p_id_156] = {
        "id": p_id_156,
        "code": "MED-TABDAFOZ",
        "name": 'TAB DAFOZ 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("246.60"),
        "default_purchase_price": Decimal("197.28"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_156 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000156")
    batches[b_id_156] = {
        "id": b_id_156,
        "product_id": p_id_156,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 22),
        "purchase_cost": Decimal("197.28"),
        "quantity": 65,
        "is_active": True,
        "created_at": now,
    }

    # TAB ROVISTA 20MG
    p_id_157 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000156")
    products[p_id_157] = {
        "id": p_id_157,
        "code": "MED-TABROVIS-2",
        "name": 'TAB ROVISTA 20MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("417.09"),
        "default_purchase_price": Decimal("333.67"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_157 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000157")
    batches[b_id_157] = {
        "id": b_id_157,
        "product_id": p_id_157,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 23),
        "purchase_cost": Decimal("333.67"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB ESOZOL FR 40MG
    p_id_158 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000157")
    products[p_id_158] = {
        "id": p_id_158,
        "code": "MED-TABESOZO",
        "name": 'TAB ESOZOL FR 40MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("164.93"),
        "default_purchase_price": Decimal("131.94"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_158 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000158")
    batches[b_id_158] = {
        "id": b_id_158,
        "product_id": p_id_158,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 24),
        "purchase_cost": Decimal("131.94"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB S-AMLONG 2.5
    p_id_159 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000158")
    products[p_id_159] = {
        "id": p_id_159,
        "code": "MED-TABSAMLO",
        "name": 'TAB S-AMLONG 2.5',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("109.69"),
        "default_purchase_price": Decimal("87.75"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_159 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000159")
    batches[b_id_159] = {
        "id": b_id_159,
        "product_id": p_id_159,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 25),
        "purchase_cost": Decimal("87.75"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # LEVECAM 500MG TAB
    p_id_160 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000159")
    products[p_id_160] = {
        "id": p_id_160,
        "code": "MED-LEVECAM5",
        "name": 'LEVECAM 500MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("184.29"),
        "default_purchase_price": Decimal("147.43"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_160 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000160")
    batches[b_id_160] = {
        "id": b_id_160,
        "product_id": p_id_160,
        "batch_number": "BCH-MEDLEV-27",
        "expiry_date": date(2027, 5, 26),
        "purchase_cost": Decimal("147.43"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELSA 40MG
    p_id_161 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000160")
    products[p_id_161] = {
        "id": p_id_161,
        "code": "MED-TABTELSA-1",
        "name": 'TAB TELSA 40MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("156.49"),
        "default_purchase_price": Decimal("125.19"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_161 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000161")
    batches[b_id_161] = {
        "id": b_id_161,
        "product_id": p_id_161,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 27),
        "purchase_cost": Decimal("125.19"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELSA 20MG
    p_id_162 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000161")
    products[p_id_162] = {
        "id": p_id_162,
        "code": "MED-TABTELSA-2",
        "name": 'TAB TELSA 20MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("99.60"),
        "default_purchase_price": Decimal("79.68"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_162 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000162")
    batches[b_id_162] = {
        "id": b_id_162,
        "product_id": p_id_162,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 1),
        "purchase_cost": Decimal("79.68"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # LIPITOP 20MG TAB
    p_id_163 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000162")
    products[p_id_163] = {
        "id": p_id_163,
        "code": "MED-LIPITOP2",
        "name": 'LIPITOP 20MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("361.41"),
        "default_purchase_price": Decimal("289.13"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_163 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000163")
    batches[b_id_163] = {
        "id": b_id_163,
        "product_id": p_id_163,
        "batch_number": "BCH-MEDLIP-28",
        "expiry_date": date(2028, 8, 2),
        "purchase_cost": Decimal("289.13"),
        "quantity": 19,
        "is_active": True,
        "created_at": now,
    }

    # TAB NEBILONG 2.5MG
    p_id_164 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000163")
    products[p_id_164] = {
        "id": p_id_164,
        "code": "MED-TABNEBIL",
        "name": 'TAB NEBILONG 2.5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("245.58"),
        "default_purchase_price": Decimal("196.46"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_164 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000164")
    batches[b_id_164] = {
        "id": b_id_164,
        "product_id": p_id_164,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 3),
        "purchase_cost": Decimal("196.46"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # TAB FARIN 1MG
    p_id_165 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000164")
    products[p_id_165] = {
        "id": p_id_165,
        "code": "MED-TABFARIN",
        "name": 'TAB FARIN 1MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("36.18"),
        "default_purchase_price": Decimal("28.94"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_165 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000165")
    batches[b_id_165] = {
        "id": b_id_165,
        "product_id": p_id_165,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 4),
        "purchase_cost": Decimal("28.94"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # TAB EMPAZ L 25MG
    p_id_166 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000165")
    products[p_id_166] = {
        "id": p_id_166,
        "code": "MED-TABEMPAZ",
        "name": 'TAB EMPAZ L 25MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("515.04"),
        "default_purchase_price": Decimal("412.03"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_166 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000166")
    batches[b_id_166] = {
        "id": b_id_166,
        "product_id": p_id_166,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 5),
        "purchase_cost": Decimal("412.03"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB ROSROL 10MG
    p_id_167 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000166")
    products[p_id_167] = {
        "id": p_id_167,
        "code": "MED-TABROSRO",
        "name": 'TAB ROSROL 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("174.33"),
        "default_purchase_price": Decimal("139.46"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_167 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000167")
    batches[b_id_167] = {
        "id": b_id_167,
        "product_id": p_id_167,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 6),
        "purchase_cost": Decimal("139.46"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB TRABET -S
    p_id_168 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000167")
    products[p_id_168] = {
        "id": p_id_168,
        "code": "MED-TABTRABE",
        "name": 'TAB TRABET -S',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("410.20"),
        "default_purchase_price": Decimal("328.16"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_168 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000168")
    batches[b_id_168] = {
        "id": b_id_168,
        "product_id": p_id_168,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 7),
        "purchase_cost": Decimal("328.16"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB MELMET 500SR
    p_id_169 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000168")
    products[p_id_169] = {
        "id": p_id_169,
        "code": "MED-TABMELME-1",
        "name": 'TAB MELMET 500SR',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("76.31"),
        "default_purchase_price": Decimal("61.05"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_169 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000169")
    batches[b_id_169] = {
        "id": b_id_169,
        "product_id": p_id_169,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 8),
        "purchase_cost": Decimal("61.05"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # TAB DIANORM OD 30MG
    p_id_170 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000169")
    products[p_id_170] = {
        "id": p_id_170,
        "code": "MED-TABDIANO",
        "name": 'TAB DIANORM OD 30MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("123.42"),
        "default_purchase_price": Decimal("98.74"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_170 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000170")
    batches[b_id_170] = {
        "id": b_id_170,
        "product_id": p_id_170,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 9),
        "purchase_cost": Decimal("98.74"),
        "quantity": 18,
        "is_active": True,
        "created_at": now,
    }

    # TAB DIANORM OD 60 MG
    p_id_171 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000170")
    products[p_id_171] = {
        "id": p_id_171,
        "code": "MED-TABDIANO-1",
        "name": 'TAB DIANORM OD 60 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("199.24"),
        "default_purchase_price": Decimal("159.39"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_171 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000171")
    batches[b_id_171] = {
        "id": b_id_171,
        "product_id": p_id_171,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 10),
        "purchase_cost": Decimal("159.39"),
        "quantity": 18,
        "is_active": True,
        "created_at": now,
    }

    # TAB CLOPERT 50MG
    p_id_172 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000171")
    products[p_id_172] = {
        "id": p_id_172,
        "code": "MED-TABCLOPE",
        "name": 'TAB CLOPERT 50MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("153.51"),
        "default_purchase_price": Decimal("122.81"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_172 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000172")
    batches[b_id_172] = {
        "id": b_id_172,
        "product_id": p_id_172,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 11),
        "purchase_cost": Decimal("122.81"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB EFLOZ -10MG
    p_id_173 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000172")
    products[p_id_173] = {
        "id": p_id_173,
        "code": "MED-TABEFLOZ",
        "name": 'TAB EFLOZ -10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("204.66"),
        "default_purchase_price": Decimal("163.73"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_173 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000173")
    batches[b_id_173] = {
        "id": b_id_173,
        "product_id": p_id_173,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 12),
        "purchase_cost": Decimal("163.73"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB SOBICA 500 MG
    p_id_174 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000173")
    products[p_id_174] = {
        "id": p_id_174,
        "code": "MED-TABSOBIC-1",
        "name": 'TAB SOBICA 500 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("516.77"),
        "default_purchase_price": Decimal("413.42"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_174 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000174")
    batches[b_id_174] = {
        "id": b_id_174,
        "product_id": p_id_174,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 13),
        "purchase_cost": Decimal("413.42"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # AMLOD 2.5 TAB
    p_id_175 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000174")
    products[p_id_175] = {
        "id": p_id_175,
        "code": "134",
        "name": 'AMLOD 2.5 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("34.95"),
        "default_purchase_price": Decimal("27.96"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_175 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000175")
    batches[b_id_175] = {
        "id": b_id_175,
        "product_id": p_id_175,
        "batch_number": "BCH-134-28",
        "expiry_date": date(2028, 8, 14),
        "purchase_cost": Decimal("27.96"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # AMLOD 5 TAB
    p_id_176 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000175")
    products[p_id_176] = {
        "id": p_id_176,
        "code": "135",
        "name": 'AMLOD 5 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("75.97"),
        "default_purchase_price": Decimal("60.78"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_176 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000176")
    batches[b_id_176] = {
        "id": b_id_176,
        "product_id": p_id_176,
        "batch_number": "BCH-135-27",
        "expiry_date": date(2027, 9, 15),
        "purchase_cost": Decimal("60.78"),
        "quantity": 40,
        "is_active": True,
        "created_at": now,
    }

    # AMLOD -L TAB
    p_id_177 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000176")
    products[p_id_177] = {
        "id": p_id_177,
        "code": "136",
        "name": 'AMLOD -L TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("192.21"),
        "default_purchase_price": Decimal("153.77"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_177 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000177")
    batches[b_id_177] = {
        "id": b_id_177,
        "product_id": p_id_177,
        "batch_number": "BCH-136-28",
        "expiry_date": date(2028, 10, 16),
        "purchase_cost": Decimal("153.77"),
        "quantity": 140,
        "is_active": True,
        "created_at": now,
    }

    # ATOR 10 MG TAB
    p_id_178 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000177")
    products[p_id_178] = {
        "id": p_id_178,
        "code": "145",
        "name": 'ATOR 10 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("109.59"),
        "default_purchase_price": Decimal("87.67"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_178 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000178")
    batches[b_id_178] = {
        "id": b_id_178,
        "product_id": p_id_178,
        "batch_number": "BCH-145-27",
        "expiry_date": date(2027, 11, 17),
        "purchase_cost": Decimal("87.67"),
        "quantity": 90,
        "is_active": True,
        "created_at": now,
    }

    # ATOR 20MG TAB
    p_id_179 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000178")
    products[p_id_179] = {
        "id": p_id_179,
        "code": "146",
        "name": 'ATOR 20MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("212.40"),
        "default_purchase_price": Decimal("169.92"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_179 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000179")
    batches[b_id_179] = {
        "id": b_id_179,
        "product_id": p_id_179,
        "batch_number": "BCH-146-28",
        "expiry_date": date(2028, 12, 18),
        "purchase_cost": Decimal("169.92"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # BRICA-BM 100ML SYP
    p_id_180 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000179")
    products[p_id_180] = {
        "id": p_id_180,
        "code": "160",
        "name": 'BRICA-BM 100ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("157.39"),
        "default_purchase_price": Decimal("125.91"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_180 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000180")
    batches[b_id_180] = {
        "id": b_id_180,
        "product_id": p_id_180,
        "batch_number": "BCH-160-27",
        "expiry_date": date(2027, 1, 19),
        "purchase_cost": Decimal("125.91"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # CTZ TAB
    p_id_181 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000180")
    products[p_id_181] = {
        "id": p_id_181,
        "code": "197",
        "name": 'CTZ TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("56.88"),
        "default_purchase_price": Decimal("45.50"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_181 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000181")
    batches[b_id_181] = {
        "id": b_id_181,
        "product_id": p_id_181,
        "batch_number": "BCH-197-28",
        "expiry_date": date(2028, 2, 20),
        "purchase_cost": Decimal("45.50"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # DIVON SR 100MG
    p_id_182 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000181")
    products[p_id_182] = {
        "id": p_id_182,
        "code": "211",
        "name": 'DIVON SR 100MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("101.31"),
        "default_purchase_price": Decimal("81.05"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_182 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000182")
    batches[b_id_182] = {
        "id": b_id_182,
        "product_id": p_id_182,
        "batch_number": "BCH-211-27",
        "expiry_date": date(2027, 3, 21),
        "purchase_cost": Decimal("81.05"),
        "quantity": 26,
        "is_active": True,
        "created_at": now,
    }

    # FRUSAL TAB
    p_id_183 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000182")
    products[p_id_183] = {
        "id": p_id_183,
        "code": "MED-FRUSALTA",
        "name": 'FRUSAL TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("92.56"),
        "default_purchase_price": Decimal("74.05"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_183 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000183")
    batches[b_id_183] = {
        "id": b_id_183,
        "product_id": p_id_183,
        "batch_number": "BCH-MEDFRU-28",
        "expiry_date": date(2028, 4, 22),
        "purchase_cost": Decimal("74.05"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # LOREE - 1 TAB
    p_id_184 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000183")
    products[p_id_184] = {
        "id": p_id_184,
        "code": "MED-LOREE1TA",
        "name": 'LOREE - 1 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("41.99"),
        "default_purchase_price": Decimal("33.59"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_184 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000184")
    batches[b_id_184] = {
        "id": b_id_184,
        "product_id": p_id_184,
        "batch_number": "BCH-MEDLOR-27",
        "expiry_date": date(2027, 5, 23),
        "purchase_cost": Decimal("33.59"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # LOSAP 25MG TAB
    p_id_185 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000184")
    products[p_id_185] = {
        "id": p_id_185,
        "code": "MED-LOSAP25M",
        "name": 'LOSAP 25MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("67.04"),
        "default_purchase_price": Decimal("53.63"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_185 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000185")
    batches[b_id_185] = {
        "id": b_id_185,
        "product_id": p_id_185,
        "batch_number": "BCH-MEDLOS-28",
        "expiry_date": date(2028, 6, 24),
        "purchase_cost": Decimal("53.63"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # LOSAP 50MG TAB
    p_id_186 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000185")
    products[p_id_186] = {
        "id": p_id_186,
        "code": "MED-LOSAP50M",
        "name": 'LOSAP 50MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("118.30"),
        "default_purchase_price": Decimal("94.64"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_186 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000186")
    batches[b_id_186] = {
        "id": b_id_186,
        "product_id": p_id_186,
        "batch_number": "BCH-MEDLOS-27",
        "expiry_date": date(2027, 7, 25),
        "purchase_cost": Decimal("94.64"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # MINIL-10 TAB
    p_id_187 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000186")
    products[p_id_187] = {
        "id": p_id_187,
        "code": "MED-MINIL10T",
        "name": 'MINIL-10 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("66.71"),
        "default_purchase_price": Decimal("53.37"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_187 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000187")
    batches[b_id_187] = {
        "id": b_id_187,
        "product_id": p_id_187,
        "batch_number": "BCH-MEDMIN-28",
        "expiry_date": date(2028, 8, 26),
        "purchase_cost": Decimal("53.37"),
        "quantity": 9,
        "is_active": True,
        "created_at": now,
    }

    # PANTOP TAB
    p_id_188 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000187")
    products[p_id_188] = {
        "id": p_id_188,
        "code": "MED-PANTOPTA",
        "name": 'PANTOP TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("134.79"),
        "default_purchase_price": Decimal("107.83"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_188 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000188")
    batches[b_id_188] = {
        "id": b_id_188,
        "product_id": p_id_188,
        "batch_number": "BCH-MEDPAN-27",
        "expiry_date": date(2027, 9, 27),
        "purchase_cost": Decimal("107.83"),
        "quantity": 60,
        "is_active": True,
        "created_at": now,
    }

    # RABEPRA 20MG CAPS
    p_id_189 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000188")
    products[p_id_189] = {
        "id": p_id_189,
        "code": "MED-RABEPRA2",
        "name": 'RABEPRA 20MG CAPS',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("130.07"),
        "default_purchase_price": Decimal("104.06"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_189 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000189")
    batches[b_id_189] = {
        "id": b_id_189,
        "product_id": p_id_189,
        "batch_number": "BCH-MEDRAB-28",
        "expiry_date": date(2028, 10, 1),
        "purchase_cost": Decimal("104.06"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # SWICH 100MG DRY SYRP
    p_id_190 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000189")
    products[p_id_190] = {
        "id": p_id_190,
        "code": "MED-SWICH100",
        "name": 'SWICH 100MG DRY SYRP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("198.00"),
        "default_purchase_price": Decimal("158.40"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_190 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000190")
    batches[b_id_190] = {
        "id": b_id_190,
        "product_id": p_id_190,
        "batch_number": "BCH-MEDSWI-27",
        "expiry_date": date(2027, 11, 2),
        "purchase_cost": Decimal("158.40"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAZLOC- 40MG TAB
    p_id_191 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000190")
    products[p_id_191] = {
        "id": p_id_191,
        "code": "MED-TAZLOC40",
        "name": 'TAZLOC- 40MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("169.86"),
        "default_purchase_price": Decimal("135.89"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_191 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000191")
    batches[b_id_191] = {
        "id": b_id_191,
        "product_id": p_id_191,
        "batch_number": "BCH-MEDTAZ-28",
        "expiry_date": date(2028, 12, 3),
        "purchase_cost": Decimal("135.89"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TELMI-H TAB
    p_id_192 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000191")
    products[p_id_192] = {
        "id": p_id_192,
        "code": "MED-TELMIHTA",
        "name": 'TELMI-H TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("183.00"),
        "default_purchase_price": Decimal("146.40"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_192 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000192")
    batches[b_id_192] = {
        "id": b_id_192,
        "product_id": p_id_192,
        "batch_number": "BCH-MEDTEL-27",
        "expiry_date": date(2027, 1, 4),
        "purchase_cost": Decimal("146.40"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # OLZAP 2.5MG
    p_id_193 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000192")
    products[p_id_193] = {
        "id": p_id_193,
        "code": "MED-OLZAP25M",
        "name": 'OLZAP 2.5MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("45.69"),
        "default_purchase_price": Decimal("36.55"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_193 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000193")
    batches[b_id_193] = {
        "id": b_id_193,
        "product_id": p_id_193,
        "batch_number": "BCH-MEDOLZ-28",
        "expiry_date": date(2028, 2, 5),
        "purchase_cost": Decimal("36.55"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # GLYCOMET GP 1 TAB
    p_id_194 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000193")
    products[p_id_194] = {
        "id": p_id_194,
        "code": "MED-GLYCOMET",
        "name": 'GLYCOMET GP 1 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("221.30"),
        "default_purchase_price": Decimal("177.04"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_194 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000194")
    batches[b_id_194] = {
        "id": b_id_194,
        "product_id": p_id_194,
        "batch_number": "BCH-MEDGLY-27",
        "expiry_date": date(2027, 3, 6),
        "purchase_cost": Decimal("177.04"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # EFZIN 10 MG TAB
    p_id_195 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000194")
    products[p_id_195] = {
        "id": p_id_195,
        "code": "MED-EFZIN10M",
        "name": 'EFZIN 10 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("67.21"),
        "default_purchase_price": Decimal("53.77"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_195 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000195")
    batches[b_id_195] = {
        "id": b_id_195,
        "product_id": p_id_195,
        "batch_number": "BCH-MEDEFZ-28",
        "expiry_date": date(2028, 4, 7),
        "purchase_cost": Decimal("53.77"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # PEPSA 10MG TAB
    p_id_196 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000195")
    products[p_id_196] = {
        "id": p_id_196,
        "code": "MED-PEPSA10M",
        "name": 'PEPSA 10MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("183.88"),
        "default_purchase_price": Decimal("147.10"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_196 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000196")
    batches[b_id_196] = {
        "id": b_id_196,
        "product_id": p_id_196,
        "batch_number": "BCH-MEDPEP-27",
        "expiry_date": date(2027, 5, 8),
        "purchase_cost": Decimal("147.10"),
        "quantity": 18,
        "is_active": True,
        "created_at": now,
    }

    # TELMI AM TAB
    p_id_197 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000196")
    products[p_id_197] = {
        "id": p_id_197,
        "code": "MED-TELMIAMT",
        "name": 'TELMI AM TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("162.09"),
        "default_purchase_price": Decimal("129.67"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_197 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000197")
    batches[b_id_197] = {
        "id": b_id_197,
        "product_id": p_id_197,
        "batch_number": "BCH-MEDTEL-28",
        "expiry_date": date(2028, 6, 9),
        "purchase_cost": Decimal("129.67"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TRIAD 10 MG
    p_id_198 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000197")
    products[p_id_198] = {
        "id": p_id_198,
        "code": "MED-TRIAD10M",
        "name": 'TRIAD 10 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("48.54"),
        "default_purchase_price": Decimal("38.83"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_198 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000198")
    batches[b_id_198] = {
        "id": b_id_198,
        "product_id": p_id_198,
        "batch_number": "BCH-MEDTRI-27",
        "expiry_date": date(2027, 7, 10),
        "purchase_cost": Decimal("38.83"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # AZITHRAL 100MG 15ML SYP
    p_id_199 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000198")
    products[p_id_199] = {
        "id": p_id_199,
        "code": "MED-AZITHRAL",
        "name": 'AZITHRAL 100MG 15ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("92.07"),
        "default_purchase_price": Decimal("73.66"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_199 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000199")
    batches[b_id_199] = {
        "id": b_id_199,
        "product_id": p_id_199,
        "batch_number": "BCH-MEDAZI-28",
        "expiry_date": date(2028, 8, 11),
        "purchase_cost": Decimal("73.66"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # AZITHRAL 200MG 30ML SYP
    p_id_200 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000199")
    products[p_id_200] = {
        "id": p_id_200,
        "code": "MED-AZITHRAL-1",
        "name": 'AZITHRAL 200MG 30ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("176.64"),
        "default_purchase_price": Decimal("141.31"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_200 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000200")
    batches[b_id_200] = {
        "id": b_id_200,
        "product_id": p_id_200,
        "batch_number": "BCH-MEDAZI-27",
        "expiry_date": date(2027, 9, 12),
        "purchase_cost": Decimal("141.31"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # BRICA-BM 60ML SYP
    p_id_201 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000200")
    products[p_id_201] = {
        "id": p_id_201,
        "code": "MED-BRICABM6",
        "name": 'BRICA-BM 60ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("111.69"),
        "default_purchase_price": Decimal("89.35"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_201 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000201")
    batches[b_id_201] = {
        "id": b_id_201,
        "product_id": p_id_201,
        "batch_number": "BCH-MEDBRI-28",
        "expiry_date": date(2028, 10, 13),
        "purchase_cost": Decimal("89.35"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # NIVARAK TEL 60ML
    p_id_202 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000201")
    products[p_id_202] = {
        "id": p_id_202,
        "code": "MED-NIVARAKT",
        "name": 'NIVARAK TEL 60ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("255.91"),
        "default_purchase_price": Decimal("204.73"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_202 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000202")
    batches[b_id_202] = {
        "id": b_id_202,
        "product_id": p_id_202,
        "batch_number": "BCH-MEDNIV-27",
        "expiry_date": date(2027, 11, 14),
        "purchase_cost": Decimal("204.73"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TRICORT INJ 40MG
    p_id_203 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000202")
    products[p_id_203] = {
        "id": p_id_203,
        "code": "MED-TRICORTI",
        "name": 'TRICORT INJ 40MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("187.85"),
        "default_purchase_price": Decimal("150.28"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_203 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000203")
    batches[b_id_203] = {
        "id": b_id_203,
        "product_id": p_id_203,
        "batch_number": "BCH-MEDTRI-28",
        "expiry_date": date(2028, 12, 15),
        "purchase_cost": Decimal("150.28"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB MEDOMOL 500 MG
    p_id_204 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000203")
    products[p_id_204] = {
        "id": p_id_204,
        "code": "MED-TABMEDOM",
        "name": 'TAB MEDOMOL 500 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("10.26"),
        "default_purchase_price": Decimal("8.21"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_204 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000204")
    batches[b_id_204] = {
        "id": b_id_204,
        "product_id": p_id_204,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 16),
        "purchase_cost": Decimal("8.21"),
        "quantity": 100,
        "is_active": True,
        "created_at": now,
    }

    # LOCET TAB
    p_id_205 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000204")
    products[p_id_205] = {
        "id": p_id_205,
        "code": "MED-LOCETTAB",
        "name": 'LOCET TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("60.70"),
        "default_purchase_price": Decimal("48.56"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_205 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000205")
    batches[b_id_205] = {
        "id": b_id_205,
        "product_id": p_id_205,
        "batch_number": "BCH-MEDLOC-28",
        "expiry_date": date(2028, 2, 17),
        "purchase_cost": Decimal("48.56"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # FLISTIN -X SYRP
    p_id_206 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000205")
    products[p_id_206] = {
        "id": p_id_206,
        "code": "MED-FLISTINX",
        "name": 'FLISTIN -X SYRP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("63.09"),
        "default_purchase_price": Decimal("50.47"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_206 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000206")
    batches[b_id_206] = {
        "id": b_id_206,
        "product_id": p_id_206,
        "batch_number": "BCH-MEDFLI-27",
        "expiry_date": date(2027, 3, 18),
        "purchase_cost": Decimal("50.47"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # Telmi 40 Tab
    p_id_207 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000206")
    products[p_id_207] = {
        "id": p_id_207,
        "code": "MED-TELMI40T",
        "name": 'Telmi 40 Tab',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("131.68"),
        "default_purchase_price": Decimal("105.34"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_207 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000207")
    batches[b_id_207] = {
        "id": b_id_207,
        "product_id": p_id_207,
        "batch_number": "BCH-MEDTEL-28",
        "expiry_date": date(2028, 4, 19),
        "purchase_cost": Decimal("105.34"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # CAP CANDITRAL 100MG
    p_id_208 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000207")
    products[p_id_208] = {
        "id": p_id_208,
        "code": "MED-CAPCANDI",
        "name": 'CAP CANDITRAL 100MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("239.21"),
        "default_purchase_price": Decimal("191.37"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_208 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000208")
    batches[b_id_208] = {
        "id": b_id_208,
        "product_id": p_id_208,
        "batch_number": "BCH-MEDCAP-27",
        "expiry_date": date(2027, 5, 20),
        "purchase_cost": Decimal("191.37"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # A TO Z GOLD CAP
    p_id_209 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000208")
    products[p_id_209] = {
        "id": p_id_209,
        "code": "MED-ATOZGOLD",
        "name": 'A TO Z GOLD CAP',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("347.25"),
        "default_purchase_price": Decimal("277.80"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_209 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000209")
    batches[b_id_209] = {
        "id": b_id_209,
        "product_id": p_id_209,
        "batch_number": "BCH-MEDATO-28",
        "expiry_date": date(2028, 6, 21),
        "purchase_cost": Decimal("277.80"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # DELYTE 25MG TAB
    p_id_210 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000209")
    products[p_id_210] = {
        "id": p_id_210,
        "code": "MED-DELYTE25",
        "name": 'DELYTE 25MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("39.09"),
        "default_purchase_price": Decimal("31.27"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_210 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000210")
    batches[b_id_210] = {
        "id": b_id_210,
        "product_id": p_id_210,
        "batch_number": "BCH-MEDDEL-27",
        "expiry_date": date(2027, 7, 22),
        "purchase_cost": Decimal("31.27"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # SPRIL-F TAB
    p_id_211 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000210")
    products[p_id_211] = {
        "id": p_id_211,
        "code": "MED-SPRILFTA",
        "name": 'SPRIL-F TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("91.94"),
        "default_purchase_price": Decimal("73.55"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_211 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000211")
    batches[b_id_211] = {
        "id": b_id_211,
        "product_id": p_id_211,
        "batch_number": "BCH-MEDSPR-28",
        "expiry_date": date(2028, 8, 23),
        "purchase_cost": Decimal("73.55"),
        "quantity": 63,
        "is_active": True,
        "created_at": now,
    }

    # GLYCOMET 500MG TAB
    p_id_212 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000211")
    products[p_id_212] = {
        "id": p_id_212,
        "code": "MED-GLYCOMET-1",
        "name": 'GLYCOMET 500MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("21.02"),
        "default_purchase_price": Decimal("16.82"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_212 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000212")
    batches[b_id_212] = {
        "id": b_id_212,
        "product_id": p_id_212,
        "batch_number": "BCH-MEDGLY-27",
        "expiry_date": date(2027, 9, 24),
        "purchase_cost": Decimal("16.82"),
        "quantity": 16,
        "is_active": True,
        "created_at": now,
    }

    # VALID ER 500
    p_id_213 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000212")
    products[p_id_213] = {
        "id": p_id_213,
        "code": "MED-VALIDER5",
        "name": 'VALID ER 500',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("153.60"),
        "default_purchase_price": Decimal("122.88"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_213 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000213")
    batches[b_id_213] = {
        "id": b_id_213,
        "product_id": p_id_213,
        "batch_number": "BCH-MEDVAL-28",
        "expiry_date": date(2028, 10, 25),
        "purchase_cost": Decimal("122.88"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # CALCIROL SACHET
    p_id_214 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000213")
    products[p_id_214] = {
        "id": p_id_214,
        "code": "MED-CALCIROL",
        "name": 'CALCIROL SACHET',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("59.33"),
        "default_purchase_price": Decimal("47.46"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_214 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000214")
    batches[b_id_214] = {
        "id": b_id_214,
        "product_id": p_id_214,
        "batch_number": "BCH-MEDCAL-27",
        "expiry_date": date(2027, 11, 26),
        "purchase_cost": Decimal("47.46"),
        "quantity": 120,
        "is_active": True,
        "created_at": now,
    }

    # TAZLOC AM
    p_id_215 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000214")
    products[p_id_215] = {
        "id": p_id_215,
        "code": "MED-TAZLOCAM",
        "name": 'TAZLOC AM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("262.05"),
        "default_purchase_price": Decimal("209.64"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_215 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000215")
    batches[b_id_215] = {
        "id": b_id_215,
        "product_id": p_id_215,
        "batch_number": "BCH-MEDTAZ-28",
        "expiry_date": date(2028, 12, 27),
        "purchase_cost": Decimal("209.64"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # CODOPAR TAB
    p_id_216 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000215")
    products[p_id_216] = {
        "id": p_id_216,
        "code": "MED-CODOPART",
        "name": 'CODOPAR TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("65.86"),
        "default_purchase_price": Decimal("52.69"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_216 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000216")
    batches[b_id_216] = {
        "id": b_id_216,
        "product_id": p_id_216,
        "batch_number": "BCH-MEDCOD-27",
        "expiry_date": date(2027, 1, 1),
        "purchase_cost": Decimal("52.69"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # KLOZEP 0.5 TAB
    p_id_217 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000216")
    products[p_id_217] = {
        "id": p_id_217,
        "code": "MED-KLOZEP05",
        "name": 'KLOZEP 0.5 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("90.99"),
        "default_purchase_price": Decimal("72.79"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_217 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000217")
    batches[b_id_217] = {
        "id": b_id_217,
        "product_id": p_id_217,
        "batch_number": "BCH-MEDKLO-28",
        "expiry_date": date(2028, 2, 2),
        "purchase_cost": Decimal("72.79"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # MEGANEURON-TAB
    p_id_218 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000217")
    products[p_id_218] = {
        "id": p_id_218,
        "code": "MED-MEGANEUR",
        "name": 'MEGANEURON-TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("152.60"),
        "default_purchase_price": Decimal("122.08"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_218 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000218")
    batches[b_id_218] = {
        "id": b_id_218,
        "product_id": p_id_218,
        "batch_number": "BCH-MEDMEG-27",
        "expiry_date": date(2027, 3, 3),
        "purchase_cost": Decimal("122.08"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # ACILOC 300 MG TAB
    p_id_219 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000218")
    products[p_id_219] = {
        "id": p_id_219,
        "code": "MED-ACILOC30",
        "name": 'ACILOC 300 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("59.09"),
        "default_purchase_price": Decimal("47.27"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_219 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000219")
    batches[b_id_219] = {
        "id": b_id_219,
        "product_id": p_id_219,
        "batch_number": "BCH-MEDACI-28",
        "expiry_date": date(2028, 4, 4),
        "purchase_cost": Decimal("47.27"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # NAPROSYN 250 MG TAB
    p_id_220 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000219")
    products[p_id_220] = {
        "id": p_id_220,
        "code": "MED-NAPROSYN",
        "name": 'NAPROSYN 250 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("176.76"),
        "default_purchase_price": Decimal("141.41"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_220 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000220")
    batches[b_id_220] = {
        "id": b_id_220,
        "product_id": p_id_220,
        "batch_number": "BCH-MEDNAP-27",
        "expiry_date": date(2027, 5, 5),
        "purchase_cost": Decimal("141.41"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # NAPROSYN 500 MG TAB
    p_id_221 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000220")
    products[p_id_221] = {
        "id": p_id_221,
        "code": "MED-NAPROSYN-1",
        "name": 'NAPROSYN 500 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("240.84"),
        "default_purchase_price": Decimal("192.67"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_221 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000221")
    batches[b_id_221] = {
        "id": b_id_221,
        "product_id": p_id_221,
        "batch_number": "BCH-MEDNAP-28",
        "expiry_date": date(2028, 6, 6),
        "purchase_cost": Decimal("192.67"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # GLYCOMET GP1 FORTE TAB
    p_id_222 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000221")
    products[p_id_222] = {
        "id": p_id_222,
        "code": "MED-GLYCOMET-2",
        "name": 'GLYCOMET GP1 FORTE TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("171.01"),
        "default_purchase_price": Decimal("136.81"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_222 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000222")
    batches[b_id_222] = {
        "id": b_id_222,
        "product_id": p_id_222,
        "batch_number": "BCH-MEDGLY-27",
        "expiry_date": date(2027, 7, 7),
        "purchase_cost": Decimal("136.81"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # GLYCOMET 500 SR TAB
    p_id_223 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000222")
    products[p_id_223] = {
        "id": p_id_223,
        "code": "MED-GLYCOMET-3",
        "name": 'GLYCOMET 500 SR TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("68.41"),
        "default_purchase_price": Decimal("54.73"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_223 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000223")
    batches[b_id_223] = {
        "id": b_id_223,
        "product_id": p_id_223,
        "batch_number": "BCH-MEDGLY-28",
        "expiry_date": date(2028, 8, 8),
        "purchase_cost": Decimal("54.73"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # MOREASE SR TAB
    p_id_224 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000223")
    products[p_id_224] = {
        "id": p_id_224,
        "code": "MED-MOREASES",
        "name": 'MOREASE SR TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("324.38"),
        "default_purchase_price": Decimal("259.50"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_224 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000224")
    batches[b_id_224] = {
        "id": b_id_224,
        "product_id": p_id_224,
        "batch_number": "BCH-MEDMOR-27",
        "expiry_date": date(2027, 9, 9),
        "purchase_cost": Decimal("259.50"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # AZITHRAL 500 MG TAB
    p_id_225 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000224")
    products[p_id_225] = {
        "id": p_id_225,
        "code": "MED-AZITHRAL-2",
        "name": 'AZITHRAL 500 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("142.41"),
        "default_purchase_price": Decimal("113.93"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_225 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000225")
    batches[b_id_225] = {
        "id": b_id_225,
        "product_id": p_id_225,
        "batch_number": "BCH-MEDAZI-28",
        "expiry_date": date(2028, 10, 10),
        "purchase_cost": Decimal("113.93"),
        "quantity": 48,
        "is_active": True,
        "created_at": now,
    }

    # CLOPID TAB
    p_id_226 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000225")
    products[p_id_226] = {
        "id": p_id_226,
        "code": "MED-CLOPIDTA",
        "name": 'CLOPID TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("170.11"),
        "default_purchase_price": Decimal("136.09"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_226 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000226")
    batches[b_id_226] = {
        "id": b_id_226,
        "product_id": p_id_226,
        "batch_number": "BCH-MEDCLO-27",
        "expiry_date": date(2027, 11, 11),
        "purchase_cost": Decimal("136.09"),
        "quantity": 22,
        "is_active": True,
        "created_at": now,
    }

    # TELMA H TAB
    p_id_227 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000226")
    products[p_id_227] = {
        "id": p_id_227,
        "code": "MED-TELMAHTA",
        "name": 'TELMA H TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("541.79"),
        "default_purchase_price": Decimal("433.43"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_227 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000227")
    batches[b_id_227] = {
        "id": b_id_227,
        "product_id": p_id_227,
        "batch_number": "BCH-MEDTEL-28",
        "expiry_date": date(2028, 12, 12),
        "purchase_cost": Decimal("433.43"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # ACECLO SR TAB
    p_id_228 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000227")
    products[p_id_228] = {
        "id": p_id_228,
        "code": "MED-ACECLOSR",
        "name": 'ACECLO SR TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("138.52"),
        "default_purchase_price": Decimal("110.82"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_228 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000228")
    batches[b_id_228] = {
        "id": b_id_228,
        "product_id": p_id_228,
        "batch_number": "BCH-MEDACE-27",
        "expiry_date": date(2027, 1, 13),
        "purchase_cost": Decimal("110.82"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ACILOC 150MG TAB
    p_id_229 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000228")
    products[p_id_229] = {
        "id": p_id_229,
        "code": "MED-ACILOC15",
        "name": 'ACILOC 150MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("43.21"),
        "default_purchase_price": Decimal("34.57"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_229 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000229")
    batches[b_id_229] = {
        "id": b_id_229,
        "product_id": p_id_229,
        "batch_number": "BCH-MEDACI-28",
        "expiry_date": date(2028, 2, 14),
        "purchase_cost": Decimal("34.57"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ACITOP 40 MG TAB
    p_id_230 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000229")
    products[p_id_230] = {
        "id": p_id_230,
        "code": "MED-ACITOP40",
        "name": 'ACITOP 40 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("105.46"),
        "default_purchase_price": Decimal("84.37"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_230 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000230")
    batches[b_id_230] = {
        "id": b_id_230,
        "product_id": p_id_230,
        "batch_number": "BCH-MEDACI-27",
        "expiry_date": date(2027, 3, 15),
        "purchase_cost": Decimal("84.37"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ALPINE-L TAB
    p_id_231 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000230")
    products[p_id_231] = {
        "id": p_id_231,
        "code": "MED-ALPINELT",
        "name": 'ALPINE-L TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("134.18"),
        "default_purchase_price": Decimal("107.34"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_231 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000231")
    batches[b_id_231] = {
        "id": b_id_231,
        "product_id": p_id_231,
        "batch_number": "BCH-MEDALP-28",
        "expiry_date": date(2028, 4, 16),
        "purchase_cost": Decimal("107.34"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ALSARTAN AM TAB
    p_id_232 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000231")
    products[p_id_232] = {
        "id": p_id_232,
        "code": "MED-ALSARTAN",
        "name": 'ALSARTAN AM TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("158.62"),
        "default_purchase_price": Decimal("126.90"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_232 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000232")
    batches[b_id_232] = {
        "id": b_id_232,
        "product_id": p_id_232,
        "batch_number": "BCH-MEDALS-27",
        "expiry_date": date(2027, 5, 17),
        "purchase_cost": Decimal("126.90"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # AMBRODIL 100 ML SYP
    p_id_233 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000232")
    products[p_id_233] = {
        "id": p_id_233,
        "code": "MED-AMBRODIL",
        "name": 'AMBRODIL 100 ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("125.75"),
        "default_purchase_price": Decimal("100.60"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_233 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000233")
    batches[b_id_233] = {
        "id": b_id_233,
        "product_id": p_id_233,
        "batch_number": "BCH-MEDAMB-28",
        "expiry_date": date(2028, 6, 18),
        "purchase_cost": Decimal("100.60"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # AMFAST L TAB
    p_id_234 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000233")
    products[p_id_234] = {
        "id": p_id_234,
        "code": "MED-AMFASTLT",
        "name": 'AMFAST L TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("132.97"),
        "default_purchase_price": Decimal("106.38"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_234 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000234")
    batches[b_id_234] = {
        "id": b_id_234,
        "product_id": p_id_234,
        "batch_number": "BCH-MEDAMF-27",
        "expiry_date": date(2027, 7, 19),
        "purchase_cost": Decimal("106.38"),
        "quantity": 45,
        "is_active": True,
        "created_at": now,
    }

    # AMFAST AT TAB
    p_id_235 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000234")
    products[p_id_235] = {
        "id": p_id_235,
        "code": "MED-AMFASTAT",
        "name": 'AMFAST AT TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("114.71"),
        "default_purchase_price": Decimal("91.77"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_235 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000235")
    batches[b_id_235] = {
        "id": b_id_235,
        "product_id": p_id_235,
        "batch_number": "BCH-MEDAMF-28",
        "expiry_date": date(2028, 8, 20),
        "purchase_cost": Decimal("91.77"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # AMILAX TAB
    p_id_236 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000235")
    products[p_id_236] = {
        "id": p_id_236,
        "code": "MED-AMILAXTA",
        "name": 'AMILAX TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("48.48"),
        "default_purchase_price": Decimal("38.78"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_236 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000236")
    batches[b_id_236] = {
        "id": b_id_236,
        "product_id": p_id_236,
        "batch_number": "BCH-MEDAMI-27",
        "expiry_date": date(2027, 9, 21),
        "purchase_cost": Decimal("38.78"),
        "quantity": 30,
        "is_active": True,
        "created_at": now,
    }

    # AMLOD AT TAB
    p_id_237 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000236")
    products[p_id_237] = {
        "id": p_id_237,
        "code": "MED-AMLODATT",
        "name": 'AMLOD AT TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("92.09"),
        "default_purchase_price": Decimal("73.67"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_237 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000237")
    batches[b_id_237] = {
        "id": b_id_237,
        "product_id": p_id_237,
        "batch_number": "BCH-MEDAML-28",
        "expiry_date": date(2028, 10, 22),
        "purchase_cost": Decimal("73.67"),
        "quantity": 75,
        "is_active": True,
        "created_at": now,
    }

    # ANTI THYROX 10 MG TAB
    p_id_238 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000237")
    products[p_id_238] = {
        "id": p_id_238,
        "code": "MED-ANTITHYR",
        "name": 'ANTI THYROX 10 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("803.39"),
        "default_purchase_price": Decimal("642.71"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_238 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000238")
    batches[b_id_238] = {
        "id": b_id_238,
        "product_id": p_id_238,
        "batch_number": "BCH-MEDANT-27",
        "expiry_date": date(2027, 11, 23),
        "purchase_cost": Decimal("642.71"),
        "quantity": 1,
        "is_active": True,
        "created_at": now,
    }

    # ANTI THYROX 5 MG TAB
    p_id_239 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000238")
    products[p_id_239] = {
        "id": p_id_239,
        "code": "MED-ANTITHYR-1",
        "name": 'ANTI THYROX 5 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("412.31"),
        "default_purchase_price": Decimal("329.85"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_239 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000239")
    batches[b_id_239] = {
        "id": b_id_239,
        "product_id": p_id_239,
        "batch_number": "BCH-MEDANT-28",
        "expiry_date": date(2028, 12, 24),
        "purchase_cost": Decimal("329.85"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # APTICARE 200 ML SYP
    p_id_240 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000239")
    products[p_id_240] = {
        "id": p_id_240,
        "code": "MED-APTICARE",
        "name": 'APTICARE 200 ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("185.34"),
        "default_purchase_price": Decimal("148.27"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_240 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000240")
    batches[b_id_240] = {
        "id": b_id_240,
        "product_id": p_id_240,
        "batch_number": "BCH-MEDAPT-27",
        "expiry_date": date(2027, 1, 25),
        "purchase_cost": Decimal("148.27"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # ARBITEL 80 MG TAB
    p_id_241 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000240")
    products[p_id_241] = {
        "id": p_id_241,
        "code": "MED-ARBITEL8",
        "name": 'ARBITEL 80 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("194.15"),
        "default_purchase_price": Decimal("155.32"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_241 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000241")
    batches[b_id_241] = {
        "id": b_id_241,
        "product_id": p_id_241,
        "batch_number": "BCH-MEDARB-28",
        "expiry_date": date(2028, 2, 26),
        "purchase_cost": Decimal("155.32"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # ARBITEL AM TAB
    p_id_242 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000241")
    products[p_id_242] = {
        "id": p_id_242,
        "code": "MED-ARBITELA",
        "name": 'ARBITEL AM TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("423.73"),
        "default_purchase_price": Decimal("338.98"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_242 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000242")
    batches[b_id_242] = {
        "id": b_id_242,
        "product_id": p_id_242,
        "batch_number": "BCH-MEDARB-27",
        "expiry_date": date(2027, 3, 27),
        "purchase_cost": Decimal("338.98"),
        "quantity": 50,
        "is_active": True,
        "created_at": now,
    }

    # ARISTOZYME 200 ML SYP
    p_id_243 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000242")
    products[p_id_243] = {
        "id": p_id_243,
        "code": "MED-ARISTOZY",
        "name": 'ARISTOZYME 200 ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("232.27"),
        "default_purchase_price": Decimal("185.82"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_243 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000243")
    batches[b_id_243] = {
        "id": b_id_243,
        "product_id": p_id_243,
        "batch_number": "BCH-MEDARI-28",
        "expiry_date": date(2028, 4, 1),
        "purchase_cost": Decimal("185.82"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ATCHOL 10 MG TAB 1X10
    p_id_244 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000243")
    products[p_id_244] = {
        "id": p_id_244,
        "code": "MED-ATCHOL10",
        "name": 'ATCHOL 10 MG TAB 1X10',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("52.26"),
        "default_purchase_price": Decimal("41.81"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_244 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000244")
    batches[b_id_244] = {
        "id": b_id_244,
        "product_id": p_id_244,
        "batch_number": "BCH-MEDATC-27",
        "expiry_date": date(2027, 5, 2),
        "purchase_cost": Decimal("41.81"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ATORTIN 10 MG TAB
    p_id_245 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000244")
    products[p_id_245] = {
        "id": p_id_245,
        "code": "MED-ATORTIN1",
        "name": 'ATORTIN 10 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("108.39"),
        "default_purchase_price": Decimal("86.71"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_245 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000245")
    batches[b_id_245] = {
        "id": b_id_245,
        "product_id": p_id_245,
        "batch_number": "BCH-MEDATO-28",
        "expiry_date": date(2028, 6, 3),
        "purchase_cost": Decimal("86.71"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # ATORTIN 20 MG TAB
    p_id_246 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000245")
    products[p_id_246] = {
        "id": p_id_246,
        "code": "MED-ATORTIN2",
        "name": 'ATORTIN 20 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("208.15"),
        "default_purchase_price": Decimal("166.52"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_246 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000246")
    batches[b_id_246] = {
        "id": b_id_246,
        "product_id": p_id_246,
        "batch_number": "BCH-MEDATO-27",
        "expiry_date": date(2027, 7, 4),
        "purchase_cost": Decimal("166.52"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # BUDAMATE 200 MG ROTOCAP
    p_id_247 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000246")
    products[p_id_247] = {
        "id": p_id_247,
        "code": "MED-BUDAMATE",
        "name": 'BUDAMATE 200 MG ROTOCAP',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("318.38"),
        "default_purchase_price": Decimal("254.70"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_247 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000247")
    batches[b_id_247] = {
        "id": b_id_247,
        "product_id": p_id_247,
        "batch_number": "BCH-MEDBUD-28",
        "expiry_date": date(2028, 8, 5),
        "purchase_cost": Decimal("254.70"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # BUDAMATE 400 MG ROTOCAP
    p_id_248 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000247")
    products[p_id_248] = {
        "id": p_id_248,
        "code": "MED-BUDAMATE-1",
        "name": 'BUDAMATE 400 MG ROTOCAP',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("386.94"),
        "default_purchase_price": Decimal("309.55"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_248 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000248")
    batches[b_id_248] = {
        "id": b_id_248,
        "product_id": p_id_248,
        "batch_number": "BCH-MEDBUD-27",
        "expiry_date": date(2027, 9, 6),
        "purchase_cost": Decimal("309.55"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # CANDID 50 GRM POWDER
    p_id_249 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000248")
    products[p_id_249] = {
        "id": p_id_249,
        "code": "MED-CANDID50",
        "name": 'CANDID 50 GRM POWDER',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("125.05"),
        "default_purchase_price": Decimal("100.04"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_249 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000249")
    batches[b_id_249] = {
        "id": b_id_249,
        "product_id": p_id_249,
        "batch_number": "BCH-MEDCAN-28",
        "expiry_date": date(2028, 10, 7),
        "purchase_cost": Decimal("100.04"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # CANDID POWDER 100 GRM
    p_id_250 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000249")
    products[p_id_250] = {
        "id": p_id_250,
        "code": "MED-CANDIDPO",
        "name": 'CANDID POWDER 100 GRM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("111.89"),
        "default_purchase_price": Decimal("89.51"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_250 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000250")
    batches[b_id_250] = {
        "id": b_id_250,
        "product_id": p_id_250,
        "batch_number": "BCH-MEDCAN-27",
        "expiry_date": date(2027, 11, 8),
        "purchase_cost": Decimal("89.51"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # CARVIDON MR TAB 1X15
    p_id_251 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000250")
    products[p_id_251] = {
        "id": p_id_251,
        "code": "MED-CARVIDON",
        "name": 'CARVIDON MR TAB 1X15',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("517.94"),
        "default_purchase_price": Decimal("414.35"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_251 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000251")
    batches[b_id_251] = {
        "id": b_id_251,
        "product_id": p_id_251,
        "batch_number": "BCH-MEDCAR-28",
        "expiry_date": date(2028, 12, 9),
        "purchase_cost": Decimal("414.35"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # CEFADROX 500 MG TAB
    p_id_252 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000251")
    products[p_id_252] = {
        "id": p_id_252,
        "code": "MED-CEFADROX",
        "name": 'CEFADROX 500 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("119.53"),
        "default_purchase_price": Decimal("95.62"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_252 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000252")
    batches[b_id_252] = {
        "id": b_id_252,
        "product_id": p_id_252,
        "batch_number": "BCH-MEDCEF-27",
        "expiry_date": date(2027, 1, 10),
        "purchase_cost": Decimal("95.62"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # CLAVAM 375 MG TAB
    p_id_253 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000252")
    products[p_id_253] = {
        "id": p_id_253,
        "code": "MED-CLAVAM37",
        "name": 'CLAVAM 375 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("238.45"),
        "default_purchase_price": Decimal("190.76"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_253 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000253")
    batches[b_id_253] = {
        "id": b_id_253,
        "product_id": p_id_253,
        "batch_number": "BCH-MEDCLA-28",
        "expiry_date": date(2028, 2, 11),
        "purchase_cost": Decimal("190.76"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # CLONAZ 0.5 MG TAB
    p_id_254 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000253")
    products[p_id_254] = {
        "id": p_id_254,
        "code": "MED-CLONAZ05",
        "name": 'CLONAZ 0.5 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("81.17"),
        "default_purchase_price": Decimal("64.94"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_254 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000254")
    batches[b_id_254] = {
        "id": b_id_254,
        "product_id": p_id_254,
        "batch_number": "BCH-MEDCLO-27",
        "expiry_date": date(2027, 3, 12),
        "purchase_cost": Decimal("64.94"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # DECOLD TAB
    p_id_255 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000254")
    products[p_id_255] = {
        "id": p_id_255,
        "code": "MED-DECOLDTA",
        "name": 'DECOLD TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("23.81"),
        "default_purchase_price": Decimal("19.05"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_255 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000255")
    batches[b_id_255] = {
        "id": b_id_255,
        "product_id": p_id_255,
        "batch_number": "BCH-MEDDEC-28",
        "expiry_date": date(2028, 4, 13),
        "purchase_cost": Decimal("19.05"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # DELYTE 10 MG TAB
    p_id_256 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000255")
    products[p_id_256] = {
        "id": p_id_256,
        "code": "MED-DELYTE10",
        "name": 'DELYTE 10 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("24.70"),
        "default_purchase_price": Decimal("19.76"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_256 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000256")
    batches[b_id_256] = {
        "id": b_id_256,
        "product_id": p_id_256,
        "batch_number": "BCH-MEDDEL-27",
        "expiry_date": date(2027, 5, 14),
        "purchase_cost": Decimal("19.76"),
        "quantity": 33,
        "is_active": True,
        "created_at": now,
    }

    # DIAPRIDE M1
    p_id_257 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000256")
    products[p_id_257] = {
        "id": p_id_257,
        "code": "MED-DIAPRIDE",
        "name": 'DIAPRIDE M1',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("252.07"),
        "default_purchase_price": Decimal("201.66"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_257 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000257")
    batches[b_id_257] = {
        "id": b_id_257,
        "product_id": p_id_257,
        "batch_number": "BCH-MEDDIA-28",
        "expiry_date": date(2028, 6, 15),
        "purchase_cost": Decimal("201.66"),
        "quantity": 40,
        "is_active": True,
        "created_at": now,
    }

    # DIAPRIDE M1 FORTE
    p_id_258 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000257")
    products[p_id_258] = {
        "id": p_id_258,
        "code": "MED-DIAPRIDE-1",
        "name": 'DIAPRIDE M1 FORTE',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("225.04"),
        "default_purchase_price": Decimal("180.03"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_258 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000258")
    batches[b_id_258] = {
        "id": b_id_258,
        "product_id": p_id_258,
        "batch_number": "BCH-MEDDIA-27",
        "expiry_date": date(2027, 7, 16),
        "purchase_cost": Decimal("180.03"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # DIAPRIDE M3 FORTE TAB
    p_id_259 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000258")
    products[p_id_259] = {
        "id": p_id_259,
        "code": "MED-DIAPRIDE-2",
        "name": 'DIAPRIDE M3 FORTE TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("305.79"),
        "default_purchase_price": Decimal("244.63"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_259 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000259")
    batches[b_id_259] = {
        "id": b_id_259,
        "product_id": p_id_259,
        "batch_number": "BCH-MEDDIA-28",
        "expiry_date": date(2028, 8, 17),
        "purchase_cost": Decimal("244.63"),
        "quantity": 69,
        "is_active": True,
        "created_at": now,
    }

    # DICLOTAL SR 100 MG
    p_id_260 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000259")
    products[p_id_260] = {
        "id": p_id_260,
        "code": "MED-DICLOTAL",
        "name": 'DICLOTAL SR 100 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("30.26"),
        "default_purchase_price": Decimal("24.21"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_260 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000260")
    batches[b_id_260] = {
        "id": b_id_260,
        "product_id": p_id_260,
        "batch_number": "BCH-MEDDIC-27",
        "expiry_date": date(2027, 9, 18),
        "purchase_cost": Decimal("24.21"),
        "quantity": 72,
        "is_active": True,
        "created_at": now,
    }

    # EMPAZ 25 MG TAB
    p_id_261 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000260")
    products[p_id_261] = {
        "id": p_id_261,
        "code": "MED-EMPAZ25M",
        "name": 'EMPAZ 25 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("308.12"),
        "default_purchase_price": Decimal("246.50"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_261 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000261")
    batches[b_id_261] = {
        "id": b_id_261,
        "product_id": p_id_261,
        "batch_number": "BCH-MEDEMP-28",
        "expiry_date": date(2028, 10, 19),
        "purchase_cost": Decimal("246.50"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # EPTUS 25 MG TAB
    p_id_262 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000261")
    products[p_id_262] = {
        "id": p_id_262,
        "code": "MED-EPTUS25M",
        "name": 'EPTUS 25 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("1088.30"),
        "default_purchase_price": Decimal("870.64"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_262 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000262")
    batches[b_id_262] = {
        "id": b_id_262,
        "product_id": p_id_262,
        "batch_number": "BCH-MEDEPT-27",
        "expiry_date": date(2027, 11, 20),
        "purchase_cost": Decimal("870.64"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # ESOZOL 40 MG TAB
    p_id_263 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000262")
    products[p_id_263] = {
        "id": p_id_263,
        "code": "MED-ESOZOL40",
        "name": 'ESOZOL 40 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("99.83"),
        "default_purchase_price": Decimal("79.86"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_263 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000263")
    batches[b_id_263] = {
        "id": b_id_263,
        "product_id": p_id_263,
        "batch_number": "BCH-MEDESO-28",
        "expiry_date": date(2028, 12, 21),
        "purchase_cost": Decimal("79.86"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # EVA 400 MG CAP
    p_id_264 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000263")
    products[p_id_264] = {
        "id": p_id_264,
        "code": "MED-EVA400MG",
        "name": 'EVA 400 MG CAP',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("66.84"),
        "default_purchase_price": Decimal("53.47"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_264 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000264")
    batches[b_id_264] = {
        "id": b_id_264,
        "product_id": p_id_264,
        "batch_number": "BCH-MEDEVA-27",
        "expiry_date": date(2027, 1, 22),
        "purchase_cost": Decimal("53.47"),
        "quantity": 40,
        "is_active": True,
        "created_at": now,
    }

    # F-STAT 40
    p_id_265 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000264")
    products[p_id_265] = {
        "id": p_id_265,
        "code": "MED-FSTAT40",
        "name": 'F-STAT 40',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("202.21"),
        "default_purchase_price": Decimal("161.77"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_265 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000265")
    batches[b_id_265] = {
        "id": b_id_265,
        "product_id": p_id_265,
        "batch_number": "BCH-MEDFST-28",
        "expiry_date": date(2028, 2, 23),
        "purchase_cost": Decimal("161.77"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # FLEXON SUSP 60 ML
    p_id_266 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000265")
    products[p_id_266] = {
        "id": p_id_266,
        "code": "MED-FLEXONSU",
        "name": 'FLEXON SUSP 60 ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("29.30"),
        "default_purchase_price": Decimal("23.44"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_266 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000266")
    batches[b_id_266] = {
        "id": b_id_266,
        "product_id": p_id_266,
        "batch_number": "BCH-MEDFLE-27",
        "expiry_date": date(2027, 3, 24),
        "purchase_cost": Decimal("23.44"),
        "quantity": 36,
        "is_active": True,
        "created_at": now,
    }

    # FORCEF 500 MG
    p_id_267 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000266")
    products[p_id_267] = {
        "id": p_id_267,
        "code": "MED-FORCEF50",
        "name": 'FORCEF 500 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("719.60"),
        "default_purchase_price": Decimal("575.68"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_267 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000267")
    batches[b_id_267] = {
        "id": b_id_267,
        "product_id": p_id_267,
        "batch_number": "BCH-MEDFOR-28",
        "expiry_date": date(2028, 4, 25),
        "purchase_cost": Decimal("575.68"),
        "quantity": 7,
        "is_active": True,
        "created_at": now,
    }

    # FORMIN G1 TAB
    p_id_268 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000267")
    products[p_id_268] = {
        "id": p_id_268,
        "code": "MED-FORMING1",
        "name": 'FORMIN G1 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("112.45"),
        "default_purchase_price": Decimal("89.96"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_268 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000268")
    batches[b_id_268] = {
        "id": b_id_268,
        "product_id": p_id_268,
        "batch_number": "BCH-MEDFOR-27",
        "expiry_date": date(2027, 5, 26),
        "purchase_cost": Decimal("89.96"),
        "quantity": 19,
        "is_active": True,
        "created_at": now,
    }

    # FORMIN G2 TAB
    p_id_269 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000268")
    products[p_id_269] = {
        "id": p_id_269,
        "code": "MED-FORMING2",
        "name": 'FORMIN G2 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("163.05"),
        "default_purchase_price": Decimal("130.44"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_269 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000269")
    batches[b_id_269] = {
        "id": b_id_269,
        "product_id": p_id_269,
        "batch_number": "BCH-MEDFOR-28",
        "expiry_date": date(2028, 6, 27),
        "purchase_cost": Decimal("130.44"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # FOSSIL 70 MG TAB 1X14
    p_id_270 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000269")
    products[p_id_270] = {
        "id": p_id_270,
        "code": "MED-FOSSIL70",
        "name": 'FOSSIL 70 MG TAB 1X14',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("228.94"),
        "default_purchase_price": Decimal("183.15"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_270 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000270")
    batches[b_id_270] = {
        "id": b_id_270,
        "product_id": p_id_270,
        "batch_number": "BCH-MEDFOS-27",
        "expiry_date": date(2027, 7, 1),
        "purchase_cost": Decimal("183.15"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # FRUSIX 20 MG TAB 1X30
    p_id_271 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000270")
    products[p_id_271] = {
        "id": p_id_271,
        "code": "MED-FRUSIX20",
        "name": 'FRUSIX 20 MG TAB 1X30',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("46.42"),
        "default_purchase_price": Decimal("37.14"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_271 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000271")
    batches[b_id_271] = {
        "id": b_id_271,
        "product_id": p_id_271,
        "batch_number": "BCH-MEDFRU-28",
        "expiry_date": date(2028, 8, 2),
        "purchase_cost": Decimal("37.14"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # GLIMIPREX MF 1/500 MG TAB
    p_id_272 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000271")
    products[p_id_272] = {
        "id": p_id_272,
        "code": "MED-GLIMIPRE",
        "name": 'GLIMIPREX MF 1/500 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("124.88"),
        "default_purchase_price": Decimal("99.90"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_272 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000272")
    batches[b_id_272] = {
        "id": b_id_272,
        "product_id": p_id_272,
        "batch_number": "BCH-MEDGLI-27",
        "expiry_date": date(2027, 9, 3),
        "purchase_cost": Decimal("99.90"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # GLIMIPREX MF 2/500 MG TAB 1X10
    p_id_273 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000272")
    products[p_id_273] = {
        "id": p_id_273,
        "code": "MED-GLIMIPRE-1",
        "name": 'GLIMIPREX MF 2/500 MG TAB 1X10',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("170.35"),
        "default_purchase_price": Decimal("136.28"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_273 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000273")
    batches[b_id_273] = {
        "id": b_id_273,
        "product_id": p_id_273,
        "batch_number": "BCH-MEDGLI-28",
        "expiry_date": date(2028, 10, 4),
        "purchase_cost": Decimal("136.28"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # GLIMIPREX MF FORTE 2 1X10
    p_id_274 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000273")
    products[p_id_274] = {
        "id": p_id_274,
        "code": "MED-GLIMIPRE-2",
        "name": 'GLIMIPREX MF FORTE 2 1X10',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("173.46"),
        "default_purchase_price": Decimal("138.77"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_274 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000274")
    batches[b_id_274] = {
        "id": b_id_274,
        "product_id": p_id_274,
        "batch_number": "BCH-MEDGLI-27",
        "expiry_date": date(2027, 11, 5),
        "purchase_cost": Decimal("138.77"),
        "quantity": 4,
        "is_active": True,
        "created_at": now,
    }

    # GLUCONORM G2 TAB
    p_id_275 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000274")
    products[p_id_275] = {
        "id": p_id_275,
        "code": "MED-GLUCONOR",
        "name": 'GLUCONORM G2 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("587.29"),
        "default_purchase_price": Decimal("469.83"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_275 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000275")
    batches[b_id_275] = {
        "id": b_id_275,
        "product_id": p_id_275,
        "batch_number": "BCH-MEDGLU-28",
        "expiry_date": date(2028, 12, 6),
        "purchase_cost": Decimal("469.83"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # GLURIDE 2 MG TAB
    p_id_276 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000275")
    products[p_id_276] = {
        "id": p_id_276,
        "code": "MED-GLURIDE2",
        "name": 'GLURIDE 2 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("88.25"),
        "default_purchase_price": Decimal("70.60"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_276 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000276")
    batches[b_id_276] = {
        "id": b_id_276,
        "product_id": p_id_276,
        "batch_number": "BCH-MEDGLU-27",
        "expiry_date": date(2027, 1, 7),
        "purchase_cost": Decimal("70.60"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # GLYCOMET 850 MG TAB
    p_id_277 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000276")
    products[p_id_277] = {
        "id": p_id_277,
        "code": "MED-GLYCOMET-4",
        "name": 'GLYCOMET 850 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("81.36"),
        "default_purchase_price": Decimal("65.09"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_277 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000277")
    batches[b_id_277] = {
        "id": b_id_277,
        "product_id": p_id_277,
        "batch_number": "BCH-MEDGLY-28",
        "expiry_date": date(2028, 2, 8),
        "purchase_cost": Decimal("65.09"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # GLYCOMET 850 SR TAB
    p_id_278 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000277")
    products[p_id_278] = {
        "id": p_id_278,
        "code": "MED-GLYCOMET-5",
        "name": 'GLYCOMET 850 SR TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("94.25"),
        "default_purchase_price": Decimal("75.40"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_278 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000278")
    batches[b_id_278] = {
        "id": b_id_278,
        "product_id": p_id_278,
        "batch_number": "BCH-MEDGLY-27",
        "expiry_date": date(2027, 3, 9),
        "purchase_cost": Decimal("75.40"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # GP1 MG TAB
    p_id_279 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000278")
    products[p_id_279] = {
        "id": p_id_279,
        "code": "MED-GP1MGTAB",
        "name": 'GP1 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("54.92"),
        "default_purchase_price": Decimal("43.94"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_279 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000279")
    batches[b_id_279] = {
        "id": b_id_279,
        "product_id": p_id_279,
        "batch_number": "BCH-MEDGP1-28",
        "expiry_date": date(2028, 4, 10),
        "purchase_cost": Decimal("43.94"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # HATRIC 30ML SYP
    p_id_280 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000279")
    products[p_id_280] = {
        "id": p_id_280,
        "code": "MED-HATRIC30",
        "name": 'HATRIC 30ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("85.35"),
        "default_purchase_price": Decimal("68.28"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_280 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000280")
    batches[b_id_280] = {
        "id": b_id_280,
        "product_id": p_id_280,
        "batch_number": "BCH-MEDHAT-27",
        "expiry_date": date(2027, 5, 11),
        "purchase_cost": Decimal("68.28"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # HATRIC TAB
    p_id_281 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000280")
    products[p_id_281] = {
        "id": p_id_281,
        "code": "MED-HATRICTA",
        "name": 'HATRIC TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("84.84"),
        "default_purchase_price": Decimal("67.87"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_281 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000281")
    batches[b_id_281] = {
        "id": b_id_281,
        "product_id": p_id_281,
        "batch_number": "BCH-MEDHAT-28",
        "expiry_date": date(2028, 6, 12),
        "purchase_cost": Decimal("67.87"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # CAP IFOL XT
    p_id_282 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000281")
    products[p_id_282] = {
        "id": p_id_282,
        "code": "MED-CAPIFOLX",
        "name": 'CAP IFOL XT',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("86.39"),
        "default_purchase_price": Decimal("69.11"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_282 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000282")
    batches[b_id_282] = {
        "id": b_id_282,
        "product_id": p_id_282,
        "batch_number": "BCH-MEDCAP-27",
        "expiry_date": date(2027, 7, 13),
        "purchase_cost": Decimal("69.11"),
        "quantity": 65,
        "is_active": True,
        "created_at": now,
    }

    # SWICH DROP
    p_id_283 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000282")
    products[p_id_283] = {
        "id": p_id_283,
        "code": "MED-SWICHDRO",
        "name": 'SWICH DROP',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("90.51"),
        "default_purchase_price": Decimal("72.41"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_283 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000283")
    batches[b_id_283] = {
        "id": b_id_283,
        "product_id": p_id_283,
        "batch_number": "BCH-MEDSWI-28",
        "expiry_date": date(2028, 8, 14),
        "purchase_cost": Decimal("72.41"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # SORBILINE 200 ML SYP
    p_id_284 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000283")
    products[p_id_284] = {
        "id": p_id_284,
        "code": "MED-SORBILIN",
        "name": 'SORBILINE 200 ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("272.44"),
        "default_purchase_price": Decimal("217.95"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_284 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000284")
    batches[b_id_284] = {
        "id": b_id_284,
        "product_id": p_id_284,
        "batch_number": "BCH-MEDSOR-27",
        "expiry_date": date(2027, 9, 15),
        "purchase_cost": Decimal("217.95"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # CTZ 30 ML SYRUP
    p_id_285 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000284")
    products[p_id_285] = {
        "id": p_id_285,
        "code": "MED-CTZ30MLS",
        "name": 'CTZ 30 ML SYRUP',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("40.62"),
        "default_purchase_price": Decimal("32.50"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_285 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000285")
    batches[b_id_285] = {
        "id": b_id_285,
        "product_id": p_id_285,
        "batch_number": "BCH-MEDCTZ-28",
        "expiry_date": date(2028, 10, 16),
        "purchase_cost": Decimal("32.50"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TORSINEX 10 MG TAB
    p_id_286 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000285")
    products[p_id_286] = {
        "id": p_id_286,
        "code": "MED-TORSINEX",
        "name": 'TORSINEX 10 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("94.90"),
        "default_purchase_price": Decimal("75.92"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_286 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000286")
    batches[b_id_286] = {
        "id": b_id_286,
        "product_id": p_id_286,
        "batch_number": "BCH-MEDTOR-27",
        "expiry_date": date(2027, 11, 17),
        "purchase_cost": Decimal("75.92"),
        "quantity": 9,
        "is_active": True,
        "created_at": now,
    }

    # ARBITEL 40 MG TAB TAB
    p_id_287 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000286")
    products[p_id_287] = {
        "id": p_id_287,
        "code": "MED-ARBITEL4",
        "name": 'ARBITEL 40 MG TAB TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("181.92"),
        "default_purchase_price": Decimal("145.54"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_287 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000287")
    batches[b_id_287] = {
        "id": b_id_287,
        "product_id": p_id_287,
        "batch_number": "BCH-MEDARB-28",
        "expiry_date": date(2028, 12, 18),
        "purchase_cost": Decimal("145.54"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # AMLOTUS L TAB
    p_id_288 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000287")
    products[p_id_288] = {
        "id": p_id_288,
        "code": "MED-AMLOTUSL",
        "name": 'AMLOTUS L TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("187.33"),
        "default_purchase_price": Decimal("149.86"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_288 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000288")
    batches[b_id_288] = {
        "id": b_id_288,
        "product_id": p_id_288,
        "batch_number": "BCH-MEDAML-27",
        "expiry_date": date(2027, 1, 19),
        "purchase_cost": Decimal("149.86"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # MYLOD-L
    p_id_289 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000288")
    products[p_id_289] = {
        "id": p_id_289,
        "code": "MED-MYLODL",
        "name": 'MYLOD-L',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("194.21"),
        "default_purchase_price": Decimal("155.37"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_289 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000289")
    batches[b_id_289] = {
        "id": b_id_289,
        "product_id": p_id_289,
        "batch_number": "BCH-MEDMYL-28",
        "expiry_date": date(2028, 2, 20),
        "purchase_cost": Decimal("155.37"),
        "quantity": 29,
        "is_active": True,
        "created_at": now,
    }

    # MYOXIN 0.125 TAB
    p_id_290 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000289")
    products[p_id_290] = {
        "id": p_id_290,
        "code": "MED-MYOXIN01",
        "name": 'MYOXIN 0.125 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("20.59"),
        "default_purchase_price": Decimal("16.47"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_290 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000290")
    batches[b_id_290] = {
        "id": b_id_290,
        "product_id": p_id_290,
        "batch_number": "BCH-MEDMYO-27",
        "expiry_date": date(2027, 3, 21),
        "purchase_cost": Decimal("16.47"),
        "quantity": 26,
        "is_active": True,
        "created_at": now,
    }

    # REPANIDE 1
    p_id_291 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000290")
    products[p_id_291] = {
        "id": p_id_291,
        "code": "MED-REPANIDE",
        "name": 'REPANIDE 1',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("92.00"),
        "default_purchase_price": Decimal("73.60"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_291 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000291")
    batches[b_id_291] = {
        "id": b_id_291,
        "product_id": p_id_291,
        "batch_number": "BCH-MEDREP-28",
        "expiry_date": date(2028, 4, 22),
        "purchase_cost": Decimal("73.60"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # XONE 500 MG INJ
    p_id_292 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000291")
    products[p_id_292] = {
        "id": p_id_292,
        "code": "MED-XONE500M",
        "name": 'XONE 500 MG INJ',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("41.76"),
        "default_purchase_price": Decimal("33.41"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_292 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000292")
    batches[b_id_292] = {
        "id": b_id_292,
        "product_id": p_id_292,
        "batch_number": "BCH-MEDXON-27",
        "expiry_date": date(2027, 5, 23),
        "purchase_cost": Decimal("33.41"),
        "quantity": 14,
        "is_active": True,
        "created_at": now,
    }

    # TELMA AM TAB
    p_id_293 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000292")
    products[p_id_293] = {
        "id": p_id_293,
        "code": "MED-TELMAAMT",
        "name": 'TELMA AM TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("564.08"),
        "default_purchase_price": Decimal("451.26"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_293 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000293")
    batches[b_id_293] = {
        "id": b_id_293,
        "product_id": p_id_293,
        "batch_number": "BCH-MEDTEL-28",
        "expiry_date": date(2028, 6, 24),
        "purchase_cost": Decimal("451.26"),
        "quantity": 9,
        "is_active": True,
        "created_at": now,
    }

    # AMLONG 2.5MG TAB
    p_id_294 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000293")
    products[p_id_294] = {
        "id": p_id_294,
        "code": "MED-AMLONG25",
        "name": 'AMLONG 2.5MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("35.35"),
        "default_purchase_price": Decimal("28.28"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_294 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000294")
    batches[b_id_294] = {
        "id": b_id_294,
        "product_id": p_id_294,
        "batch_number": "BCH-MEDAML-27",
        "expiry_date": date(2027, 7, 25),
        "purchase_cost": Decimal("28.28"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # NEBILONG TAB
    p_id_295 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000294")
    products[p_id_295] = {
        "id": p_id_295,
        "code": "MED-NEBILONG",
        "name": 'NEBILONG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("405.26"),
        "default_purchase_price": Decimal("324.21"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_295 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000295")
    batches[b_id_295] = {
        "id": b_id_295,
        "product_id": p_id_295,
        "batch_number": "BCH-MEDNEB-28",
        "expiry_date": date(2028, 8, 26),
        "purchase_cost": Decimal("324.21"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # MEFTAL SPAS 60 ML SUSP
    p_id_296 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000295")
    products[p_id_296] = {
        "id": p_id_296,
        "code": "MED-MEFTALSP",
        "name": 'MEFTAL SPAS 60 ML SUSP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("150.09"),
        "default_purchase_price": Decimal("120.07"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_296 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000296")
    batches[b_id_296] = {
        "id": b_id_296,
        "product_id": p_id_296,
        "batch_number": "BCH-MEDMEF-27",
        "expiry_date": date(2027, 9, 27),
        "purchase_cost": Decimal("120.07"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # NEWLIN 50 MG TAB
    p_id_297 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000296")
    products[p_id_297] = {
        "id": p_id_297,
        "code": "MED-NEWLIN50",
        "name": 'NEWLIN 50 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("68.08"),
        "default_purchase_price": Decimal("54.46"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_297 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000297")
    batches[b_id_297] = {
        "id": b_id_297,
        "product_id": p_id_297,
        "batch_number": "BCH-MEDNEW-28",
        "expiry_date": date(2028, 10, 1),
        "purchase_cost": Decimal("54.46"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # TELVAS 40 MG TAB
    p_id_298 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000297")
    products[p_id_298] = {
        "id": p_id_298,
        "code": "MED-TELVAS40",
        "name": 'TELVAS 40 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("154.94"),
        "default_purchase_price": Decimal("123.95"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_298 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000298")
    batches[b_id_298] = {
        "id": b_id_298,
        "product_id": p_id_298,
        "batch_number": "BCH-MEDTEL-27",
        "expiry_date": date(2027, 11, 2),
        "purchase_cost": Decimal("123.95"),
        "quantity": 30,
        "is_active": True,
        "created_at": now,
    }

    # NEWRON 75 N FORTE
    p_id_299 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000298")
    products[p_id_299] = {
        "id": p_id_299,
        "code": "MED-NEWRON75",
        "name": 'NEWRON 75 N FORTE',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("187.93"),
        "default_purchase_price": Decimal("150.34"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_299 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000299")
    batches[b_id_299] = {
        "id": b_id_299,
        "product_id": p_id_299,
        "batch_number": "BCH-MEDNEW-28",
        "expiry_date": date(2028, 12, 3),
        "purchase_cost": Decimal("150.34"),
        "quantity": 25,
        "is_active": True,
        "created_at": now,
    }

    # ORTHOREX OIL
    p_id_300 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000299")
    products[p_id_300] = {
        "id": p_id_300,
        "code": "MED-ORTHOREX",
        "name": 'ORTHOREX OIL',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("231.65"),
        "default_purchase_price": Decimal("185.32"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_300 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000300")
    batches[b_id_300] = {
        "id": b_id_300,
        "product_id": p_id_300,
        "batch_number": "BCH-MEDORT-27",
        "expiry_date": date(2027, 1, 4),
        "purchase_cost": Decimal("185.32"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # ETORICA 90MG TAB
    p_id_301 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000300")
    products[p_id_301] = {
        "id": p_id_301,
        "code": "MED-ETORICA9",
        "name": 'ETORICA 90MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("453.64"),
        "default_purchase_price": Decimal("362.91"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_301 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000301")
    batches[b_id_301] = {
        "id": b_id_301,
        "product_id": p_id_301,
        "batch_number": "BCH-MEDETO-28",
        "expiry_date": date(2028, 2, 5),
        "purchase_cost": Decimal("362.91"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # INDCLAV 625MG TAB
    p_id_302 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000301")
    products[p_id_302] = {
        "id": p_id_302,
        "code": "MED-INDCLAV6",
        "name": 'INDCLAV 625MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("255.07"),
        "default_purchase_price": Decimal("204.06"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_302 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000302")
    batches[b_id_302] = {
        "id": b_id_302,
        "product_id": p_id_302,
        "batch_number": "BCH-MEDIND-27",
        "expiry_date": date(2027, 3, 6),
        "purchase_cost": Decimal("204.06"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # GLYCOMET GP 0.5MG
    p_id_303 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000302")
    products[p_id_303] = {
        "id": p_id_303,
        "code": "MED-GLYCOMET-6",
        "name": 'GLYCOMET GP 0.5MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("106.36"),
        "default_purchase_price": Decimal("85.09"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_303 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000303")
    batches[b_id_303] = {
        "id": b_id_303,
        "product_id": p_id_303,
        "batch_number": "BCH-MEDGLY-28",
        "expiry_date": date(2028, 4, 7),
        "purchase_cost": Decimal("85.09"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # MEDIGRA 25
    p_id_304 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000303")
    products[p_id_304] = {
        "id": p_id_304,
        "code": "MED-MEDIGRA2",
        "name": 'MEDIGRA 25',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("204.80"),
        "default_purchase_price": Decimal("163.84"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_304 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000304")
    batches[b_id_304] = {
        "id": b_id_304,
        "product_id": p_id_304,
        "batch_number": "BCH-MEDMED-27",
        "expiry_date": date(2027, 5, 8),
        "purchase_cost": Decimal("163.84"),
        "quantity": 18,
        "is_active": True,
        "created_at": now,
    }

    # LINAMET 1 MG
    p_id_305 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000304")
    products[p_id_305] = {
        "id": p_id_305,
        "code": "MED-LINAMET1",
        "name": 'LINAMET 1 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("254.59"),
        "default_purchase_price": Decimal("203.67"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_305 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000305")
    batches[b_id_305] = {
        "id": b_id_305,
        "product_id": p_id_305,
        "batch_number": "BCH-MEDLIN-28",
        "expiry_date": date(2028, 6, 9),
        "purchase_cost": Decimal("203.67"),
        "quantity": 32,
        "is_active": True,
        "created_at": now,
    }

    # ASCORIL D SYR 100ML
    p_id_306 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000305")
    products[p_id_306] = {
        "id": p_id_306,
        "code": "MED-ASCORILD",
        "name": 'ASCORIL D SYR 100ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("129.90"),
        "default_purchase_price": Decimal("103.92"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_306 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000306")
    batches[b_id_306] = {
        "id": b_id_306,
        "product_id": p_id_306,
        "batch_number": "BCH-MEDASC-27",
        "expiry_date": date(2027, 7, 10),
        "purchase_cost": Decimal("103.92"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # METFOR SR 1000MG
    p_id_307 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000306")
    products[p_id_307] = {
        "id": p_id_307,
        "code": "MED-METFORSR",
        "name": 'METFOR SR 1000MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("63.32"),
        "default_purchase_price": Decimal("50.66"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_307 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000307")
    batches[b_id_307] = {
        "id": b_id_307,
        "product_id": p_id_307,
        "batch_number": "BCH-MEDMET-28",
        "expiry_date": date(2028, 8, 11),
        "purchase_cost": Decimal("50.66"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # NEWRON 1500 MG TAB
    p_id_308 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000307")
    products[p_id_308] = {
        "id": p_id_308,
        "code": "MED-NEWRON15",
        "name": 'NEWRON 1500 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("186.89"),
        "default_purchase_price": Decimal("149.51"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_308 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000308")
    batches[b_id_308] = {
        "id": b_id_308,
        "product_id": p_id_308,
        "batch_number": "BCH-MEDNEW-27",
        "expiry_date": date(2027, 9, 12),
        "purchase_cost": Decimal("149.51"),
        "quantity": 23,
        "is_active": True,
        "created_at": now,
    }

    # PAAZ 0.5 TAB
    p_id_309 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000308")
    products[p_id_309] = {
        "id": p_id_309,
        "code": "MED-PAAZ05TA",
        "name": 'PAAZ 0.5 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("48.25"),
        "default_purchase_price": Decimal("38.60"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_309 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000309")
    batches[b_id_309] = {
        "id": b_id_309,
        "product_id": p_id_309,
        "batch_number": "BCH-MEDPAA-28",
        "expiry_date": date(2028, 10, 13),
        "purchase_cost": Decimal("38.60"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # PAAZ 0.25 TAB
    p_id_310 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000309")
    products[p_id_310] = {
        "id": p_id_310,
        "code": "MED-PAAZ025T",
        "name": 'PAAZ 0.25 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("24.14"),
        "default_purchase_price": Decimal("19.31"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_310 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000310")
    batches[b_id_310] = {
        "id": b_id_310,
        "product_id": p_id_310,
        "batch_number": "BCH-MEDPAA-27",
        "expiry_date": date(2027, 11, 14),
        "purchase_cost": Decimal("19.31"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # MINIL-20 TAB
    p_id_311 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000310")
    products[p_id_311] = {
        "id": p_id_311,
        "code": "MED-MINIL20T",
        "name": 'MINIL-20 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("97.04"),
        "default_purchase_price": Decimal("77.63"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_311 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000311")
    batches[b_id_311] = {
        "id": b_id_311,
        "product_id": p_id_311,
        "batch_number": "BCH-MEDMIN-28",
        "expiry_date": date(2028, 12, 15),
        "purchase_cost": Decimal("77.63"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # INNOLOL-20 MG TAB
    p_id_312 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000311")
    products[p_id_312] = {
        "id": p_id_312,
        "code": "MED-INNOLOL2",
        "name": 'INNOLOL-20 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("35.54"),
        "default_purchase_price": Decimal("28.43"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_312 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000312")
    batches[b_id_312] = {
        "id": b_id_312,
        "product_id": p_id_312,
        "batch_number": "BCH-MEDINN-27",
        "expiry_date": date(2027, 1, 16),
        "purchase_cost": Decimal("28.43"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # RAY D3 60K
    p_id_313 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000312")
    products[p_id_313] = {
        "id": p_id_313,
        "code": "MED-RAYD360K",
        "name": 'RAY D3 60K',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("433.05"),
        "default_purchase_price": Decimal("346.44"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_313 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000313")
    batches[b_id_313] = {
        "id": b_id_313,
        "product_id": p_id_313,
        "batch_number": "BCH-MEDRAY-28",
        "expiry_date": date(2028, 2, 17),
        "purchase_cost": Decimal("346.44"),
        "quantity": 7,
        "is_active": True,
        "created_at": now,
    }

    # FEROFOLIC DROP 15ML
    p_id_314 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000313")
    products[p_id_314] = {
        "id": p_id_314,
        "code": "MED-FEROFOLI",
        "name": 'FEROFOLIC DROP 15ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("72.59"),
        "default_purchase_price": Decimal("58.07"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_314 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000314")
    batches[b_id_314] = {
        "id": b_id_314,
        "product_id": p_id_314,
        "batch_number": "BCH-MEDFER-27",
        "expiry_date": date(2027, 3, 18),
        "purchase_cost": Decimal("58.07"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # AZITHRAL 200 MG 15 ML SYP
    p_id_315 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000314")
    products[p_id_315] = {
        "id": p_id_315,
        "code": "MED-AZITHRAL-3",
        "name": 'AZITHRAL 200 MG 15 ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("88.30"),
        "default_purchase_price": Decimal("70.64"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_315 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000315")
    batches[b_id_315] = {
        "id": b_id_315,
        "product_id": p_id_315,
        "batch_number": "BCH-MEDAZI-28",
        "expiry_date": date(2028, 4, 19),
        "purchase_cost": Decimal("70.64"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # GRANDEM 10ML SYP
    p_id_316 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000315")
    products[p_id_316] = {
        "id": p_id_316,
        "code": "MED-GRANDEM1",
        "name": 'GRANDEM 10ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("84.38"),
        "default_purchase_price": Decimal("67.50"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_316 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000316")
    batches[b_id_316] = {
        "id": b_id_316,
        "product_id": p_id_316,
        "batch_number": "BCH-MEDGRA-27",
        "expiry_date": date(2027, 5, 20),
        "purchase_cost": Decimal("67.50"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # RELIF SYP
    p_id_317 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000316")
    products[p_id_317] = {
        "id": p_id_317,
        "code": "MED-RELIFSYP",
        "name": 'RELIF SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("32.51"),
        "default_purchase_price": Decimal("26.01"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_317 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000317")
    batches[b_id_317] = {
        "id": b_id_317,
        "product_id": p_id_317,
        "batch_number": "BCH-MEDREL-28",
        "expiry_date": date(2028, 6, 21),
        "purchase_cost": Decimal("26.01"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # EXTACEF 200DT TAB
    p_id_318 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000317")
    products[p_id_318] = {
        "id": p_id_318,
        "code": "MED-EXTACEF2",
        "name": 'EXTACEF 200DT TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("128.24"),
        "default_purchase_price": Decimal("102.59"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_318 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000318")
    batches[b_id_318] = {
        "id": b_id_318,
        "product_id": p_id_318,
        "batch_number": "BCH-MEDEXT-27",
        "expiry_date": date(2027, 7, 22),
        "purchase_cost": Decimal("102.59"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # PANSAFE-D CAPS
    p_id_319 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000318")
    products[p_id_319] = {
        "id": p_id_319,
        "code": "MED-PANSAFED",
        "name": 'PANSAFE-D CAPS',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("143.24"),
        "default_purchase_price": Decimal("114.59"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_319 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000319")
    batches[b_id_319] = {
        "id": b_id_319,
        "product_id": p_id_319,
        "batch_number": "BCH-MEDPAN-28",
        "expiry_date": date(2028, 8, 23),
        "purchase_cost": Decimal("114.59"),
        "quantity": 24,
        "is_active": True,
        "created_at": now,
    }

    # METFOR 500MG
    p_id_320 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000319")
    products[p_id_320] = {
        "id": p_id_320,
        "code": "MED-METFOR50",
        "name": 'METFOR 500MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("20.27"),
        "default_purchase_price": Decimal("16.22"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_320 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000320")
    batches[b_id_320] = {
        "id": b_id_320,
        "product_id": p_id_320,
        "batch_number": "BCH-MEDMET-27",
        "expiry_date": date(2027, 9, 24),
        "purchase_cost": Decimal("16.22"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # CANDID CREAM 30 GM
    p_id_321 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000320")
    products[p_id_321] = {
        "id": p_id_321,
        "code": "MED-CANDIDCR",
        "name": 'CANDID CREAM 30 GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("154.91"),
        "default_purchase_price": Decimal("123.93"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_321 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000321")
    batches[b_id_321] = {
        "id": b_id_321,
        "product_id": p_id_321,
        "batch_number": "BCH-MEDCAN-28",
        "expiry_date": date(2028, 10, 25),
        "purchase_cost": Decimal("123.93"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # PANTA FAST DSR CAP
    p_id_322 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000321")
    products[p_id_322] = {
        "id": p_id_322,
        "code": "MED-PANTAFAS",
        "name": 'PANTA FAST DSR CAP',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("162.46"),
        "default_purchase_price": Decimal("129.97"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_322 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000322")
    batches[b_id_322] = {
        "id": b_id_322,
        "product_id": p_id_322,
        "batch_number": "BCH-MEDPAN-27",
        "expiry_date": date(2027, 11, 26),
        "purchase_cost": Decimal("129.97"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # R-PPI 20MG TAB
    p_id_323 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000322")
    products[p_id_323] = {
        "id": p_id_323,
        "code": "MED-RPPI20MG",
        "name": 'R-PPI 20MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("60.04"),
        "default_purchase_price": Decimal("48.03"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_323 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000323")
    batches[b_id_323] = {
        "id": b_id_323,
        "product_id": p_id_323,
        "batch_number": "BCH-MEDRPP-28",
        "expiry_date": date(2028, 12, 27),
        "purchase_cost": Decimal("48.03"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # SWICH50MG DRY SYP
    p_id_324 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000323")
    products[p_id_324] = {
        "id": p_id_324,
        "code": "MED-SWICH50M",
        "name": 'SWICH50MG DRY SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("118.79"),
        "default_purchase_price": Decimal("95.03"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_324 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000324")
    batches[b_id_324] = {
        "id": b_id_324,
        "product_id": p_id_324,
        "batch_number": "BCH-MEDSWI-27",
        "expiry_date": date(2027, 1, 1),
        "purchase_cost": Decimal("95.03"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # AMLOD 10 MG
    p_id_325 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000324")
    products[p_id_325] = {
        "id": p_id_325,
        "code": "MED-AMLOD10M",
        "name": 'AMLOD 10 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("122.12"),
        "default_purchase_price": Decimal("97.70"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_325 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000325")
    batches[b_id_325] = {
        "id": b_id_325,
        "product_id": p_id_325,
        "batch_number": "BCH-MEDAML-28",
        "expiry_date": date(2028, 2, 2),
        "purchase_cost": Decimal("97.70"),
        "quantity": 30,
        "is_active": True,
        "created_at": now,
    }

    # MEGA CV 625MG TAB
    p_id_326 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000325")
    products[p_id_326] = {
        "id": p_id_326,
        "code": "MED-MEGACV62",
        "name": 'MEGA CV 625MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("252.97"),
        "default_purchase_price": Decimal("202.38"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_326 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000326")
    batches[b_id_326] = {
        "id": b_id_326,
        "product_id": p_id_326,
        "batch_number": "BCH-MEDMEG-27",
        "expiry_date": date(2027, 3, 3),
        "purchase_cost": Decimal("202.38"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TELMA 40MG TAB
    p_id_327 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000326")
    products[p_id_327] = {
        "id": p_id_327,
        "code": "MED-TELMA40M",
        "name": 'TELMA 40MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("387.40"),
        "default_purchase_price": Decimal("309.92"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_327 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000327")
    batches[b_id_327] = {
        "id": b_id_327,
        "product_id": p_id_327,
        "batch_number": "BCH-MEDTEL-28",
        "expiry_date": date(2028, 4, 4),
        "purchase_cost": Decimal("309.92"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # FEZA 120MG TAB
    p_id_328 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000327")
    products[p_id_328] = {
        "id": p_id_328,
        "code": "MED-FEZA120M",
        "name": 'FEZA 120MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("104.08"),
        "default_purchase_price": Decimal("83.26"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_328 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000328")
    batches[b_id_328] = {
        "id": b_id_328,
        "product_id": p_id_328,
        "batch_number": "BCH-MEDFEZ-27",
        "expiry_date": date(2027, 5, 5),
        "purchase_cost": Decimal("83.26"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB UDCA 300MG
    p_id_329 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000328")
    products[p_id_329] = {
        "id": p_id_329,
        "code": "MED-TABUDCA3",
        "name": 'TAB UDCA 300MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("398.39"),
        "default_purchase_price": Decimal("318.71"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_329 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000329")
    batches[b_id_329] = {
        "id": b_id_329,
        "product_id": p_id_329,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 6),
        "purchase_cost": Decimal("318.71"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # MEDIGRA-25
    p_id_330 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000329")
    products[p_id_330] = {
        "id": p_id_330,
        "code": "MED-MEDIGRA2-1",
        "name": 'MEDIGRA-25',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("204.77"),
        "default_purchase_price": Decimal("163.82"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_330 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000330")
    batches[b_id_330] = {
        "id": b_id_330,
        "product_id": p_id_330,
        "batch_number": "BCH-MEDMED-27",
        "expiry_date": date(2027, 7, 7),
        "purchase_cost": Decimal("163.82"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # MEFTAL 500MG TAB
    p_id_331 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000330")
    products[p_id_331] = {
        "id": p_id_331,
        "code": "MED-MEFTAL50",
        "name": 'MEFTAL 500MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("56.71"),
        "default_purchase_price": Decimal("45.37"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_331 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000331")
    batches[b_id_331] = {
        "id": b_id_331,
        "product_id": p_id_331,
        "batch_number": "BCH-MEDMEF-28",
        "expiry_date": date(2028, 8, 8),
        "purchase_cost": Decimal("45.37"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ORNIDA 500MG TAB
    p_id_332 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000331")
    products[p_id_332] = {
        "id": p_id_332,
        "code": "MED-ORNIDA50",
        "name": 'ORNIDA 500MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("238.31"),
        "default_purchase_price": Decimal("190.65"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_332 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000332")
    batches[b_id_332] = {
        "id": b_id_332,
        "product_id": p_id_332,
        "batch_number": "BCH-MEDORN-27",
        "expiry_date": date(2027, 9, 9),
        "purchase_cost": Decimal("190.65"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # KETOLAK-TAB
    p_id_333 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000332")
    products[p_id_333] = {
        "id": p_id_333,
        "code": "MED-KETOLAKT",
        "name": 'KETOLAK-TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("89.35"),
        "default_purchase_price": Decimal("71.48"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_333 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000333")
    batches[b_id_333] = {
        "id": b_id_333,
        "product_id": p_id_333,
        "batch_number": "BCH-MEDKET-28",
        "expiry_date": date(2028, 10, 10),
        "purchase_cost": Decimal("71.48"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # VOZIN-TAB
    p_id_334 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000333")
    products[p_id_334] = {
        "id": p_id_334,
        "code": "MED-VOZINTAB",
        "name": 'VOZIN-TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("61.24"),
        "default_purchase_price": Decimal("48.99"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_334 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000334")
    batches[b_id_334] = {
        "id": b_id_334,
        "product_id": p_id_334,
        "batch_number": "BCH-MEDVOZ-27",
        "expiry_date": date(2027, 11, 11),
        "purchase_cost": Decimal("48.99"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # SIPTIN 50
    p_id_335 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000334")
    products[p_id_335] = {
        "id": p_id_335,
        "code": "MED-SIPTIN50",
        "name": 'SIPTIN 50',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("257.90"),
        "default_purchase_price": Decimal("206.32"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_335 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000335")
    batches[b_id_335] = {
        "id": b_id_335,
        "product_id": p_id_335,
        "batch_number": "BCH-MEDSIP-28",
        "expiry_date": date(2028, 12, 12),
        "purchase_cost": Decimal("206.32"),
        "quantity": 7,
        "is_active": True,
        "created_at": now,
    }

    # SIPTIN 100 TAB
    p_id_336 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000335")
    products[p_id_336] = {
        "id": p_id_336,
        "code": "MED-SIPTIN10",
        "name": 'SIPTIN 100 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("361.08"),
        "default_purchase_price": Decimal("288.86"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_336 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000336")
    batches[b_id_336] = {
        "id": b_id_336,
        "product_id": p_id_336,
        "batch_number": "BCH-MEDSIP-27",
        "expiry_date": date(2027, 1, 13),
        "purchase_cost": Decimal("288.86"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # NETFORMIN G2
    p_id_337 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000336")
    products[p_id_337] = {
        "id": p_id_337,
        "code": "MED-NETFORMI",
        "name": 'NETFORMIN G2',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("147.22"),
        "default_purchase_price": Decimal("117.78"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_337 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000337")
    batches[b_id_337] = {
        "id": b_id_337,
        "product_id": p_id_337,
        "batch_number": "BCH-MEDNET-28",
        "expiry_date": date(2028, 2, 14),
        "purchase_cost": Decimal("117.78"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # METFOR G1
    p_id_338 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000337")
    products[p_id_338] = {
        "id": p_id_338,
        "code": "MED-METFORG1",
        "name": 'METFOR G1',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("97.38"),
        "default_purchase_price": Decimal("77.90"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_338 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000338")
    batches[b_id_338] = {
        "id": b_id_338,
        "product_id": p_id_338,
        "batch_number": "BCH-MEDMET-27",
        "expiry_date": date(2027, 3, 15),
        "purchase_cost": Decimal("77.90"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # METFOR G1 FORTE
    p_id_339 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000338")
    products[p_id_339] = {
        "id": p_id_339,
        "code": "MED-METFORG1-1",
        "name": 'METFOR G1 FORTE',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("111.44"),
        "default_purchase_price": Decimal("89.15"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_339 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000339")
    batches[b_id_339] = {
        "id": b_id_339,
        "product_id": p_id_339,
        "batch_number": "BCH-MEDMET-28",
        "expiry_date": date(2028, 4, 16),
        "purchase_cost": Decimal("89.15"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # DIAPRIDE M4 FORTE TAB
    p_id_340 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000339")
    products[p_id_340] = {
        "id": p_id_340,
        "code": "MED-DIAPRIDE-3",
        "name": 'DIAPRIDE M4 FORTE TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("353.96"),
        "default_purchase_price": Decimal("283.17"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_340 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000340")
    batches[b_id_340] = {
        "id": b_id_340,
        "product_id": p_id_340,
        "batch_number": "BCH-MEDDIA-27",
        "expiry_date": date(2027, 5, 17),
        "purchase_cost": Decimal("283.17"),
        "quantity": 24,
        "is_active": True,
        "created_at": now,
    }

    # METAPRO-XL 25
    p_id_341 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000340")
    products[p_id_341] = {
        "id": p_id_341,
        "code": "MED-METAPROX",
        "name": 'METAPRO-XL 25',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("61.95"),
        "default_purchase_price": Decimal("49.56"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_341 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000341")
    batches[b_id_341] = {
        "id": b_id_341,
        "product_id": p_id_341,
        "batch_number": "BCH-MEDMET-28",
        "expiry_date": date(2028, 6, 18),
        "purchase_cost": Decimal("49.56"),
        "quantity": 60,
        "is_active": True,
        "created_at": now,
    }

    # METLOC XL 50
    p_id_342 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000341")
    products[p_id_342] = {
        "id": p_id_342,
        "code": "MED-METLOCXL",
        "name": 'METLOC XL 50',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("107.93"),
        "default_purchase_price": Decimal("86.34"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_342 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000342")
    batches[b_id_342] = {
        "id": b_id_342,
        "product_id": p_id_342,
        "batch_number": "BCH-MEDMET-27",
        "expiry_date": date(2027, 7, 19),
        "purchase_cost": Decimal("86.34"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # METAPRO-XL 50
    p_id_343 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000342")
    products[p_id_343] = {
        "id": p_id_343,
        "code": "MED-METAPROX-1",
        "name": 'METAPRO-XL 50',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("83.64"),
        "default_purchase_price": Decimal("66.91"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_343 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000343")
    batches[b_id_343] = {
        "id": b_id_343,
        "product_id": p_id_343,
        "batch_number": "BCH-MEDMET-28",
        "expiry_date": date(2028, 8, 20),
        "purchase_cost": Decimal("66.91"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # METLOC XL 12.5
    p_id_344 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000343")
    products[p_id_344] = {
        "id": p_id_344,
        "code": "MED-METLOCXL-1",
        "name": 'METLOC XL 12.5',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("77.30"),
        "default_purchase_price": Decimal("61.84"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_344 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000344")
    batches[b_id_344] = {
        "id": b_id_344,
        "product_id": p_id_344,
        "batch_number": "BCH-MEDMET-27",
        "expiry_date": date(2027, 9, 21),
        "purchase_cost": Decimal("61.84"),
        "quantity": 46,
        "is_active": True,
        "created_at": now,
    }

    # MYLOD2.5
    p_id_345 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000344")
    products[p_id_345] = {
        "id": p_id_345,
        "code": "MED-MYLOD25",
        "name": 'MYLOD2.5',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("36.31"),
        "default_purchase_price": Decimal("29.05"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_345 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000345")
    batches[b_id_345] = {
        "id": b_id_345,
        "product_id": p_id_345,
        "batch_number": "BCH-MEDMYL-28",
        "expiry_date": date(2028, 10, 22),
        "purchase_cost": Decimal("29.05"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # MYLOD5-TAB
    p_id_346 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000345")
    products[p_id_346] = {
        "id": p_id_346,
        "code": "MED-MYLOD5TA",
        "name": 'MYLOD5-TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("78.00"),
        "default_purchase_price": Decimal("62.40"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_346 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000346")
    batches[b_id_346] = {
        "id": b_id_346,
        "product_id": p_id_346,
        "batch_number": "BCH-MEDMYL-27",
        "expiry_date": date(2027, 11, 23),
        "purchase_cost": Decimal("62.40"),
        "quantity": 30,
        "is_active": True,
        "created_at": now,
    }

    # MYLOD-LH-TAB
    p_id_347 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000346")
    products[p_id_347] = {
        "id": p_id_347,
        "code": "MED-MYLODLHT",
        "name": 'MYLOD-LH-TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("94.69"),
        "default_purchase_price": Decimal("75.75"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_347 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000347")
    batches[b_id_347] = {
        "id": b_id_347,
        "product_id": p_id_347,
        "batch_number": "BCH-MEDMYL-28",
        "expiry_date": date(2028, 12, 24),
        "purchase_cost": Decimal("75.75"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # ROSUTAB-20
    p_id_348 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000347")
    products[p_id_348] = {
        "id": p_id_348,
        "code": "MED-ROSUTAB2",
        "name": 'ROSUTAB-20',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("390.44"),
        "default_purchase_price": Decimal("312.35"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_348 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000348")
    batches[b_id_348] = {
        "id": b_id_348,
        "product_id": p_id_348,
        "batch_number": "BCH-MEDROS-27",
        "expiry_date": date(2027, 1, 25),
        "purchase_cost": Decimal("312.35"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # ROSUTAB 5
    p_id_349 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000348")
    products[p_id_349] = {
        "id": p_id_349,
        "code": "MED-ROSUTAB5",
        "name": 'ROSUTAB 5',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("121.85"),
        "default_purchase_price": Decimal("97.48"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_349 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000349")
    batches[b_id_349] = {
        "id": b_id_349,
        "product_id": p_id_349,
        "batch_number": "BCH-MEDROS-28",
        "expiry_date": date(2028, 2, 26),
        "purchase_cost": Decimal("97.48"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # RESERT H
    p_id_350 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000349")
    products[p_id_350] = {
        "id": p_id_350,
        "code": "MED-RESERTH",
        "name": 'RESERT H',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("213.09"),
        "default_purchase_price": Decimal("170.47"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_350 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000350")
    batches[b_id_350] = {
        "id": b_id_350,
        "product_id": p_id_350,
        "batch_number": "BCH-MEDRES-27",
        "expiry_date": date(2027, 3, 27),
        "purchase_cost": Decimal("170.47"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # RESERT 25
    p_id_351 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000350")
    products[p_id_351] = {
        "id": p_id_351,
        "code": "MED-RESERT25",
        "name": 'RESERT 25',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("64.67"),
        "default_purchase_price": Decimal("51.74"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_351 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000351")
    batches[b_id_351] = {
        "id": b_id_351,
        "product_id": p_id_351,
        "batch_number": "BCH-MEDRES-28",
        "expiry_date": date(2028, 4, 1),
        "purchase_cost": Decimal("51.74"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # TELVAS 80MG TAB
    p_id_352 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000351")
    products[p_id_352] = {
        "id": p_id_352,
        "code": "MED-TELVAS80",
        "name": 'TELVAS 80MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("276.42"),
        "default_purchase_price": Decimal("221.14"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_352 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000352")
    batches[b_id_352] = {
        "id": b_id_352,
        "product_id": p_id_352,
        "batch_number": "BCH-MEDTEL-27",
        "expiry_date": date(2027, 5, 2),
        "purchase_cost": Decimal("221.14"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ROSUTAB-10
    p_id_353 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000352")
    products[p_id_353] = {
        "id": p_id_353,
        "code": "MED-ROSUTAB1",
        "name": 'ROSUTAB-10',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("213.23"),
        "default_purchase_price": Decimal("170.58"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_353 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000353")
    batches[b_id_353] = {
        "id": b_id_353,
        "product_id": p_id_353,
        "batch_number": "BCH-MEDROS-28",
        "expiry_date": date(2028, 6, 3),
        "purchase_cost": Decimal("170.58"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TELVAS H 40/12.5
    p_id_354 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000353")
    products[p_id_354] = {
        "id": p_id_354,
        "code": "MED-TELVASH4",
        "name": 'TELVAS H 40/12.5',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("143.78"),
        "default_purchase_price": Decimal("115.02"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_354 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000354")
    batches[b_id_354] = {
        "id": b_id_354,
        "product_id": p_id_354,
        "batch_number": "BCH-MEDTEL-27",
        "expiry_date": date(2027, 7, 4),
        "purchase_cost": Decimal("115.02"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TELSARTAN H
    p_id_355 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000354")
    products[p_id_355] = {
        "id": p_id_355,
        "code": "MED-TELSARTA",
        "name": 'TELSARTAN H',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("184.12"),
        "default_purchase_price": Decimal("147.30"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_355 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000355")
    batches[b_id_355] = {
        "id": b_id_355,
        "product_id": p_id_355,
        "batch_number": "BCH-MEDTEL-28",
        "expiry_date": date(2028, 8, 5),
        "purchase_cost": Decimal("147.30"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TELMA 20
    p_id_356 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000355")
    products[p_id_356] = {
        "id": p_id_356,
        "code": "MED-TELMA20",
        "name": 'TELMA 20',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("108.61"),
        "default_purchase_price": Decimal("86.89"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_356 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000356")
    batches[b_id_356] = {
        "id": b_id_356,
        "product_id": p_id_356,
        "batch_number": "BCH-MEDTEL-27",
        "expiry_date": date(2027, 9, 6),
        "purchase_cost": Decimal("86.89"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # AMLOZAR TAB
    p_id_357 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000356")
    products[p_id_357] = {
        "id": p_id_357,
        "code": "MED-AMLOZART",
        "name": 'AMLOZAR TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("493.85"),
        "default_purchase_price": Decimal("395.08"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_357 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000357")
    batches[b_id_357] = {
        "id": b_id_357,
        "product_id": p_id_357,
        "batch_number": "BCH-MEDAML-28",
        "expiry_date": date(2028, 10, 7),
        "purchase_cost": Decimal("395.08"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # AMLOSAFE 5MG TAB
    p_id_358 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000357")
    products[p_id_358] = {
        "id": p_id_358,
        "code": "MED-AMLOSAFE",
        "name": 'AMLOSAFE 5MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("48.74"),
        "default_purchase_price": Decimal("38.99"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_358 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000358")
    batches[b_id_358] = {
        "id": b_id_358,
        "product_id": p_id_358,
        "batch_number": "BCH-MEDAML-27",
        "expiry_date": date(2027, 11, 8),
        "purchase_cost": Decimal("38.99"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # LUZO ONT 30 GM
    p_id_359 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000358")
    products[p_id_359] = {
        "id": p_id_359,
        "code": "MED-LUZOONT3",
        "name": 'LUZO ONT 30 GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("561.08"),
        "default_purchase_price": Decimal("448.86"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_359 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000359")
    batches[b_id_359] = {
        "id": b_id_359,
        "product_id": p_id_359,
        "batch_number": "BCH-MEDLUZ-28",
        "expiry_date": date(2028, 12, 9),
        "purchase_cost": Decimal("448.86"),
        "quantity": 1,
        "is_active": True,
        "created_at": now,
    }

    # MYLOD AT TAB
    p_id_360 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000359")
    products[p_id_360] = {
        "id": p_id_360,
        "code": "MED-MYLODATT",
        "name": 'MYLOD AT TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("124.57"),
        "default_purchase_price": Decimal("99.66"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_360 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000360")
    batches[b_id_360] = {
        "id": b_id_360,
        "product_id": p_id_360,
        "batch_number": "BCH-MEDMYL-27",
        "expiry_date": date(2027, 1, 10),
        "purchase_cost": Decimal("99.66"),
        "quantity": 33,
        "is_active": True,
        "created_at": now,
    }

    # TAZLOC 20 MG TAB
    p_id_361 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000360")
    products[p_id_361] = {
        "id": p_id_361,
        "code": "MED-TAZLOC20",
        "name": 'TAZLOC 20 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("65.24"),
        "default_purchase_price": Decimal("52.19"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_361 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000361")
    batches[b_id_361] = {
        "id": b_id_361,
        "product_id": p_id_361,
        "batch_number": "BCH-MEDTAZ-28",
        "expiry_date": date(2028, 2, 11),
        "purchase_cost": Decimal("52.19"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # OLZAP 5MG
    p_id_362 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000361")
    products[p_id_362] = {
        "id": p_id_362,
        "code": "MED-OLZAP5MG",
        "name": 'OLZAP 5MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("60.93"),
        "default_purchase_price": Decimal("48.74"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_362 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000362")
    batches[b_id_362] = {
        "id": b_id_362,
        "product_id": p_id_362,
        "batch_number": "BCH-MEDOLZ-27",
        "expiry_date": date(2027, 3, 12),
        "purchase_cost": Decimal("48.74"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TOFANIB 5
    p_id_363 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000362")
    products[p_id_363] = {
        "id": p_id_363,
        "code": "MED-TOFANIB5",
        "name": 'TOFANIB 5',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("2166.93"),
        "default_purchase_price": Decimal("1733.54"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_363 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000363")
    batches[b_id_363] = {
        "id": b_id_363,
        "product_id": p_id_363,
        "batch_number": "BCH-MEDTOF-28",
        "expiry_date": date(2028, 4, 13),
        "purchase_cost": Decimal("1733.54"),
        "quantity": 7,
        "is_active": True,
        "created_at": now,
    }

    # SONADERM-GM
    p_id_364 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000363")
    products[p_id_364] = {
        "id": p_id_364,
        "code": "MED-SONADERM",
        "name": 'SONADERM-GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("62.96"),
        "default_purchase_price": Decimal("50.37"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_364 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000364")
    batches[b_id_364] = {
        "id": b_id_364,
        "product_id": p_id_364,
        "batch_number": "BCH-MEDSON-27",
        "expiry_date": date(2027, 5, 14),
        "purchase_cost": Decimal("50.37"),
        "quantity": 18,
        "is_active": True,
        "created_at": now,
    }

    # BETAVATE-C CREAM
    p_id_365 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000364")
    products[p_id_365] = {
        "id": p_id_365,
        "code": "MED-BETAVATE",
        "name": 'BETAVATE-C CREAM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("47.39"),
        "default_purchase_price": Decimal("37.91"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_365 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000365")
    batches[b_id_365] = {
        "id": b_id_365,
        "product_id": p_id_365,
        "batch_number": "BCH-MEDBET-28",
        "expiry_date": date(2028, 6, 15),
        "purchase_cost": Decimal("37.91"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # METFORE SR 850MG TAB
    p_id_366 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000365")
    products[p_id_366] = {
        "id": p_id_366,
        "code": "MED-METFORES",
        "name": 'METFORE SR 850MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("46.42"),
        "default_purchase_price": Decimal("37.14"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_366 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000366")
    batches[b_id_366] = {
        "id": b_id_366,
        "product_id": p_id_366,
        "batch_number": "BCH-MEDMET-27",
        "expiry_date": date(2027, 7, 16),
        "purchase_cost": Decimal("37.14"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # SEZ 1000 TAB
    p_id_367 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000366")
    products[p_id_367] = {
        "id": p_id_367,
        "code": "MED-SEZ1000T",
        "name": 'SEZ 1000 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("111.34"),
        "default_purchase_price": Decimal("89.07"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_367 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000367")
    batches[b_id_367] = {
        "id": b_id_367,
        "product_id": p_id_367,
        "batch_number": "BCH-MEDSEZ-28",
        "expiry_date": date(2028, 8, 17),
        "purchase_cost": Decimal("89.07"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # A TO Z SYP 200ML
    p_id_368 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000367")
    products[p_id_368] = {
        "id": p_id_368,
        "code": "MED-ATOZSYP2",
        "name": 'A TO Z SYP 200ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("291.66"),
        "default_purchase_price": Decimal("233.33"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_368 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000368")
    batches[b_id_368] = {
        "id": b_id_368,
        "product_id": p_id_368,
        "batch_number": "BCH-MEDATO-27",
        "expiry_date": date(2027, 9, 18),
        "purchase_cost": Decimal("233.33"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TELMA 80 MG TAB.
    p_id_369 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000368")
    products[p_id_369] = {
        "id": p_id_369,
        "code": "MED-TELMA80M",
        "name": 'TELMA 80 MG TAB.',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("292.23"),
        "default_purchase_price": Decimal("233.78"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_369 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000369")
    batches[b_id_369] = {
        "id": b_id_369,
        "product_id": p_id_369,
        "batch_number": "BCH-MEDTEL-28",
        "expiry_date": date(2028, 10, 19),
        "purchase_cost": Decimal("233.78"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # CANDID B 30ML LOTION
    p_id_370 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000369")
    products[p_id_370] = {
        "id": p_id_370,
        "code": "MED-CANDIDB3",
        "name": 'CANDID B 30ML LOTION',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("405.94"),
        "default_purchase_price": Decimal("324.75"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_370 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000370")
    batches[b_id_370] = {
        "id": b_id_370,
        "product_id": p_id_370,
        "batch_number": "BCH-MEDCAN-27",
        "expiry_date": date(2027, 11, 20),
        "purchase_cost": Decimal("324.75"),
        "quantity": 9,
        "is_active": True,
        "created_at": now,
    }

    # A TO Z 100ML SYP
    p_id_371 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000370")
    products[p_id_371] = {
        "id": p_id_371,
        "code": "MED-ATOZ100M",
        "name": 'A TO Z 100ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("160.85"),
        "default_purchase_price": Decimal("128.68"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_371 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000371")
    batches[b_id_371] = {
        "id": b_id_371,
        "product_id": p_id_371,
        "batch_number": "BCH-MEDATO-28",
        "expiry_date": date(2028, 12, 21),
        "purchase_cost": Decimal("128.68"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # NULONG 10 TAB
    p_id_372 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000371")
    products[p_id_372] = {
        "id": p_id_372,
        "code": "MED-NULONG10",
        "name": 'NULONG 10 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("317.82"),
        "default_purchase_price": Decimal("254.26"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_372 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000372")
    batches[b_id_372] = {
        "id": b_id_372,
        "product_id": p_id_372,
        "batch_number": "BCH-MEDNUL-27",
        "expiry_date": date(2027, 1, 22),
        "purchase_cost": Decimal("254.26"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # DICLOTAL FORTE GEL
    p_id_373 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000372")
    products[p_id_373] = {
        "id": p_id_373,
        "code": "MED-DICLOTAL-1",
        "name": 'DICLOTAL FORTE GEL',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("203.17"),
        "default_purchase_price": Decimal("162.54"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_373 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000373")
    batches[b_id_373] = {
        "id": b_id_373,
        "product_id": p_id_373,
        "batch_number": "BCH-MEDDIC-28",
        "expiry_date": date(2028, 2, 23),
        "purchase_cost": Decimal("162.54"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # VASTATIN 10 TAB
    p_id_374 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000373")
    products[p_id_374] = {
        "id": p_id_374,
        "code": "MED-VASTATIN",
        "name": 'VASTATIN 10 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("109.89"),
        "default_purchase_price": Decimal("87.91"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_374 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000374")
    batches[b_id_374] = {
        "id": b_id_374,
        "product_id": p_id_374,
        "batch_number": "BCH-MEDVAS-27",
        "expiry_date": date(2027, 3, 24),
        "purchase_cost": Decimal("87.91"),
        "quantity": 33,
        "is_active": True,
        "created_at": now,
    }

    # IFOL TAB
    p_id_375 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000374")
    products[p_id_375] = {
        "id": p_id_375,
        "code": "MED-IFOLTAB",
        "name": 'IFOL TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("96.91"),
        "default_purchase_price": Decimal("77.53"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_375 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000375")
    batches[b_id_375] = {
        "id": b_id_375,
        "product_id": p_id_375,
        "batch_number": "BCH-MEDIFO-28",
        "expiry_date": date(2028, 4, 25),
        "purchase_cost": Decimal("77.53"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # METLOC -XL 25
    p_id_376 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000375")
    products[p_id_376] = {
        "id": p_id_376,
        "code": "MED-METLOCXL-2",
        "name": 'METLOC -XL 25',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("106.64"),
        "default_purchase_price": Decimal("85.31"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_376 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000376")
    batches[b_id_376] = {
        "id": b_id_376,
        "product_id": p_id_376,
        "batch_number": "BCH-MEDMET-27",
        "expiry_date": date(2027, 5, 26),
        "purchase_cost": Decimal("85.31"),
        "quantity": 182,
        "is_active": True,
        "created_at": now,
    }

    # GLYFALL G2
    p_id_377 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000376")
    products[p_id_377] = {
        "id": p_id_377,
        "code": "MED-GLYFALLG",
        "name": 'GLYFALL G2',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("224.04"),
        "default_purchase_price": Decimal("179.23"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_377 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000377")
    batches[b_id_377] = {
        "id": b_id_377,
        "product_id": p_id_377,
        "batch_number": "BCH-MEDGLY-28",
        "expiry_date": date(2028, 6, 27),
        "purchase_cost": Decimal("179.23"),
        "quantity": 25,
        "is_active": True,
        "created_at": now,
    }

    # HEPACT-150 MG TAB
    p_id_378 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000377")
    products[p_id_378] = {
        "id": p_id_378,
        "code": "MED-HEPACT15",
        "name": 'HEPACT-150 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("259.19"),
        "default_purchase_price": Decimal("207.35"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_378 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000378")
    batches[b_id_378] = {
        "id": b_id_378,
        "product_id": p_id_378,
        "batch_number": "BCH-MEDHEP-27",
        "expiry_date": date(2027, 7, 1),
        "purchase_cost": Decimal("207.35"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # SMARTAN-50 TAB
    p_id_379 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000378")
    products[p_id_379] = {
        "id": p_id_379,
        "code": "MED-SMARTAN5",
        "name": 'SMARTAN-50 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("160.97"),
        "default_purchase_price": Decimal("128.78"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_379 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000379")
    batches[b_id_379] = {
        "id": b_id_379,
        "product_id": p_id_379,
        "batch_number": "BCH-MEDSMA-28",
        "expiry_date": date(2028, 8, 2),
        "purchase_cost": Decimal("128.78"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ARSIL-DX (100 ML) SYP
    p_id_380 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000379")
    products[p_id_380] = {
        "id": p_id_380,
        "code": "MED-ARSILDX1",
        "name": 'ARSIL-DX (100 ML) SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("67.22"),
        "default_purchase_price": Decimal("53.78"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_380 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000380")
    batches[b_id_380] = {
        "id": b_id_380,
        "product_id": p_id_380,
        "batch_number": "BCH-MEDARS-27",
        "expiry_date": date(2027, 9, 3),
        "purchase_cost": Decimal("53.78"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # TRANLOK 500 MG TAB
    p_id_381 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000380")
    products[p_id_381] = {
        "id": p_id_381,
        "code": "MED-TRANLOK5",
        "name": 'TRANLOK 500 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("186.06"),
        "default_purchase_price": Decimal("148.85"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_381 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000381")
    batches[b_id_381] = {
        "id": b_id_381,
        "product_id": p_id_381,
        "batch_number": "BCH-MEDTRA-28",
        "expiry_date": date(2028, 10, 4),
        "purchase_cost": Decimal("148.85"),
        "quantity": 7,
        "is_active": True,
        "created_at": now,
    }

    # SPRIL-25MG
    p_id_382 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000381")
    products[p_id_382] = {
        "id": p_id_382,
        "code": "MED-SPRIL25M",
        "name": 'SPRIL-25MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("81.65"),
        "default_purchase_price": Decimal("65.32"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_382 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000382")
    batches[b_id_382] = {
        "id": b_id_382,
        "product_id": p_id_382,
        "batch_number": "BCH-MEDSPR-27",
        "expiry_date": date(2027, 11, 5),
        "purchase_cost": Decimal("65.32"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # NULONG 5 MG
    p_id_383 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000382")
    products[p_id_383] = {
        "id": p_id_383,
        "code": "MED-NULONG5M",
        "name": 'NULONG 5 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("177.90"),
        "default_purchase_price": Decimal("142.32"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_383 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000383")
    batches[b_id_383] = {
        "id": b_id_383,
        "product_id": p_id_383,
        "batch_number": "BCH-MEDNUL-28",
        "expiry_date": date(2028, 12, 6),
        "purchase_cost": Decimal("142.32"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ZITA PLUS TAB
    p_id_384 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000383")
    products[p_id_384] = {
        "id": p_id_384,
        "code": "MED-ZITAPLUS",
        "name": 'ZITA PLUS TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("311.99"),
        "default_purchase_price": Decimal("249.59"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_384 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000384")
    batches[b_id_384] = {
        "id": b_id_384,
        "product_id": p_id_384,
        "batch_number": "BCH-MEDZIT-27",
        "expiry_date": date(2027, 1, 7),
        "purchase_cost": Decimal("249.59"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # DEXORANGE SYP
    p_id_385 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000384")
    products[p_id_385] = {
        "id": p_id_385,
        "code": "MED-DEXORANG",
        "name": 'DEXORANGE SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("282.59"),
        "default_purchase_price": Decimal("226.07"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_385 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000385")
    batches[b_id_385] = {
        "id": b_id_385,
        "product_id": p_id_385,
        "batch_number": "BCH-MEDDEX-28",
        "expiry_date": date(2028, 2, 8),
        "purchase_cost": Decimal("226.07"),
        "quantity": 17,
        "is_active": True,
        "created_at": now,
    }

    # CLOZIDE 10MG
    p_id_386 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000385")
    products[p_id_386] = {
        "id": p_id_386,
        "code": "MED-CLOZIDE1",
        "name": 'CLOZIDE 10MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("81.65"),
        "default_purchase_price": Decimal("65.32"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_386 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000386")
    batches[b_id_386] = {
        "id": b_id_386,
        "product_id": p_id_386,
        "batch_number": "BCH-MEDCLO-27",
        "expiry_date": date(2027, 3, 9),
        "purchase_cost": Decimal("65.32"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # METFOR SR 500 MG TAB
    p_id_387 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000386")
    products[p_id_387] = {
        "id": p_id_387,
        "code": "MED-METFORSR-1",
        "name": 'METFOR SR 500 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("37.99"),
        "default_purchase_price": Decimal("30.39"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_387 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000387")
    batches[b_id_387] = {
        "id": b_id_387,
        "product_id": p_id_387,
        "batch_number": "BCH-MEDMET-28",
        "expiry_date": date(2028, 4, 10),
        "purchase_cost": Decimal("30.39"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # HOPACE-2.5MG TAB
    p_id_388 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000387")
    products[p_id_388] = {
        "id": p_id_388,
        "code": "MED-HOPACE25",
        "name": 'HOPACE-2.5MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("142.85"),
        "default_purchase_price": Decimal("114.28"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_388 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000388")
    batches[b_id_388] = {
        "id": b_id_388,
        "product_id": p_id_388,
        "batch_number": "BCH-MEDHOP-27",
        "expiry_date": date(2027, 5, 11),
        "purchase_cost": Decimal("114.28"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # LOSIUM 50MG TAB
    p_id_389 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000388")
    products[p_id_389] = {
        "id": p_id_389,
        "code": "MED-LOSIUM50",
        "name": 'LOSIUM 50MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("263.99"),
        "default_purchase_price": Decimal("211.19"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_389 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000389")
    batches[b_id_389] = {
        "id": b_id_389,
        "product_id": p_id_389,
        "batch_number": "BCH-MEDLOS-28",
        "expiry_date": date(2028, 6, 12),
        "purchase_cost": Decimal("211.19"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # CEDON 200DT TAB
    p_id_390 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000389")
    products[p_id_390] = {
        "id": p_id_390,
        "code": "MED-CEDON200",
        "name": 'CEDON 200DT TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("208.05"),
        "default_purchase_price": Decimal("166.44"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_390 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000390")
    batches[b_id_390] = {
        "id": b_id_390,
        "product_id": p_id_390,
        "batch_number": "BCH-MEDCED-27",
        "expiry_date": date(2027, 7, 13),
        "purchase_cost": Decimal("166.44"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # SILOSIN 4MG TAB
    p_id_391 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000390")
    products[p_id_391] = {
        "id": p_id_391,
        "code": "MED-SILOSIN4",
        "name": 'SILOSIN 4MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("206.83"),
        "default_purchase_price": Decimal("165.46"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_391 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000391")
    batches[b_id_391] = {
        "id": b_id_391,
        "product_id": p_id_391,
        "batch_number": "BCH-MEDSIL-28",
        "expiry_date": date(2028, 8, 14),
        "purchase_cost": Decimal("165.46"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # FORMIN G2 FORTE TAB
    p_id_392 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000391")
    products[p_id_392] = {
        "id": p_id_392,
        "code": "MED-FORMING2-1",
        "name": 'FORMIN G2 FORTE TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("172.19"),
        "default_purchase_price": Decimal("137.75"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_392 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000392")
    batches[b_id_392] = {
        "id": b_id_392,
        "product_id": p_id_392,
        "batch_number": "BCH-MEDFOR-27",
        "expiry_date": date(2027, 9, 15),
        "purchase_cost": Decimal("137.75"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # FEZA 180MG TAB
    p_id_393 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000392")
    products[p_id_393] = {
        "id": p_id_393,
        "code": "MED-FEZA180M",
        "name": 'FEZA 180MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("150.61"),
        "default_purchase_price": Decimal("120.49"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_393 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000393")
    batches[b_id_393] = {
        "id": b_id_393,
        "product_id": p_id_393,
        "batch_number": "BCH-MEDFEZ-28",
        "expiry_date": date(2028, 10, 16),
        "purchase_cost": Decimal("120.49"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # AMLONG 5MG TAB
    p_id_394 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000393")
    products[p_id_394] = {
        "id": p_id_394,
        "code": "MED-AMLONG5M",
        "name": 'AMLONG 5MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("152.12"),
        "default_purchase_price": Decimal("121.70"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_394 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000394")
    batches[b_id_394] = {
        "id": b_id_394,
        "product_id": p_id_394,
        "batch_number": "BCH-MEDAML-27",
        "expiry_date": date(2027, 11, 17),
        "purchase_cost": Decimal("121.70"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # LOSPO-H TAB
    p_id_395 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000394")
    products[p_id_395] = {
        "id": p_id_395,
        "code": "MED-LOSPOHTA",
        "name": 'LOSPO-H TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("306.08"),
        "default_purchase_price": Decimal("244.86"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_395 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000395")
    batches[b_id_395] = {
        "id": b_id_395,
        "product_id": p_id_395,
        "batch_number": "BCH-MEDLOS-28",
        "expiry_date": date(2028, 12, 18),
        "purchase_cost": Decimal("244.86"),
        "quantity": 1,
        "is_active": True,
        "created_at": now,
    }

    # DAPA 10 MG TAB
    p_id_396 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000395")
    products[p_id_396] = {
        "id": p_id_396,
        "code": "MED-DAPA10MG",
        "name": 'DAPA 10 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("226.38"),
        "default_purchase_price": Decimal("181.10"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_396 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000396")
    batches[b_id_396] = {
        "id": b_id_396,
        "product_id": p_id_396,
        "batch_number": "BCH-MEDDAP-27",
        "expiry_date": date(2027, 1, 19),
        "purchase_cost": Decimal("181.10"),
        "quantity": 101,
        "is_active": True,
        "created_at": now,
    }

    # TELSARTAN-AM
    p_id_397 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000396")
    products[p_id_397] = {
        "id": p_id_397,
        "code": "MED-TELSARTA-1",
        "name": 'TELSARTAN-AM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("146.16"),
        "default_purchase_price": Decimal("116.93"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_397 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000397")
    batches[b_id_397] = {
        "id": b_id_397,
        "product_id": p_id_397,
        "batch_number": "BCH-MEDTEL-28",
        "expiry_date": date(2028, 2, 20),
        "purchase_cost": Decimal("116.93"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # NITROFIX -SR 60MG TAB
    p_id_398 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000397")
    products[p_id_398] = {
        "id": p_id_398,
        "code": "MED-NITROFIX",
        "name": 'NITROFIX -SR 60MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("126.84"),
        "default_purchase_price": Decimal("101.47"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_398 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000398")
    batches[b_id_398] = {
        "id": b_id_398,
        "product_id": p_id_398,
        "batch_number": "BCH-MEDNIT-27",
        "expiry_date": date(2027, 3, 21),
        "purchase_cost": Decimal("101.47"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # SILOSIN-8MG TAB
    p_id_399 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000398")
    products[p_id_399] = {
        "id": p_id_399,
        "code": "MED-SILOSIN8",
        "name": 'SILOSIN-8MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("361.93"),
        "default_purchase_price": Decimal("289.54"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_399 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000399")
    batches[b_id_399] = {
        "id": b_id_399,
        "product_id": p_id_399,
        "batch_number": "BCH-MEDSIL-28",
        "expiry_date": date(2028, 4, 22),
        "purchase_cost": Decimal("289.54"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # METLOC 25 MG TAB
    p_id_400 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000399")
    products[p_id_400] = {
        "id": p_id_400,
        "code": "MED-METLOC25",
        "name": 'METLOC 25 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("41.29"),
        "default_purchase_price": Decimal("33.03"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_400 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000400")
    batches[b_id_400] = {
        "id": b_id_400,
        "product_id": p_id_400,
        "batch_number": "BCH-MEDMET-27",
        "expiry_date": date(2027, 5, 23),
        "purchase_cost": Decimal("33.03"),
        "quantity": 18,
        "is_active": True,
        "created_at": now,
    }

    # AMLOD LH TAB
    p_id_401 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000400")
    products[p_id_401] = {
        "id": p_id_401,
        "code": "MED-AMLODLHT",
        "name": 'AMLOD LH TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("106.88"),
        "default_purchase_price": Decimal("85.50"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_401 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000401")
    batches[b_id_401] = {
        "id": b_id_401,
        "product_id": p_id_401,
        "batch_number": "BCH-MEDAML-28",
        "expiry_date": date(2028, 6, 24),
        "purchase_cost": Decimal("85.50"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # SINEX MINI 15ML
    p_id_402 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000401")
    products[p_id_402] = {
        "id": p_id_402,
        "code": "MED-SINEXMIN",
        "name": 'SINEX MINI 15ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("95.02"),
        "default_purchase_price": Decimal("76.02"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_402 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000402")
    batches[b_id_402] = {
        "id": b_id_402,
        "product_id": p_id_402,
        "batch_number": "BCH-MEDSIN-27",
        "expiry_date": date(2027, 7, 25),
        "purchase_cost": Decimal("76.02"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # EBAST 20MG TAB
    p_id_403 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000402")
    products[p_id_403] = {
        "id": p_id_403,
        "code": "MED-EBAST20M",
        "name": 'EBAST 20MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("291.89"),
        "default_purchase_price": Decimal("233.51"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_403 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000403")
    batches[b_id_403] = {
        "id": b_id_403,
        "product_id": p_id_403,
        "batch_number": "BCH-MEDEBA-28",
        "expiry_date": date(2028, 8, 26),
        "purchase_cost": Decimal("233.51"),
        "quantity": 36,
        "is_active": True,
        "created_at": now,
    }

    # ATCHOL 20MG TAB
    p_id_404 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000403")
    products[p_id_404] = {
        "id": p_id_404,
        "code": "MED-ATCHOL20",
        "name": 'ATCHOL 20MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("90.68"),
        "default_purchase_price": Decimal("72.54"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_404 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000404")
    batches[b_id_404] = {
        "id": b_id_404,
        "product_id": p_id_404,
        "batch_number": "BCH-MEDATC-27",
        "expiry_date": date(2027, 9, 27),
        "purchase_cost": Decimal("72.54"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # CEFADROX KID 250MG TAB
    p_id_405 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000404")
    products[p_id_405] = {
        "id": p_id_405,
        "code": "MED-CEFADROX-1",
        "name": 'CEFADROX KID 250MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("93.35"),
        "default_purchase_price": Decimal("74.68"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_405 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000405")
    batches[b_id_405] = {
        "id": b_id_405,
        "product_id": p_id_405,
        "batch_number": "BCH-MEDCEF-28",
        "expiry_date": date(2028, 10, 1),
        "purchase_cost": Decimal("74.68"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TELMA 80 H TAB
    p_id_406 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000405")
    products[p_id_406] = {
        "id": p_id_406,
        "code": "MED-TELMA80H",
        "name": 'TELMA 80 H TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("896.47"),
        "default_purchase_price": Decimal("717.18"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_406 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000406")
    batches[b_id_406] = {
        "id": b_id_406,
        "product_id": p_id_406,
        "batch_number": "BCH-MEDTEL-27",
        "expiry_date": date(2027, 11, 2),
        "purchase_cost": Decimal("717.18"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # CILACAR 10 TAB
    p_id_407 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000406")
    products[p_id_407] = {
        "id": p_id_407,
        "code": "MED-CILACAR1",
        "name": 'CILACAR 10 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("82.60"),
        "default_purchase_price": Decimal("66.08"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_407 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000407")
    batches[b_id_407] = {
        "id": b_id_407,
        "product_id": p_id_407,
        "batch_number": "BCH-MEDCIL-28",
        "expiry_date": date(2028, 12, 3),
        "purchase_cost": Decimal("66.08"),
        "quantity": 47,
        "is_active": True,
        "created_at": now,
    }

    # Q-PIL 2.5 MG TAB
    p_id_408 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000407")
    products[p_id_408] = {
        "id": p_id_408,
        "code": "MED-QPIL25MG",
        "name": 'Q-PIL 2.5 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("23.49"),
        "default_purchase_price": Decimal("18.79"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_408 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000408")
    batches[b_id_408] = {
        "id": b_id_408,
        "product_id": p_id_408,
        "batch_number": "BCH-MEDQPI-27",
        "expiry_date": date(2027, 1, 4),
        "purchase_cost": Decimal("18.79"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # FEZA SYP
    p_id_409 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000408")
    products[p_id_409] = {
        "id": p_id_409,
        "code": "MED-FEZASYP",
        "name": 'FEZA SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("101.55"),
        "default_purchase_price": Decimal("81.24"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_409 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000409")
    batches[b_id_409] = {
        "id": b_id_409,
        "product_id": p_id_409,
        "batch_number": "BCH-MEDFEZ-28",
        "expiry_date": date(2028, 2, 5),
        "purchase_cost": Decimal("81.24"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # M-BACT 10 GM
    p_id_410 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000409")
    products[p_id_410] = {
        "id": p_id_410,
        "code": "MED-MBACT10G",
        "name": 'M-BACT 10 GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("149.60"),
        "default_purchase_price": Decimal("119.68"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_410 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000410")
    batches[b_id_410] = {
        "id": b_id_410,
        "product_id": p_id_410,
        "batch_number": "BCH-MEDMBA-27",
        "expiry_date": date(2027, 3, 6),
        "purchase_cost": Decimal("119.68"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # ARBITEL-H TAB
    p_id_411 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000410")
    products[p_id_411] = {
        "id": p_id_411,
        "code": "MED-ARBITELH",
        "name": 'ARBITEL-H TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("300.52"),
        "default_purchase_price": Decimal("240.42"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_411 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000411")
    batches[b_id_411] = {
        "id": b_id_411,
        "product_id": p_id_411,
        "batch_number": "BCH-MEDARB-28",
        "expiry_date": date(2028, 4, 7),
        "purchase_cost": Decimal("240.42"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # RENOSAFE TAB
    p_id_412 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000411")
    products[p_id_412] = {
        "id": p_id_412,
        "code": "MED-RENOSAFE",
        "name": 'RENOSAFE TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("223.36"),
        "default_purchase_price": Decimal("178.69"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_412 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000412")
    batches[b_id_412] = {
        "id": b_id_412,
        "product_id": p_id_412,
        "batch_number": "BCH-MEDREN-27",
        "expiry_date": date(2027, 5, 8),
        "purchase_cost": Decimal("178.69"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # ARISTOZYME CAP
    p_id_413 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000412")
    products[p_id_413] = {
        "id": p_id_413,
        "code": "MED-ARISTOZY-1",
        "name": 'ARISTOZYME CAP',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("157.55"),
        "default_purchase_price": Decimal("126.04"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_413 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000413")
    batches[b_id_413] = {
        "id": b_id_413,
        "product_id": p_id_413,
        "batch_number": "BCH-MEDARI-28",
        "expiry_date": date(2028, 6, 9),
        "purchase_cost": Decimal("126.04"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # LINTOR M 850 MG TAB
    p_id_414 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000413")
    products[p_id_414] = {
        "id": p_id_414,
        "code": "MED-LINTORM8",
        "name": 'LINTOR M 850 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("92.41"),
        "default_purchase_price": Decimal("73.93"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_414 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000414")
    batches[b_id_414] = {
        "id": b_id_414,
        "product_id": p_id_414,
        "batch_number": "BCH-MEDLIN-27",
        "expiry_date": date(2027, 7, 10),
        "purchase_cost": Decimal("73.93"),
        "quantity": 25,
        "is_active": True,
        "created_at": now,
    }

    # MIGON TAB
    p_id_415 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000414")
    products[p_id_415] = {
        "id": p_id_415,
        "code": "MED-MIGONTAB",
        "name": 'MIGON TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("75.46"),
        "default_purchase_price": Decimal("60.37"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_415 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000415")
    batches[b_id_415] = {
        "id": b_id_415,
        "product_id": p_id_415,
        "batch_number": "BCH-MEDMIG-28",
        "expiry_date": date(2028, 8, 11),
        "purchase_cost": Decimal("60.37"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # RESERT 50MG
    p_id_416 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000415")
    products[p_id_416] = {
        "id": p_id_416,
        "code": "MED-RESERT50",
        "name": 'RESERT 50MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("115.66"),
        "default_purchase_price": Decimal("92.53"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_416 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000416")
    batches[b_id_416] = {
        "id": b_id_416,
        "product_id": p_id_416,
        "batch_number": "BCH-MEDRES-27",
        "expiry_date": date(2027, 9, 12),
        "purchase_cost": Decimal("92.53"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # LACULAX 200ML SYP
    p_id_417 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000416")
    products[p_id_417] = {
        "id": p_id_417,
        "code": "MED-LACULAX2",
        "name": 'LACULAX 200ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("339.47"),
        "default_purchase_price": Decimal("271.58"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_417 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000417")
    batches[b_id_417] = {
        "id": b_id_417,
        "product_id": p_id_417,
        "batch_number": "BCH-MEDLAC-28",
        "expiry_date": date(2028, 10, 13),
        "purchase_cost": Decimal("271.58"),
        "quantity": 9,
        "is_active": True,
        "created_at": now,
    }

    # TURBOVAS 20 MG
    p_id_418 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000417")
    products[p_id_418] = {
        "id": p_id_418,
        "code": "MED-TURBOVAS",
        "name": 'TURBOVAS 20 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("652.40"),
        "default_purchase_price": Decimal("521.92"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_418 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000418")
    batches[b_id_418] = {
        "id": b_id_418,
        "product_id": p_id_418,
        "batch_number": "BCH-MEDTUR-27",
        "expiry_date": date(2027, 11, 14),
        "purchase_cost": Decimal("521.92"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # LINICS -M 1000 MG
    p_id_419 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000418")
    products[p_id_419] = {
        "id": p_id_419,
        "code": "MED-LINICSM1",
        "name": 'LINICS -M 1000 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("175.03"),
        "default_purchase_price": Decimal("140.02"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_419 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000419")
    batches[b_id_419] = {
        "id": b_id_419,
        "product_id": p_id_419,
        "batch_number": "BCH-MEDLIN-28",
        "expiry_date": date(2028, 12, 15),
        "purchase_cost": Decimal("140.02"),
        "quantity": 33,
        "is_active": True,
        "created_at": now,
    }

    # DIAPRIDE M2 TAB
    p_id_420 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000419")
    products[p_id_420] = {
        "id": p_id_420,
        "code": "MED-DIAPRIDE-4",
        "name": 'DIAPRIDE M2 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("464.12"),
        "default_purchase_price": Decimal("371.30"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_420 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000420")
    batches[b_id_420] = {
        "id": b_id_420,
        "product_id": p_id_420,
        "batch_number": "BCH-MEDDIA-27",
        "expiry_date": date(2027, 1, 16),
        "purchase_cost": Decimal("371.30"),
        "quantity": 69,
        "is_active": True,
        "created_at": now,
    }

    # LINTOR M 1000 TAB
    p_id_421 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000420")
    products[p_id_421] = {
        "id": p_id_421,
        "code": "MED-LINTORM1",
        "name": 'LINTOR M 1000 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("98.66"),
        "default_purchase_price": Decimal("78.93"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_421 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000421")
    batches[b_id_421] = {
        "id": b_id_421,
        "product_id": p_id_421,
        "batch_number": "BCH-MEDLIN-28",
        "expiry_date": date(2028, 2, 17),
        "purchase_cost": Decimal("78.93"),
        "quantity": 80,
        "is_active": True,
        "created_at": now,
    }

    # TELMA CT 40/6.25 TAB
    p_id_422 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000421")
    products[p_id_422] = {
        "id": p_id_422,
        "code": "MED-TELMACT4",
        "name": 'TELMA CT 40/6.25 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("500.32"),
        "default_purchase_price": Decimal("400.26"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_422 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000422")
    batches[b_id_422] = {
        "id": b_id_422,
        "product_id": p_id_422,
        "batch_number": "BCH-MEDTEL-27",
        "expiry_date": date(2027, 3, 18),
        "purchase_cost": Decimal("400.26"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # SAL 4 TAB
    p_id_423 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000422")
    products[p_id_423] = {
        "id": p_id_423,
        "code": "MED-SAL4TAB",
        "name": 'SAL 4 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("17.01"),
        "default_purchase_price": Decimal("13.61"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_423 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000423")
    batches[b_id_423] = {
        "id": b_id_423,
        "product_id": p_id_423,
        "batch_number": "BCH-MEDSAL-28",
        "expiry_date": date(2028, 4, 19),
        "purchase_cost": Decimal("13.61"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # MEFIPRIST TAB
    p_id_424 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000423")
    products[p_id_424] = {
        "id": p_id_424,
        "code": "MED-MEFIPRIS",
        "name": 'MEFIPRIST TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("391.61"),
        "default_purchase_price": Decimal("313.29"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_424 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000424")
    batches[b_id_424] = {
        "id": b_id_424,
        "product_id": p_id_424,
        "batch_number": "BCH-MEDMEF-27",
        "expiry_date": date(2027, 5, 20),
        "purchase_cost": Decimal("313.29"),
        "quantity": 30,
        "is_active": True,
        "created_at": now,
    }

    # HYTIDE 25MG TAB
    p_id_425 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000424")
    products[p_id_425] = {
        "id": p_id_425,
        "code": "MED-HYTIDE25",
        "name": 'HYTIDE 25MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("48.99"),
        "default_purchase_price": Decimal("39.19"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_425 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000425")
    batches[b_id_425] = {
        "id": b_id_425,
        "product_id": p_id_425,
        "batch_number": "BCH-MEDHYT-28",
        "expiry_date": date(2028, 6, 21),
        "purchase_cost": Decimal("39.19"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # CAMLO 2.5 MG TAB
    p_id_426 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000425")
    products[p_id_426] = {
        "id": p_id_426,
        "code": "MED-CAMLO25M",
        "name": 'CAMLO 2.5 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("34.95"),
        "default_purchase_price": Decimal("27.96"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_426 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000426")
    batches[b_id_426] = {
        "id": b_id_426,
        "product_id": p_id_426,
        "batch_number": "BCH-MEDCAM-27",
        "expiry_date": date(2027, 7, 22),
        "purchase_cost": Decimal("27.96"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # CAMLO 5 MG TAB
    p_id_427 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000426")
    products[p_id_427] = {
        "id": p_id_427,
        "code": "MED-CAMLO5MG",
        "name": 'CAMLO 5 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("75.99"),
        "default_purchase_price": Decimal("60.79"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_427 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000427")
    batches[b_id_427] = {
        "id": b_id_427,
        "product_id": p_id_427,
        "batch_number": "BCH-MEDCAM-28",
        "expiry_date": date(2028, 8, 23),
        "purchase_cost": Decimal("60.79"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # CAMLO L TAB
    p_id_428 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000427")
    products[p_id_428] = {
        "id": p_id_428,
        "code": "MED-CAMLOLTA",
        "name": 'CAMLO L TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("122.93"),
        "default_purchase_price": Decimal("98.34"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_428 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000428")
    batches[b_id_428] = {
        "id": b_id_428,
        "product_id": p_id_428,
        "batch_number": "BCH-MEDCAM-27",
        "expiry_date": date(2027, 9, 24),
        "purchase_cost": Decimal("98.34"),
        "quantity": 50,
        "is_active": True,
        "created_at": now,
    }

    # CANDID-V GELL 30 GM
    p_id_429 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000428")
    products[p_id_429] = {
        "id": p_id_429,
        "code": "MED-CANDIDVG",
        "name": 'CANDID-V GELL 30 GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("279.51"),
        "default_purchase_price": Decimal("223.61"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_429 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000429")
    batches[b_id_429] = {
        "id": b_id_429,
        "product_id": p_id_429,
        "batch_number": "BCH-MEDCAN-28",
        "expiry_date": date(2028, 10, 25),
        "purchase_cost": Decimal("223.61"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # COUMADIN 5MG TAB
    p_id_430 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000429")
    products[p_id_430] = {
        "id": p_id_430,
        "code": "MED-COUMADIN",
        "name": 'COUMADIN 5MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("56.88"),
        "default_purchase_price": Decimal("45.50"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_430 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000430")
    batches[b_id_430] = {
        "id": b_id_430,
        "product_id": p_id_430,
        "batch_number": "BCH-MEDCOU-27",
        "expiry_date": date(2027, 11, 26),
        "purchase_cost": Decimal("45.50"),
        "quantity": 9,
        "is_active": True,
        "created_at": now,
    }

    # CLODERM-S OINT
    p_id_431 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000430")
    products[p_id_431] = {
        "id": p_id_431,
        "code": "MED-CLODERMS",
        "name": 'CLODERM-S OINT',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("150.51"),
        "default_purchase_price": Decimal("120.41"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_431 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000431")
    batches[b_id_431] = {
        "id": b_id_431,
        "product_id": p_id_431,
        "batch_number": "BCH-MEDCLO-28",
        "expiry_date": date(2028, 12, 27),
        "purchase_cost": Decimal("120.41"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # DIAPRIDE M2 FORTE
    p_id_432 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000431")
    products[p_id_432] = {
        "id": p_id_432,
        "code": "MED-DIAPRIDE-5",
        "name": 'DIAPRIDE M2 FORTE',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("513.89"),
        "default_purchase_price": Decimal("411.11"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_432 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000432")
    batches[b_id_432] = {
        "id": b_id_432,
        "product_id": p_id_432,
        "batch_number": "BCH-MEDDIA-27",
        "expiry_date": date(2027, 1, 1),
        "purchase_cost": Decimal("411.11"),
        "quantity": 62,
        "is_active": True,
        "created_at": now,
    }

    # LINICS M 500MG TAB
    p_id_433 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000432")
    products[p_id_433] = {
        "id": p_id_433,
        "code": "MED-LINICSM5",
        "name": 'LINICS M 500MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("143.96"),
        "default_purchase_price": Decimal("115.17"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_433 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000433")
    batches[b_id_433] = {
        "id": b_id_433,
        "product_id": p_id_433,
        "batch_number": "BCH-MEDLIN-28",
        "expiry_date": date(2028, 2, 2),
        "purchase_cost": Decimal("115.17"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # A TO Z DROP
    p_id_434 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000433")
    products[p_id_434] = {
        "id": p_id_434,
        "code": "MED-ATOZDROP",
        "name": 'A TO Z DROP',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("119.14"),
        "default_purchase_price": Decimal("95.31"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_434 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000434")
    batches[b_id_434] = {
        "id": b_id_434,
        "product_id": p_id_434,
        "batch_number": "BCH-MEDATO-27",
        "expiry_date": date(2027, 3, 3),
        "purchase_cost": Decimal("95.31"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # CALIN 100ML LOTION
    p_id_435 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000434")
    products[p_id_435] = {
        "id": p_id_435,
        "code": "MED-CALIN100",
        "name": 'CALIN 100ML LOTION',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("108.44"),
        "default_purchase_price": Decimal("86.75"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_435 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000435")
    batches[b_id_435] = {
        "id": b_id_435,
        "product_id": p_id_435,
        "batch_number": "BCH-MEDCAL-28",
        "expiry_date": date(2028, 4, 4),
        "purchase_cost": Decimal("86.75"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TRIAD 25 MG TAB
    p_id_436 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000435")
    products[p_id_436] = {
        "id": p_id_436,
        "code": "MED-TRIAD25M",
        "name": 'TRIAD 25 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("76.85"),
        "default_purchase_price": Decimal("61.48"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_436 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000436")
    batches[b_id_436] = {
        "id": b_id_436,
        "product_id": p_id_436,
        "batch_number": "BCH-MEDTRI-27",
        "expiry_date": date(2027, 5, 5),
        "purchase_cost": Decimal("61.48"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # MONORAL 100MG D/SYP
    p_id_437 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000436")
    products[p_id_437] = {
        "id": p_id_437,
        "code": "MED-MONORAL1",
        "name": 'MONORAL 100MG D/SYP',
        "category": "Surgical",
        "unit": "Bottle",
        "mrp": Decimal("284.20"),
        "default_purchase_price": Decimal("227.36"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_437 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000437")
    batches[b_id_437] = {
        "id": b_id_437,
        "product_id": p_id_437,
        "batch_number": "BCH-MEDMON-28",
        "expiry_date": date(2028, 6, 6),
        "purchase_cost": Decimal("227.36"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # LULICAN CREAM 30GM
    p_id_438 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000437")
    products[p_id_438] = {
        "id": p_id_438,
        "code": "MED-LULICANC",
        "name": 'LULICAN CREAM 30GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("576.15"),
        "default_purchase_price": Decimal("460.92"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_438 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000438")
    batches[b_id_438] = {
        "id": b_id_438,
        "product_id": p_id_438,
        "batch_number": "BCH-MEDLUL-27",
        "expiry_date": date(2027, 7, 7),
        "purchase_cost": Decimal("460.92"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # GLUCONORMG1
    p_id_439 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000438")
    products[p_id_439] = {
        "id": p_id_439,
        "code": "MED-GLUCONOR-1",
        "name": 'GLUCONORMG1',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("373.34"),
        "default_purchase_price": Decimal("298.67"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_439 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000439")
    batches[b_id_439] = {
        "id": b_id_439,
        "product_id": p_id_439,
        "batch_number": "BCH-MEDGLU-28",
        "expiry_date": date(2028, 8, 8),
        "purchase_cost": Decimal("298.67"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # AMPRO 5 MG TAB
    p_id_440 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000439")
    products[p_id_440] = {
        "id": p_id_440,
        "code": "MED-AMPRO5MG",
        "name": 'AMPRO 5 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("51.35"),
        "default_purchase_price": Decimal("41.08"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_440 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000440")
    batches[b_id_440] = {
        "id": b_id_440,
        "product_id": p_id_440,
        "batch_number": "BCH-MEDAMP-27",
        "expiry_date": date(2027, 9, 9),
        "purchase_cost": Decimal("41.08"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # SITAMET-SR 500 MG TAB
    p_id_441 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000440")
    products[p_id_441] = {
        "id": p_id_441,
        "code": "MED-SITAMETS",
        "name": 'SITAMET-SR 500 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("265.17"),
        "default_purchase_price": Decimal("212.14"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_441 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000441")
    batches[b_id_441] = {
        "id": b_id_441,
        "product_id": p_id_441,
        "batch_number": "BCH-MEDSIT-28",
        "expiry_date": date(2028, 10, 10),
        "purchase_cost": Decimal("212.14"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # COUMADIN 3MG TAB
    p_id_442 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000441")
    products[p_id_442] = {
        "id": p_id_442,
        "code": "MED-COUMADIN-1",
        "name": 'COUMADIN 3MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("51.34"),
        "default_purchase_price": Decimal("41.07"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_442 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000442")
    batches[b_id_442] = {
        "id": b_id_442,
        "product_id": p_id_442,
        "batch_number": "BCH-MEDCOU-27",
        "expiry_date": date(2027, 11, 11),
        "purchase_cost": Decimal("41.07"),
        "quantity": 9,
        "is_active": True,
        "created_at": now,
    }

    # NITROFIX SR 30MG TAB
    p_id_443 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000442")
    products[p_id_443] = {
        "id": p_id_443,
        "code": "MED-NITROFIX-1",
        "name": 'NITROFIX SR 30MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("95.59"),
        "default_purchase_price": Decimal("76.47"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_443 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000443")
    batches[b_id_443] = {
        "id": b_id_443,
        "product_id": p_id_443,
        "batch_number": "BCH-MEDNIT-28",
        "expiry_date": date(2028, 12, 12),
        "purchase_cost": Decimal("76.47"),
        "quantity": 14,
        "is_active": True,
        "created_at": now,
    }

    # CORTILONE 10 MG TAB
    p_id_444 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000443")
    products[p_id_444] = {
        "id": p_id_444,
        "code": "MED-CORTILON",
        "name": 'CORTILONE 10 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("45.50"),
        "default_purchase_price": Decimal("36.40"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_444 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000444")
    batches[b_id_444] = {
        "id": b_id_444,
        "product_id": p_id_444,
        "batch_number": "BCH-MEDCOR-27",
        "expiry_date": date(2027, 1, 13),
        "purchase_cost": Decimal("36.40"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # CORTILONE 20 MG TAB
    p_id_445 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000444")
    products[p_id_445] = {
        "id": p_id_445,
        "code": "MED-CORTILON-1",
        "name": 'CORTILONE 20 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("85.92"),
        "default_purchase_price": Decimal("68.74"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_445 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000445")
    batches[b_id_445] = {
        "id": b_id_445,
        "product_id": p_id_445,
        "batch_number": "BCH-MEDCOR-28",
        "expiry_date": date(2028, 2, 14),
        "purchase_cost": Decimal("68.74"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # CORTILONE 40 MG TAB
    p_id_446 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000445")
    products[p_id_446] = {
        "id": p_id_446,
        "code": "MED-CORTILON-2",
        "name": 'CORTILONE 40 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("151.62"),
        "default_purchase_price": Decimal("121.30"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_446 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000446")
    batches[b_id_446] = {
        "id": b_id_446,
        "product_id": p_id_446,
        "batch_number": "BCH-MEDCOR-27",
        "expiry_date": date(2027, 3, 15),
        "purchase_cost": Decimal("121.30"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # CORTILONE 5 MG TAB
    p_id_447 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000446")
    products[p_id_447] = {
        "id": p_id_447,
        "code": "MED-CORTILON-3",
        "name": 'CORTILONE 5 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("25.40"),
        "default_purchase_price": Decimal("20.32"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_447 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000447")
    batches[b_id_447] = {
        "id": b_id_447,
        "product_id": p_id_447,
        "batch_number": "BCH-MEDCOR-28",
        "expiry_date": date(2028, 4, 16),
        "purchase_cost": Decimal("20.32"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # DAFODIL 5MG TAB
    p_id_448 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000447")
    products[p_id_448] = {
        "id": p_id_448,
        "code": "MED-DAFODIL5",
        "name": 'DAFODIL 5MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("174.04"),
        "default_purchase_price": Decimal("139.23"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_448 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000448")
    batches[b_id_448] = {
        "id": b_id_448,
        "product_id": p_id_448,
        "batch_number": "BCH-MEDDAF-27",
        "expiry_date": date(2027, 5, 17),
        "purchase_cost": Decimal("139.23"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # HOPACE-1.25MG TAB
    p_id_449 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000448")
    products[p_id_449] = {
        "id": p_id_449,
        "code": "MED-HOPACE12",
        "name": 'HOPACE-1.25MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("88.73"),
        "default_purchase_price": Decimal("70.98"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_449 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000449")
    batches[b_id_449] = {
        "id": b_id_449,
        "product_id": p_id_449,
        "batch_number": "BCH-MEDHOP-28",
        "expiry_date": date(2028, 6, 18),
        "purchase_cost": Decimal("70.98"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # BISOLOL 5MG TAB
    p_id_450 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000449")
    products[p_id_450] = {
        "id": p_id_450,
        "code": "MED-BISOLOL5",
        "name": 'BISOLOL 5MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("141.80"),
        "default_purchase_price": Decimal("113.44"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_450 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000450")
    batches[b_id_450] = {
        "id": b_id_450,
        "product_id": p_id_450,
        "batch_number": "BCH-MEDBIS-27",
        "expiry_date": date(2027, 7, 19),
        "purchase_cost": Decimal("113.44"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # AZITHRAL 100 MG 30 ML SYP
    p_id_451 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000450")
    products[p_id_451] = {
        "id": p_id_451,
        "code": "MED-AZITHRAL-4",
        "name": 'AZITHRAL 100 MG 30 ML SYP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("168.56"),
        "default_purchase_price": Decimal("134.85"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_451 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000451")
    batches[b_id_451] = {
        "id": b_id_451,
        "product_id": p_id_451,
        "batch_number": "BCH-MEDAZI-28",
        "expiry_date": date(2028, 8, 20),
        "purchase_cost": Decimal("134.85"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # CLONAZ 0.25 MG TAB
    p_id_452 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000451")
    products[p_id_452] = {
        "id": p_id_452,
        "code": "MED-CLONAZ02",
        "name": 'CLONAZ 0.25 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("61.16"),
        "default_purchase_price": Decimal("48.93"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_452 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000452")
    batches[b_id_452] = {
        "id": b_id_452,
        "product_id": p_id_452,
        "batch_number": "BCH-MEDCLO-27",
        "expiry_date": date(2027, 9, 21),
        "purchase_cost": Decimal("48.93"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # ENPIL 5 MG TAB
    p_id_453 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000452")
    products[p_id_453] = {
        "id": p_id_453,
        "code": "MED-ENPIL5MG",
        "name": 'ENPIL 5 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("62.06"),
        "default_purchase_price": Decimal("49.65"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_453 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000453")
    batches[b_id_453] = {
        "id": b_id_453,
        "product_id": p_id_453,
        "batch_number": "BCH-MEDENP-28",
        "expiry_date": date(2028, 10, 22),
        "purchase_cost": Decimal("49.65"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # FUSID B 10 GRM OINTMENT
    p_id_454 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000453")
    products[p_id_454] = {
        "id": p_id_454,
        "code": "MED-FUSIDB10",
        "name": 'FUSID B 10 GRM OINTMENT',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("127.51"),
        "default_purchase_price": Decimal("102.01"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_454 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000454")
    batches[b_id_454] = {
        "id": b_id_454,
        "product_id": p_id_454,
        "batch_number": "BCH-MEDFUS-27",
        "expiry_date": date(2027, 11, 23),
        "purchase_cost": Decimal("102.01"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # A TO Z TAB
    p_id_455 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000454")
    products[p_id_455] = {
        "id": p_id_455,
        "code": "MED-ATOZTAB",
        "name": 'A TO Z TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("282.98"),
        "default_purchase_price": Decimal("226.38"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_455 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000455")
    batches[b_id_455] = {
        "id": b_id_455,
        "product_id": p_id_455,
        "batch_number": "BCH-MEDATO-28",
        "expiry_date": date(2028, 12, 24),
        "purchase_cost": Decimal("226.38"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # CLAVAM FORTE DRY SYRUP 30ML
    p_id_456 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000455")
    products[p_id_456] = {
        "id": p_id_456,
        "code": "MED-CLAVAMFO",
        "name": 'CLAVAM FORTE DRY SYRUP 30ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("176.49"),
        "default_purchase_price": Decimal("141.19"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_456 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000456")
    batches[b_id_456] = {
        "id": b_id_456,
        "product_id": p_id_456,
        "batch_number": "BCH-MEDCLA-27",
        "expiry_date": date(2027, 1, 25),
        "purchase_cost": Decimal("141.19"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # ROVAS 20TAB
    p_id_457 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000456")
    products[p_id_457] = {
        "id": p_id_457,
        "code": "MED-ROVAS20T",
        "name": 'ROVAS 20TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("537.88"),
        "default_purchase_price": Decimal("430.30"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_457 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000457")
    batches[b_id_457] = {
        "id": b_id_457,
        "product_id": p_id_457,
        "batch_number": "BCH-MEDROV-28",
        "expiry_date": date(2028, 2, 26),
        "purchase_cost": Decimal("430.30"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # LOSPO 50MG TAB
    p_id_458 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000457")
    products[p_id_458] = {
        "id": p_id_458,
        "code": "MED-LOSPO50M",
        "name": 'LOSPO 50MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("107.75"),
        "default_purchase_price": Decimal("86.20"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_458 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000458")
    batches[b_id_458] = {
        "id": b_id_458,
        "product_id": p_id_458,
        "batch_number": "BCH-MEDLOS-27",
        "expiry_date": date(2027, 3, 27),
        "purchase_cost": Decimal("86.20"),
        "quantity": 18,
        "is_active": True,
        "created_at": now,
    }

    # RAZO 20MG TAB
    p_id_459 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000458")
    products[p_id_459] = {
        "id": p_id_459,
        "code": "MED-RAZO20MG",
        "name": 'RAZO 20MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("440.48"),
        "default_purchase_price": Decimal("352.38"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_459 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000459")
    batches[b_id_459] = {
        "id": b_id_459,
        "product_id": p_id_459,
        "batch_number": "BCH-MEDRAZ-28",
        "expiry_date": date(2028, 4, 1),
        "purchase_cost": Decimal("352.38"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ROVASTIN 10 MG TAB
    p_id_460 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000459")
    products[p_id_460] = {
        "id": p_id_460,
        "code": "MED-ROVASTIN",
        "name": 'ROVASTIN 10 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("294.97"),
        "default_purchase_price": Decimal("235.98"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_460 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000460")
    batches[b_id_460] = {
        "id": b_id_460,
        "product_id": p_id_460,
        "batch_number": "BCH-MEDROV-27",
        "expiry_date": date(2027, 5, 2),
        "purchase_cost": Decimal("235.98"),
        "quantity": 35,
        "is_active": True,
        "created_at": now,
    }

    # TELSARTAN 20 MG
    p_id_461 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000460")
    products[p_id_461] = {
        "id": p_id_461,
        "code": "MED-TELSARTA-2",
        "name": 'TELSARTAN 20 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("71.41"),
        "default_purchase_price": Decimal("57.13"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_461 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000461")
    batches[b_id_461] = {
        "id": b_id_461,
        "product_id": p_id_461,
        "batch_number": "BCH-MEDTEL-28",
        "expiry_date": date(2028, 6, 3),
        "purchase_cost": Decimal("57.13"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TENEPRIDE 20 MG TABLET
    p_id_462 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000461")
    products[p_id_462] = {
        "id": p_id_462,
        "code": "MED-TENEPRID",
        "name": 'TENEPRIDE 20 MG TABLET',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("294.73"),
        "default_purchase_price": Decimal("235.78"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_462 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000462")
    batches[b_id_462] = {
        "id": b_id_462,
        "product_id": p_id_462,
        "batch_number": "BCH-MEDTEN-27",
        "expiry_date": date(2027, 7, 4),
        "purchase_cost": Decimal("235.78"),
        "quantity": 25,
        "is_active": True,
        "created_at": now,
    }

    # LUPILA 10MG TAB
    p_id_463 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000462")
    products[p_id_463] = {
        "id": p_id_463,
        "code": "MED-LUPILA10",
        "name": 'LUPILA 10MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("336.45"),
        "default_purchase_price": Decimal("269.16"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_463 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000463")
    batches[b_id_463] = {
        "id": b_id_463,
        "product_id": p_id_463,
        "batch_number": "BCH-MEDLUP-28",
        "expiry_date": date(2028, 8, 5),
        "purchase_cost": Decimal("269.16"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # CANDITRAL-SB 130MG TAB
    p_id_464 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000463")
    products[p_id_464] = {
        "id": p_id_464,
        "code": "MED-CANDITRA",
        "name": 'CANDITRAL-SB 130MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("498.66"),
        "default_purchase_price": Decimal("398.93"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_464 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000464")
    batches[b_id_464] = {
        "id": b_id_464,
        "product_id": p_id_464,
        "batch_number": "BCH-MEDCAN-27",
        "expiry_date": date(2027, 9, 6),
        "purchase_cost": Decimal("398.93"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # ALEX+PED DROP 15ML
    p_id_465 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000464")
    products[p_id_465] = {
        "id": p_id_465,
        "code": "MED-ALEXPEDD",
        "name": 'ALEX+PED DROP 15ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("111.12"),
        "default_purchase_price": Decimal("88.90"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_465 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000465")
    batches[b_id_465] = {
        "id": b_id_465,
        "product_id": p_id_465,
        "batch_number": "BCH-MEDALE-28",
        "expiry_date": date(2028, 10, 7),
        "purchase_cost": Decimal("88.90"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # LOSAP-H TAB
    p_id_466 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000465")
    products[p_id_466] = {
        "id": p_id_466,
        "code": "MED-LOSAPHTA",
        "name": 'LOSAP-H TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("213.50"),
        "default_purchase_price": Decimal("170.80"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_466 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000466")
    batches[b_id_466] = {
        "id": b_id_466,
        "product_id": p_id_466,
        "batch_number": "BCH-MEDLOS-27",
        "expiry_date": date(2027, 11, 8),
        "purchase_cost": Decimal("170.80"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # MELMET 1000MG SR TAB
    p_id_467 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000466")
    products[p_id_467] = {
        "id": p_id_467,
        "code": "MED-MELMET10",
        "name": 'MELMET 1000MG SR TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("111.08"),
        "default_purchase_price": Decimal("88.86"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_467 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000467")
    batches[b_id_467] = {
        "id": b_id_467,
        "product_id": p_id_467,
        "batch_number": "BCH-MEDMEL-28",
        "expiry_date": date(2028, 12, 9),
        "purchase_cost": Decimal("88.86"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # PANTOTAB DSR TAB
    p_id_468 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000467")
    products[p_id_468] = {
        "id": p_id_468,
        "code": "MED-PANTOTAB",
        "name": 'PANTOTAB DSR TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("277.76"),
        "default_purchase_price": Decimal("222.21"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_468 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000468")
    batches[b_id_468] = {
        "id": b_id_468,
        "product_id": p_id_468,
        "batch_number": "BCH-MEDPAN-27",
        "expiry_date": date(2027, 1, 10),
        "purchase_cost": Decimal("222.21"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TURBOVAS-10 MG TAB
    p_id_469 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000468")
    products[p_id_469] = {
        "id": p_id_469,
        "code": "MED-TURBOVAS-1",
        "name": 'TURBOVAS-10 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("383.71"),
        "default_purchase_price": Decimal("306.97"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_469 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000469")
    batches[b_id_469] = {
        "id": b_id_469,
        "product_id": p_id_469,
        "batch_number": "BCH-MEDTUR-28",
        "expiry_date": date(2028, 2, 11),
        "purchase_cost": Decimal("306.97"),
        "quantity": 17,
        "is_active": True,
        "created_at": now,
    }

    # M-BACT 5GM
    p_id_470 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000469")
    products[p_id_470] = {
        "id": p_id_470,
        "code": "MED-MBACT5GM",
        "name": 'M-BACT 5GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("87.81"),
        "default_purchase_price": Decimal("70.25"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_470 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000470")
    batches[b_id_470] = {
        "id": b_id_470,
        "product_id": p_id_470,
        "batch_number": "BCH-MEDMBA-27",
        "expiry_date": date(2027, 3, 12),
        "purchase_cost": Decimal("70.25"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # TRIPLIN 25MG TAB
    p_id_471 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000470")
    products[p_id_471] = {
        "id": p_id_471,
        "code": "MED-TRIPLIN2",
        "name": 'TRIPLIN 25MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("53.92"),
        "default_purchase_price": Decimal("43.14"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_471 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000471")
    batches[b_id_471] = {
        "id": b_id_471,
        "product_id": p_id_471,
        "batch_number": "BCH-MEDTRI-28",
        "expiry_date": date(2028, 4, 13),
        "purchase_cost": Decimal("43.14"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # GLIDE 5MG TAB
    p_id_472 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000471")
    products[p_id_472] = {
        "id": p_id_472,
        "code": "MED-GLIDE5MG",
        "name": 'GLIDE 5MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("14.71"),
        "default_purchase_price": Decimal("11.77"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_472 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000472")
    batches[b_id_472] = {
        "id": b_id_472,
        "product_id": p_id_472,
        "batch_number": "BCH-MEDGLI-27",
        "expiry_date": date(2027, 5, 14),
        "purchase_cost": Decimal("11.77"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # microcef-200 dt tab
    p_id_473 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000472")
    products[p_id_473] = {
        "id": p_id_473,
        "code": "MED-MICROCEF",
        "name": 'microcef-200 dt tab',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("217.11"),
        "default_purchase_price": Decimal("173.69"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_473 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000473")
    batches[b_id_473] = {
        "id": b_id_473,
        "product_id": p_id_473,
        "batch_number": "BCH-MEDMIC-28",
        "expiry_date": date(2028, 6, 15),
        "purchase_cost": Decimal("173.69"),
        "quantity": 30,
        "is_active": True,
        "created_at": now,
    }

    # PANDOM -DSR
    p_id_474 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000473")
    products[p_id_474] = {
        "id": p_id_474,
        "code": "MED-PANDOMDS",
        "name": 'PANDOM -DSR',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("162.45"),
        "default_purchase_price": Decimal("129.96"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_474 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000474")
    batches[b_id_474] = {
        "id": b_id_474,
        "product_id": p_id_474,
        "batch_number": "BCH-MEDPAN-27",
        "expiry_date": date(2027, 7, 16),
        "purchase_cost": Decimal("129.96"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # FLUDAC 20MG TAB
    p_id_475 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000474")
    products[p_id_475] = {
        "id": p_id_475,
        "code": "MED-FLUDAC20",
        "name": 'FLUDAC 20MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("103.75"),
        "default_purchase_price": Decimal("83.00"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_475 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000475")
    batches[b_id_475] = {
        "id": b_id_475,
        "product_id": p_id_475,
        "batch_number": "BCH-MEDFLU-28",
        "expiry_date": date(2028, 8, 17),
        "purchase_cost": Decimal("83.00"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # PANCARE DSR CAP
    p_id_476 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000475")
    products[p_id_476] = {
        "id": p_id_476,
        "code": "MED-PANCARED",
        "name": 'PANCARE DSR CAP',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("140.91"),
        "default_purchase_price": Decimal("112.73"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_476 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000476")
    batches[b_id_476] = {
        "id": b_id_476,
        "product_id": p_id_476,
        "batch_number": "BCH-MEDPAN-27",
        "expiry_date": date(2027, 9, 18),
        "purchase_cost": Decimal("112.73"),
        "quantity": 48,
        "is_active": True,
        "created_at": now,
    }

    # ROVASTIN 20 TAB
    p_id_477 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000476")
    products[p_id_477] = {
        "id": p_id_477,
        "code": "MED-ROVASTIN-1",
        "name": 'ROVASTIN 20 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("512.14"),
        "default_purchase_price": Decimal("409.71"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_477 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000477")
    batches[b_id_477] = {
        "id": b_id_477,
        "product_id": p_id_477,
        "batch_number": "BCH-MEDROV-28",
        "expiry_date": date(2028, 10, 19),
        "purchase_cost": Decimal("409.71"),
        "quantity": 18,
        "is_active": True,
        "created_at": now,
    }

    # HYTIDE 12.5 TAB
    p_id_478 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000477")
    products[p_id_478] = {
        "id": p_id_478,
        "code": "MED-HYTIDE12",
        "name": 'HYTIDE 12.5 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("29.57"),
        "default_purchase_price": Decimal("23.66"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_478 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000478")
    batches[b_id_478] = {
        "id": b_id_478,
        "product_id": p_id_478,
        "batch_number": "BCH-MEDHYT-27",
        "expiry_date": date(2027, 11, 20),
        "purchase_cost": Decimal("23.66"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # FRUSIX 40MG TAB
    p_id_479 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000478")
    products[p_id_479] = {
        "id": p_id_479,
        "code": "MED-FRUSIX40",
        "name": 'FRUSIX 40MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("61.24"),
        "default_purchase_price": Decimal("48.99"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_479 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000479")
    batches[b_id_479] = {
        "id": b_id_479,
        "product_id": p_id_479,
        "batch_number": "BCH-MEDFRU-28",
        "expiry_date": date(2028, 12, 21),
        "purchase_cost": Decimal("48.99"),
        "quantity": 1,
        "is_active": True,
        "created_at": now,
    }

    # FUNGITOP-150 CAP
    p_id_480 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000479")
    products[p_id_480] = {
        "id": p_id_480,
        "code": "MED-FUNGITOP",
        "name": 'FUNGITOP-150 CAP',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("20.69"),
        "default_purchase_price": Decimal("16.55"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_480 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000480")
    batches[b_id_480] = {
        "id": b_id_480,
        "product_id": p_id_480,
        "batch_number": "BCH-MEDFUN-27",
        "expiry_date": date(2027, 1, 22),
        "purchase_cost": Decimal("16.55"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # LOSIUM-H TAB
    p_id_481 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000480")
    products[p_id_481] = {
        "id": p_id_481,
        "code": "MED-LOSIUMHT",
        "name": 'LOSIUM-H TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("550.36"),
        "default_purchase_price": Decimal("440.29"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_481 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000481")
    batches[b_id_481] = {
        "id": b_id_481,
        "product_id": p_id_481,
        "batch_number": "BCH-MEDLOS-28",
        "expiry_date": date(2028, 2, 23),
        "purchase_cost": Decimal("440.29"),
        "quantity": 1,
        "is_active": True,
        "created_at": now,
    }

    # ANGICAM 5MG TAB
    p_id_482 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000481")
    products[p_id_482] = {
        "id": p_id_482,
        "code": "MED-ANGICAM5",
        "name": 'ANGICAM 5MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("40.51"),
        "default_purchase_price": Decimal("32.41"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_482 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000482")
    batches[b_id_482] = {
        "id": b_id_482,
        "product_id": p_id_482,
        "batch_number": "BCH-MEDANG-27",
        "expiry_date": date(2027, 3, 24),
        "purchase_cost": Decimal("32.41"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # METFOR GP2 FORTE TAB
    p_id_483 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000482")
    products[p_id_483] = {
        "id": p_id_483,
        "code": "MED-METFORGP",
        "name": 'METFOR GP2 FORTE TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("146.88"),
        "default_purchase_price": Decimal("117.50"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_483 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000483")
    batches[b_id_483] = {
        "id": b_id_483,
        "product_id": p_id_483,
        "batch_number": "BCH-MEDMET-28",
        "expiry_date": date(2028, 4, 25),
        "purchase_cost": Decimal("117.50"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # PRAN 10MG TAB
    p_id_484 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000483")
    products[p_id_484] = {
        "id": p_id_484,
        "code": "MED-PRAN10MG",
        "name": 'PRAN 10MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("35.56"),
        "default_purchase_price": Decimal("28.45"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_484 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000484")
    batches[b_id_484] = {
        "id": b_id_484,
        "product_id": p_id_484,
        "batch_number": "BCH-MEDPRA-27",
        "expiry_date": date(2027, 5, 26),
        "purchase_cost": Decimal("28.45"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # SEROPRAM 10 MG
    p_id_485 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000484")
    products[p_id_485] = {
        "id": p_id_485,
        "code": "MED-SEROPRAM",
        "name": 'SEROPRAM 10 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("122.40"),
        "default_purchase_price": Decimal("97.92"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_485 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000485")
    batches[b_id_485] = {
        "id": b_id_485,
        "product_id": p_id_485,
        "batch_number": "BCH-MEDSER-28",
        "expiry_date": date(2028, 6, 27),
        "purchase_cost": Decimal("97.92"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # METFOR G2
    p_id_486 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000485")
    products[p_id_486] = {
        "id": p_id_486,
        "code": "MED-METFORG2",
        "name": 'METFOR G2',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("148.69"),
        "default_purchase_price": Decimal("118.95"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_486 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000486")
    batches[b_id_486] = {
        "id": b_id_486,
        "product_id": p_id_486,
        "batch_number": "BCH-MEDMET-27",
        "expiry_date": date(2027, 7, 1),
        "purchase_cost": Decimal("118.95"),
        "quantity": 30,
        "is_active": True,
        "created_at": now,
    }

    # ROVAS 10 MG TAB
    p_id_487 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000486")
    products[p_id_487] = {
        "id": p_id_487,
        "code": "MED-ROVAS10M",
        "name": 'ROVAS 10 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("304.84"),
        "default_purchase_price": Decimal("243.87"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_487 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000487")
    batches[b_id_487] = {
        "id": b_id_487,
        "product_id": p_id_487,
        "batch_number": "BCH-MEDROV-28",
        "expiry_date": date(2028, 8, 2),
        "purchase_cost": Decimal("243.87"),
        "quantity": 44,
        "is_active": True,
        "created_at": now,
    }

    # ROVAS 5 MG TAB
    p_id_488 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000487")
    products[p_id_488] = {
        "id": p_id_488,
        "code": "MED-ROVAS5MG",
        "name": 'ROVAS 5 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("182.33"),
        "default_purchase_price": Decimal("145.86"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_488 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000488")
    batches[b_id_488] = {
        "id": b_id_488,
        "product_id": p_id_488,
        "batch_number": "BCH-MEDROV-27",
        "expiry_date": date(2027, 9, 3),
        "purchase_cost": Decimal("145.86"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # FINAST 5 MG TAB
    p_id_489 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000488")
    products[p_id_489] = {
        "id": p_id_489,
        "code": "MED-FINAST5M",
        "name": 'FINAST 5 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("1052.54"),
        "default_purchase_price": Decimal("842.03"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_489 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000489")
    batches[b_id_489] = {
        "id": b_id_489,
        "product_id": p_id_489,
        "batch_number": "BCH-MEDFIN-28",
        "expiry_date": date(2028, 10, 4),
        "purchase_cost": Decimal("842.03"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # AMLOTAN 55 MG TAB
    p_id_490 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000489")
    products[p_id_490] = {
        "id": p_id_490,
        "code": "MED-AMLOTAN5",
        "name": 'AMLOTAN 55 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("134.76"),
        "default_purchase_price": Decimal("107.81"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_490 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000490")
    batches[b_id_490] = {
        "id": b_id_490,
        "product_id": p_id_490,
        "batch_number": "BCH-MEDAML-27",
        "expiry_date": date(2027, 11, 5),
        "purchase_cost": Decimal("107.81"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # OLMAT 40 MG TAB
    p_id_491 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000490")
    products[p_id_491] = {
        "id": p_id_491,
        "code": "MED-OLMAT40M",
        "name": 'OLMAT 40 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("577.94"),
        "default_purchase_price": Decimal("462.35"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_491 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000491")
    batches[b_id_491] = {
        "id": b_id_491,
        "product_id": p_id_491,
        "batch_number": "BCH-MEDOLM-28",
        "expiry_date": date(2028, 12, 6),
        "purchase_cost": Decimal("462.35"),
        "quantity": 7,
        "is_active": True,
        "created_at": now,
    }

    # CARBOTRAP-25MG TAB
    p_id_492 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000491")
    products[p_id_492] = {
        "id": p_id_492,
        "code": "MED-CARBOTRA",
        "name": 'CARBOTRAP-25MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("310.99"),
        "default_purchase_price": Decimal("248.79"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_492 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000492")
    batches[b_id_492] = {
        "id": b_id_492,
        "product_id": p_id_492,
        "batch_number": "BCH-MEDCAR-27",
        "expiry_date": date(2027, 1, 7),
        "purchase_cost": Decimal("248.79"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # PANTOP-D TAB
    p_id_493 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000492")
    products[p_id_493] = {
        "id": p_id_493,
        "code": "MED-PANTOPDT",
        "name": 'PANTOP-D TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("134.77"),
        "default_purchase_price": Decimal("107.82"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_493 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000493")
    batches[b_id_493] = {
        "id": b_id_493,
        "product_id": p_id_493,
        "batch_number": "BCH-MEDPAN-28",
        "expiry_date": date(2028, 2, 8),
        "purchase_cost": Decimal("107.82"),
        "quantity": 60,
        "is_active": True,
        "created_at": now,
    }

    # SIPTIN -M 850 MG TAB
    p_id_494 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000493")
    products[p_id_494] = {
        "id": p_id_494,
        "code": "MED-SIPTINM8",
        "name": 'SIPTIN -M 850 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("276.84"),
        "default_purchase_price": Decimal("221.47"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_494 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000494")
    batches[b_id_494] = {
        "id": b_id_494,
        "product_id": p_id_494,
        "batch_number": "BCH-MEDSIP-27",
        "expiry_date": date(2027, 3, 9),
        "purchase_cost": Decimal("221.47"),
        "quantity": 9,
        "is_active": True,
        "created_at": now,
    }

    # AMLOSAFE AT TAB
    p_id_495 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000494")
    products[p_id_495] = {
        "id": p_id_495,
        "code": "MED-AMLOSAFE-1",
        "name": 'AMLOSAFE AT TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("131.11"),
        "default_purchase_price": Decimal("104.89"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_495 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000495")
    batches[b_id_495] = {
        "id": b_id_495,
        "product_id": p_id_495,
        "batch_number": "BCH-MEDAML-28",
        "expiry_date": date(2028, 4, 10),
        "purchase_cost": Decimal("104.89"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # SYP ASCORIL BT (SSF)
    p_id_496 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000495")
    products[p_id_496] = {
        "id": p_id_496,
        "code": "MED-SYPASCOR",
        "name": 'SYP ASCORIL BT (SSF)',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("153.62"),
        "default_purchase_price": Decimal("122.90"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_496 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000496")
    batches[b_id_496] = {
        "id": b_id_496,
        "product_id": p_id_496,
        "batch_number": "BCH-MEDSYP-27",
        "expiry_date": date(2027, 5, 11),
        "purchase_cost": Decimal("122.90"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB LEVOCET 5 MG
    p_id_497 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000496")
    products[p_id_497] = {
        "id": p_id_497,
        "code": "MED-TABLEVOC",
        "name": 'TAB LEVOCET 5 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("52.02"),
        "default_purchase_price": Decimal("41.62"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_497 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000497")
    batches[b_id_497] = {
        "id": b_id_497,
        "product_id": p_id_497,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 12),
        "purchase_cost": Decimal("41.62"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # VEGAMIN P 1500 CAP
    p_id_498 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000497")
    products[p_id_498] = {
        "id": p_id_498,
        "code": "MED-VEGAMINP",
        "name": 'VEGAMIN P 1500 CAP',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("326.44"),
        "default_purchase_price": Decimal("261.15"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_498 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000498")
    batches[b_id_498] = {
        "id": b_id_498,
        "product_id": p_id_498,
        "batch_number": "BCH-MEDVEG-27",
        "expiry_date": date(2027, 7, 13),
        "purchase_cost": Decimal("261.15"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB LIPTA 5
    p_id_499 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000498")
    products[p_id_499] = {
        "id": p_id_499,
        "code": "MED-TABLIPTA",
        "name": 'TAB LIPTA 5',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("296.98"),
        "default_purchase_price": Decimal("237.58"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_499 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000499")
    batches[b_id_499] = {
        "id": b_id_499,
        "product_id": p_id_499,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 14),
        "purchase_cost": Decimal("237.58"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ASTAT 10 MG
    p_id_500 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000499")
    products[p_id_500] = {
        "id": p_id_500,
        "code": "MED-ASTAT10M",
        "name": 'ASTAT 10 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("110.61"),
        "default_purchase_price": Decimal("88.49"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_500 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000500")
    batches[b_id_500] = {
        "id": b_id_500,
        "product_id": p_id_500,
        "batch_number": "BCH-MEDAST-27",
        "expiry_date": date(2027, 9, 15),
        "purchase_cost": Decimal("88.49"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # NEUROGARD P 50
    p_id_501 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000500")
    products[p_id_501] = {
        "id": p_id_501,
        "code": "MED-NEUROGAR",
        "name": 'NEUROGARD P 50',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("286.10"),
        "default_purchase_price": Decimal("228.88"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_501 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000501")
    batches[b_id_501] = {
        "id": b_id_501,
        "product_id": p_id_501,
        "batch_number": "BCH-MEDNEU-28",
        "expiry_date": date(2028, 10, 16),
        "purchase_cost": Decimal("228.88"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # NEUROGARD P 75
    p_id_502 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000501")
    products[p_id_502] = {
        "id": p_id_502,
        "code": "MED-NEUROGAR-1",
        "name": 'NEUROGARD P 75',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("326.96"),
        "default_purchase_price": Decimal("261.57"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_502 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000502")
    batches[b_id_502] = {
        "id": b_id_502,
        "product_id": p_id_502,
        "batch_number": "BCH-MEDNEU-27",
        "expiry_date": date(2027, 11, 17),
        "purchase_cost": Decimal("261.57"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ICON CAP 100mg
    p_id_503 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000502")
    products[p_id_503] = {
        "id": p_id_503,
        "code": "MED-ICONCAP1",
        "name": 'ICON CAP 100mg',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("157.20"),
        "default_purchase_price": Decimal("125.76"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_503 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000503")
    batches[b_id_503] = {
        "id": b_id_503,
        "product_id": p_id_503,
        "batch_number": "BCH-MEDICO-28",
        "expiry_date": date(2028, 12, 18),
        "purchase_cost": Decimal("125.76"),
        "quantity": 36,
        "is_active": True,
        "created_at": now,
    }

    # SYP TRICANE MPS
    p_id_504 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000503")
    products[p_id_504] = {
        "id": p_id_504,
        "code": "MED-SYPTRICA",
        "name": 'SYP TRICANE MPS',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("143.78"),
        "default_purchase_price": Decimal("115.02"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_504 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000504")
    batches[b_id_504] = {
        "id": b_id_504,
        "product_id": p_id_504,
        "batch_number": "BCH-MEDSYP-27",
        "expiry_date": date(2027, 1, 19),
        "purchase_cost": Decimal("115.02"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # MONTINA L
    p_id_505 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000504")
    products[p_id_505] = {
        "id": p_id_505,
        "code": "MED-MONTINAL",
        "name": 'MONTINA L',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("122.88"),
        "default_purchase_price": Decimal("98.30"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_505 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000505")
    batches[b_id_505] = {
        "id": b_id_505,
        "product_id": p_id_505,
        "batch_number": "BCH-MEDMON-28",
        "expiry_date": date(2028, 2, 20),
        "purchase_cost": Decimal("98.30"),
        "quantity": 19,
        "is_active": True,
        "created_at": now,
    }

    # NIMS TAB
    p_id_506 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000505")
    products[p_id_506] = {
        "id": p_id_506,
        "code": "MED-NIMSTAB",
        "name": 'NIMS TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("36.49"),
        "default_purchase_price": Decimal("29.19"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_506 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000506")
    batches[b_id_506] = {
        "id": b_id_506,
        "product_id": p_id_506,
        "batch_number": "BCH-MEDNIM-27",
        "expiry_date": date(2027, 3, 21),
        "purchase_cost": Decimal("29.19"),
        "quantity": 48,
        "is_active": True,
        "created_at": now,
    }

    # NETFORMIN-G1 TAB
    p_id_507 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000506")
    products[p_id_507] = {
        "id": p_id_507,
        "code": "MED-NETFORMI-1",
        "name": 'NETFORMIN-G1 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("91.39"),
        "default_purchase_price": Decimal("73.11"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_507 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000507")
    batches[b_id_507] = {
        "id": b_id_507,
        "product_id": p_id_507,
        "batch_number": "BCH-MEDNET-28",
        "expiry_date": date(2028, 4, 22),
        "purchase_cost": Decimal("73.11"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # CLAVAM 625 MG
    p_id_508 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000507")
    products[p_id_508] = {
        "id": p_id_508,
        "code": "MED-CLAVAM62",
        "name": 'CLAVAM 625 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("111.62"),
        "default_purchase_price": Decimal("89.30"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_508 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000508")
    batches[b_id_508] = {
        "id": b_id_508,
        "product_id": p_id_508,
        "batch_number": "BCH-MEDCLA-27",
        "expiry_date": date(2027, 5, 23),
        "purchase_cost": Decimal("89.30"),
        "quantity": 33,
        "is_active": True,
        "created_at": now,
    }

    # MEFTAL -SPAS TAB
    p_id_509 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000508")
    products[p_id_509] = {
        "id": p_id_509,
        "code": "MED-MEFTALSP-1",
        "name": 'MEFTAL -SPAS TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("82.56"),
        "default_purchase_price": Decimal("66.05"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_509 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000509")
    batches[b_id_509] = {
        "id": b_id_509,
        "product_id": p_id_509,
        "batch_number": "BCH-MEDMEF-28",
        "expiry_date": date(2028, 6, 24),
        "purchase_cost": Decimal("66.05"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # CHX ORAL RINSE
    p_id_510 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000509")
    products[p_id_510] = {
        "id": p_id_510,
        "code": "MED-CHXORALR",
        "name": 'CHX ORAL RINSE',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("86.40"),
        "default_purchase_price": Decimal("69.12"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_510 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000510")
    batches[b_id_510] = {
        "id": b_id_510,
        "product_id": p_id_510,
        "batch_number": "BCH-MEDCHX-27",
        "expiry_date": date(2027, 7, 25),
        "purchase_cost": Decimal("69.12"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # ULGEL-ELICHI 200ML
    p_id_511 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000510")
    products[p_id_511] = {
        "id": p_id_511,
        "code": "MED-ULGELELI",
        "name": 'ULGEL-ELICHI 200ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("220.65"),
        "default_purchase_price": Decimal("176.52"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_511 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000511")
    batches[b_id_511] = {
        "id": b_id_511,
        "product_id": p_id_511,
        "batch_number": "BCH-MEDULG-28",
        "expiry_date": date(2028, 8, 26),
        "purchase_cost": Decimal("176.52"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB DEZACOR 6MG
    p_id_512 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000511")
    products[p_id_512] = {
        "id": p_id_512,
        "code": "MED-TABDEZAC",
        "name": 'TAB DEZACOR 6MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("250.97"),
        "default_purchase_price": Decimal("200.78"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_512 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000512")
    batches[b_id_512] = {
        "id": b_id_512,
        "product_id": p_id_512,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 27),
        "purchase_cost": Decimal("200.78"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB TORSINEX 20MG
    p_id_513 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000512")
    products[p_id_513] = {
        "id": p_id_513,
        "code": "MED-TABTORSI",
        "name": 'TAB TORSINEX 20MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("172.04"),
        "default_purchase_price": Decimal("137.63"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_513 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000513")
    batches[b_id_513] = {
        "id": b_id_513,
        "product_id": p_id_513,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 1),
        "purchase_cost": Decimal("137.63"),
        "quantity": 17,
        "is_active": True,
        "created_at": now,
    }

    # TUSQ-X 100ML
    p_id_514 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000513")
    products[p_id_514] = {
        "id": p_id_514,
        "code": "MED-TUSQX100",
        "name": 'TUSQ-X 100ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("140.09"),
        "default_purchase_price": Decimal("112.07"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_514 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000514")
    batches[b_id_514] = {
        "id": b_id_514,
        "product_id": p_id_514,
        "batch_number": "BCH-MEDTUS-27",
        "expiry_date": date(2027, 11, 2),
        "purchase_cost": Decimal("112.07"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # RITE O CEF-100MG TAB
    p_id_515 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000514")
    products[p_id_515] = {
        "id": p_id_515,
        "code": "MED-RITEOCEF",
        "name": 'RITE O CEF-100MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("114.08"),
        "default_purchase_price": Decimal("91.26"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_515 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000515")
    batches[b_id_515] = {
        "id": b_id_515,
        "product_id": p_id_515,
        "batch_number": "BCH-MEDRIT-28",
        "expiry_date": date(2028, 12, 3),
        "purchase_cost": Decimal("91.26"),
        "quantity": 24,
        "is_active": True,
        "created_at": now,
    }

    # XONE 1GM INJ
    p_id_516 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000515")
    products[p_id_516] = {
        "id": p_id_516,
        "code": "MED-XONE1GMI",
        "name": 'XONE 1GM INJ',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("43.36"),
        "default_purchase_price": Decimal("34.69"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_516 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000516")
    batches[b_id_516] = {
        "id": b_id_516,
        "product_id": p_id_516,
        "batch_number": "BCH-MEDXON-27",
        "expiry_date": date(2027, 1, 4),
        "purchase_cost": Decimal("34.69"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # ROSEDAY 20MG
    p_id_517 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000516")
    products[p_id_517] = {
        "id": p_id_517,
        "code": "MED-ROSEDAY2",
        "name": 'ROSEDAY 20MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("702.60"),
        "default_purchase_price": Decimal("562.08"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_517 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000517")
    batches[b_id_517] = {
        "id": b_id_517,
        "product_id": p_id_517,
        "batch_number": "BCH-MEDROS-28",
        "expiry_date": date(2028, 2, 5),
        "purchase_cost": Decimal("562.08"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TELSARTAN 40MG
    p_id_518 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000517")
    products[p_id_518] = {
        "id": p_id_518,
        "code": "MED-TELSARTA-3",
        "name": 'TELSARTAN 40MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("134.66"),
        "default_purchase_price": Decimal("107.73"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_518 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000518")
    batches[b_id_518] = {
        "id": b_id_518,
        "product_id": p_id_518,
        "batch_number": "BCH-MEDTEL-27",
        "expiry_date": date(2027, 3, 6),
        "purchase_cost": Decimal("107.73"),
        "quantity": 30,
        "is_active": True,
        "created_at": now,
    }

    # CAP DV60K
    p_id_519 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000518")
    products[p_id_519] = {
        "id": p_id_519,
        "code": "MED-CAPDV60K",
        "name": 'CAP DV60K',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("607.09"),
        "default_purchase_price": Decimal("485.67"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_519 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000519")
    batches[b_id_519] = {
        "id": b_id_519,
        "product_id": p_id_519,
        "batch_number": "BCH-MEDCAP-28",
        "expiry_date": date(2028, 4, 7),
        "purchase_cost": Decimal("485.67"),
        "quantity": 7,
        "is_active": True,
        "created_at": now,
    }

    # ES - PRAM 5 MG TAB
    p_id_520 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000519")
    products[p_id_520] = {
        "id": p_id_520,
        "code": "MED-ESPRAM5M",
        "name": 'ES - PRAM 5 MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("101.50"),
        "default_purchase_price": Decimal("81.20"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_520 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000520")
    batches[b_id_520] = {
        "id": b_id_520,
        "product_id": p_id_520,
        "batch_number": "BCH-MEDESP-27",
        "expiry_date": date(2027, 5, 8),
        "purchase_cost": Decimal("81.20"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # VONAPRO 20MG TAB
    p_id_521 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000520")
    products[p_id_521] = {
        "id": p_id_521,
        "code": "MED-VONAPRO2",
        "name": 'VONAPRO 20MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("306.54"),
        "default_purchase_price": Decimal("245.23"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_521 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000521")
    batches[b_id_521] = {
        "id": b_id_521,
        "product_id": p_id_521,
        "batch_number": "BCH-MEDVON-28",
        "expiry_date": date(2028, 6, 9),
        "purchase_cost": Decimal("245.23"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # ATENOL 50MG TAB
    p_id_522 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000521")
    products[p_id_522] = {
        "id": p_id_522,
        "code": "MED-ATENOL50",
        "name": 'ATENOL 50MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("61.24"),
        "default_purchase_price": Decimal("48.99"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_522 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000522")
    batches[b_id_522] = {
        "id": b_id_522,
        "product_id": p_id_522,
        "batch_number": "BCH-MEDATE-27",
        "expiry_date": date(2027, 7, 10),
        "purchase_cost": Decimal("48.99"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # VOBOSE 0.3 TAB
    p_id_523 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000522")
    products[p_id_523] = {
        "id": p_id_523,
        "code": "MED-VOBOSE03",
        "name": 'VOBOSE 0.3 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("278.94"),
        "default_purchase_price": Decimal("223.15"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_523 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000523")
    batches[b_id_523] = {
        "id": b_id_523,
        "product_id": p_id_523,
        "batch_number": "BCH-MEDVOB-28",
        "expiry_date": date(2028, 8, 11),
        "purchase_cost": Decimal("223.15"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # OLMAT 20MG TAB
    p_id_524 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000523")
    products[p_id_524] = {
        "id": p_id_524,
        "code": "MED-OLMAT20M",
        "name": 'OLMAT 20MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("336.73"),
        "default_purchase_price": Decimal("269.38"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_524 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000524")
    batches[b_id_524] = {
        "id": b_id_524,
        "product_id": p_id_524,
        "batch_number": "BCH-MEDOLM-27",
        "expiry_date": date(2027, 9, 12),
        "purchase_cost": Decimal("269.38"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # VOBOSE 0.2MG TAB
    p_id_525 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000524")
    products[p_id_525] = {
        "id": p_id_525,
        "code": "MED-VOBOSE02",
        "name": 'VOBOSE 0.2MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("209.10"),
        "default_purchase_price": Decimal("167.28"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_525 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000525")
    batches[b_id_525] = {
        "id": b_id_525,
        "product_id": p_id_525,
        "batch_number": "BCH-MEDVOB-28",
        "expiry_date": date(2028, 10, 13),
        "purchase_cost": Decimal("167.28"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # AMFAST 2.5MG TAB
    p_id_526 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000525")
    products[p_id_526] = {
        "id": p_id_526,
        "code": "MED-AMFAST25",
        "name": 'AMFAST 2.5MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("23.49"),
        "default_purchase_price": Decimal("18.79"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_526 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000526")
    batches[b_id_526] = {
        "id": b_id_526,
        "product_id": p_id_526,
        "batch_number": "BCH-MEDAMF-27",
        "expiry_date": date(2027, 11, 14),
        "purchase_cost": Decimal("18.79"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # AMFAST LH TAB
    p_id_527 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000526")
    products[p_id_527] = {
        "id": p_id_527,
        "code": "MED-AMFASTLH",
        "name": 'AMFAST LH TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("136.22"),
        "default_purchase_price": Decimal("108.98"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_527 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000527")
    batches[b_id_527] = {
        "id": b_id_527,
        "product_id": p_id_527,
        "batch_number": "BCH-MEDAMF-28",
        "expiry_date": date(2028, 12, 15),
        "purchase_cost": Decimal("108.98"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # CORTILONE 30MG TAB
    p_id_528 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000527")
    products[p_id_528] = {
        "id": p_id_528,
        "code": "MED-CORTILON-4",
        "name": 'CORTILONE 30MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("121.31"),
        "default_purchase_price": Decimal("97.05"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_528 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000528")
    batches[b_id_528] = {
        "id": b_id_528,
        "product_id": p_id_528,
        "batch_number": "BCH-MEDCOR-27",
        "expiry_date": date(2027, 1, 16),
        "purchase_cost": Decimal("97.05"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # CEDON-100 DT
    p_id_529 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000528")
    products[p_id_529] = {
        "id": p_id_529,
        "code": "MED-CEDON100",
        "name": 'CEDON-100 DT',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("213.34"),
        "default_purchase_price": Decimal("170.67"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_529 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000529")
    batches[b_id_529] = {
        "id": b_id_529,
        "product_id": p_id_529,
        "batch_number": "BCH-MEDCED-28",
        "expiry_date": date(2028, 2, 17),
        "purchase_cost": Decimal("170.67"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # LEVOZIN 5MG TAB
    p_id_530 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000529")
    products[p_id_530] = {
        "id": p_id_530,
        "code": "MED-LEVOZIN5",
        "name": 'LEVOZIN 5MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("52.04"),
        "default_purchase_price": Decimal("41.63"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_530 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000530")
    batches[b_id_530] = {
        "id": b_id_530,
        "product_id": p_id_530,
        "batch_number": "BCH-MEDLEV-27",
        "expiry_date": date(2027, 3, 18),
        "purchase_cost": Decimal("41.63"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # CARBOTRAP 10MG TAB
    p_id_531 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000530")
    products[p_id_531] = {
        "id": p_id_531,
        "code": "MED-CARBOTRA-1",
        "name": 'CARBOTRAP 10MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("248.79"),
        "default_purchase_price": Decimal("199.03"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_531 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000531")
    batches[b_id_531] = {
        "id": b_id_531,
        "product_id": p_id_531,
        "batch_number": "BCH-MEDCAR-28",
        "expiry_date": date(2028, 4, 19),
        "purchase_cost": Decimal("199.03"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # HYOSPAN FORTE
    p_id_532 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000531")
    products[p_id_532] = {
        "id": p_id_532,
        "code": "MED-HYOSPANF",
        "name": 'HYOSPAN FORTE',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("232.49"),
        "default_purchase_price": Decimal("185.99"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_532 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000532")
    batches[b_id_532] = {
        "id": b_id_532,
        "product_id": p_id_532,
        "batch_number": "BCH-MEDHYO-27",
        "expiry_date": date(2027, 5, 20),
        "purchase_cost": Decimal("185.99"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # MYOCIL 5MG
    p_id_533 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000532")
    products[p_id_533] = {
        "id": p_id_533,
        "code": "MED-MYOCIL5M",
        "name": 'MYOCIL 5MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("51.61"),
        "default_purchase_price": Decimal("41.29"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_533 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000533")
    batches[b_id_533] = {
        "id": b_id_533,
        "product_id": p_id_533,
        "batch_number": "BCH-MEDMYO-28",
        "expiry_date": date(2028, 6, 21),
        "purchase_cost": Decimal("41.29"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # METFOR 850MG
    p_id_534 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000533")
    products[p_id_534] = {
        "id": p_id_534,
        "code": "MED-METFOR85",
        "name": 'METFOR 850MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("37.99"),
        "default_purchase_price": Decimal("30.39"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_534 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000534")
    batches[b_id_534] = {
        "id": b_id_534,
        "product_id": p_id_534,
        "batch_number": "BCH-MEDMET-27",
        "expiry_date": date(2027, 7, 22),
        "purchase_cost": Decimal("30.39"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ZYMOLIV 200 ML
    p_id_535 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000534")
    products[p_id_535] = {
        "id": p_id_535,
        "code": "MED-ZYMOLIV2",
        "name": 'ZYMOLIV 200 ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("223.24"),
        "default_purchase_price": Decimal("178.59"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_535 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000535")
    batches[b_id_535] = {
        "id": b_id_535,
        "product_id": p_id_535,
        "batch_number": "BCH-MEDZYM-28",
        "expiry_date": date(2028, 8, 23),
        "purchase_cost": Decimal("178.59"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # ATENOL 25MG TAB
    p_id_536 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000535")
    products[p_id_536] = {
        "id": p_id_536,
        "code": "MED-ATENOL25",
        "name": 'ATENOL 25MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("33.68"),
        "default_purchase_price": Decimal("26.94"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_536 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000536")
    batches[b_id_536] = {
        "id": b_id_536,
        "product_id": p_id_536,
        "batch_number": "BCH-MEDATE-27",
        "expiry_date": date(2027, 9, 24),
        "purchase_cost": Decimal("26.94"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # Tab GLYCOMET GP2
    p_id_537 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000536")
    products[p_id_537] = {
        "id": p_id_537,
        "code": "MED-TABGLYCO",
        "name": 'Tab GLYCOMET GP2',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("320.26"),
        "default_purchase_price": Decimal("256.21"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_537 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000537")
    batches[b_id_537] = {
        "id": b_id_537,
        "product_id": p_id_537,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 25),
        "purchase_cost": Decimal("256.21"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ICON 200MG CAP
    p_id_538 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000537")
    products[p_id_538] = {
        "id": p_id_538,
        "code": "MED-ICON200M",
        "name": 'ICON 200MG CAP',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("306.93"),
        "default_purchase_price": Decimal("245.54"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_538 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000538")
    batches[b_id_538] = {
        "id": b_id_538,
        "product_id": p_id_538,
        "batch_number": "BCH-MEDICO-27",
        "expiry_date": date(2027, 11, 26),
        "purchase_cost": Decimal("245.54"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # CLAVAM DROPS 10ML
    p_id_539 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000538")
    products[p_id_539] = {
        "id": p_id_539,
        "code": "MED-CLAVAMDR",
        "name": 'CLAVAM DROPS 10ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("119.61"),
        "default_purchase_price": Decimal("95.69"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_539 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000539")
    batches[b_id_539] = {
        "id": b_id_539,
        "product_id": p_id_539,
        "batch_number": "BCH-MEDCLA-28",
        "expiry_date": date(2028, 12, 27),
        "purchase_cost": Decimal("95.69"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # METLOC 12.5MG TAB
    p_id_540 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000539")
    products[p_id_540] = {
        "id": p_id_540,
        "code": "MED-METLOC12",
        "name": 'METLOC 12.5MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("29.59"),
        "default_purchase_price": Decimal("23.67"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_540 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000540")
    batches[b_id_540] = {
        "id": b_id_540,
        "product_id": p_id_540,
        "batch_number": "BCH-MEDMET-27",
        "expiry_date": date(2027, 1, 1),
        "purchase_cost": Decimal("23.67"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # REPANIDE 0.5MG
    p_id_541 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000540")
    products[p_id_541] = {
        "id": p_id_541,
        "code": "MED-REPANIDE-1",
        "name": 'REPANIDE 0.5MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("71.64"),
        "default_purchase_price": Decimal("57.31"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_541 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000541")
    batches[b_id_541] = {
        "id": b_id_541,
        "product_id": p_id_541,
        "batch_number": "BCH-MEDREP-28",
        "expiry_date": date(2028, 2, 2),
        "purchase_cost": Decimal("57.31"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # ES - PRAM 10MG
    p_id_542 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000541")
    products[p_id_542] = {
        "id": p_id_542,
        "code": "MED-ESPRAM10",
        "name": 'ES - PRAM 10MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("172.57"),
        "default_purchase_price": Decimal("138.06"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_542 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000542")
    batches[b_id_542] = {
        "id": b_id_542,
        "product_id": p_id_542,
        "batch_number": "BCH-MEDESP-27",
        "expiry_date": date(2027, 3, 3),
        "purchase_cost": Decimal("138.06"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # RITE OCEF 100 MG 60ML
    p_id_543 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000542")
    products[p_id_543] = {
        "id": p_id_543,
        "code": "MED-RITEOCEF-1",
        "name": 'RITE OCEF 100 MG 60ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("236.92"),
        "default_purchase_price": Decimal("189.54"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_543 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000543")
    batches[b_id_543] = {
        "id": b_id_543,
        "product_id": p_id_543,
        "batch_number": "BCH-MEDRIT-28",
        "expiry_date": date(2028, 4, 4),
        "purchase_cost": Decimal("189.54"),
        "quantity": 24,
        "is_active": True,
        "created_at": now,
    }

    # DEZACOR 30ML SUSP
    p_id_544 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000543")
    products[p_id_544] = {
        "id": p_id_544,
        "code": "MED-DEZACOR3",
        "name": 'DEZACOR 30ML SUSP',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("130.86"),
        "default_purchase_price": Decimal("104.69"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_544 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000544")
    batches[b_id_544] = {
        "id": b_id_544,
        "product_id": p_id_544,
        "batch_number": "BCH-MEDDEZ-27",
        "expiry_date": date(2027, 5, 5),
        "purchase_cost": Decimal("104.69"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # SIPTIN-M 500
    p_id_545 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000544")
    products[p_id_545] = {
        "id": p_id_545,
        "code": "MED-SIPTINM5",
        "name": 'SIPTIN-M 500',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("267.18"),
        "default_purchase_price": Decimal("213.74"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_545 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000545")
    batches[b_id_545] = {
        "id": b_id_545,
        "product_id": p_id_545,
        "batch_number": "BCH-MEDSIP-28",
        "expiry_date": date(2028, 6, 6),
        "purchase_cost": Decimal("213.74"),
        "quantity": 65,
        "is_active": True,
        "created_at": now,
    }

    # LINA-5
    p_id_546 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000545")
    products[p_id_546] = {
        "id": p_id_546,
        "code": "MED-LINA5",
        "name": 'LINA-5',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("196.94"),
        "default_purchase_price": Decimal("157.55"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_546 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000546")
    batches[b_id_546] = {
        "id": b_id_546,
        "product_id": p_id_546,
        "batch_number": "BCH-MEDLIN-27",
        "expiry_date": date(2027, 7, 7),
        "purchase_cost": Decimal("157.55"),
        "quantity": 74,
        "is_active": True,
        "created_at": now,
    }

    # LINTOR 5
    p_id_547 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000546")
    products[p_id_547] = {
        "id": p_id_547,
        "code": "MED-LINTOR5",
        "name": 'LINTOR 5',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("205.21"),
        "default_purchase_price": Decimal("164.17"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_547 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000547")
    batches[b_id_547] = {
        "id": b_id_547,
        "product_id": p_id_547,
        "batch_number": "BCH-MEDLIN-28",
        "expiry_date": date(2028, 8, 8),
        "purchase_cost": Decimal("164.17"),
        "quantity": 47,
        "is_active": True,
        "created_at": now,
    }

    # LINAMET 500 TAB
    p_id_548 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000547")
    products[p_id_548] = {
        "id": p_id_548,
        "code": "MED-LINAMET5",
        "name": 'LINAMET 500 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("218.75"),
        "default_purchase_price": Decimal("175.00"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_548 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000548")
    batches[b_id_548] = {
        "id": b_id_548,
        "product_id": p_id_548,
        "batch_number": "BCH-MEDLIN-27",
        "expiry_date": date(2027, 9, 9),
        "purchase_cost": Decimal("175.00"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB DOLOPAR
    p_id_549 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000548")
    products[p_id_549] = {
        "id": p_id_549,
        "code": "MED-TABDOLOP",
        "name": 'TAB DOLOPAR',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("76.29"),
        "default_purchase_price": Decimal("61.03"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_549 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000549")
    batches[b_id_549] = {
        "id": b_id_549,
        "product_id": p_id_549,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 10),
        "purchase_cost": Decimal("61.03"),
        "quantity": 104,
        "is_active": True,
        "created_at": now,
    }

    # TAB DIAPRIDE M1
    p_id_550 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000549")
    products[p_id_550] = {
        "id": p_id_550,
        "code": "MED-TABDIAPR",
        "name": 'TAB DIAPRIDE M1',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("243.55"),
        "default_purchase_price": Decimal("194.84"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_550 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000550")
    batches[b_id_550] = {
        "id": b_id_550,
        "product_id": p_id_550,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 11),
        "purchase_cost": Decimal("194.84"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # RITE O CEF. 200MG
    p_id_551 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000550")
    products[p_id_551] = {
        "id": p_id_551,
        "code": "MED-RITEOCEF-2",
        "name": 'RITE O CEF. 200MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("172.66"),
        "default_purchase_price": Decimal("138.13"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_551 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000551")
    batches[b_id_551] = {
        "id": b_id_551,
        "product_id": p_id_551,
        "batch_number": "BCH-MEDRIT-28",
        "expiry_date": date(2028, 12, 12),
        "purchase_cost": Decimal("138.13"),
        "quantity": 48,
        "is_active": True,
        "created_at": now,
    }

    # FORMIN G1 FORTE
    p_id_552 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000551")
    products[p_id_552] = {
        "id": p_id_552,
        "code": "MED-FORMING1-1",
        "name": 'FORMIN G1 FORTE',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("121.55"),
        "default_purchase_price": Decimal("97.24"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_552 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000552")
    batches[b_id_552] = {
        "id": b_id_552,
        "product_id": p_id_552,
        "batch_number": "BCH-MEDFOR-27",
        "expiry_date": date(2027, 1, 13),
        "purchase_cost": Decimal("97.24"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB CALSUP 500
    p_id_553 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000552")
    products[p_id_553] = {
        "id": p_id_553,
        "code": "MED-TABCALSU",
        "name": 'TAB CALSUP 500',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("55.84"),
        "default_purchase_price": Decimal("44.67"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_553 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000553")
    batches[b_id_553] = {
        "id": b_id_553,
        "product_id": p_id_553,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 14),
        "purchase_cost": Decimal("44.67"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB LOSAGEM 50MG
    p_id_554 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000553")
    products[p_id_554] = {
        "id": p_id_554,
        "code": "MED-TABLOSAG",
        "name": 'TAB LOSAGEM 50MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("24.04"),
        "default_purchase_price": Decimal("19.23"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_554 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000554")
    batches[b_id_554] = {
        "id": b_id_554,
        "product_id": p_id_554,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 15),
        "purchase_cost": Decimal("19.23"),
        "quantity": 130,
        "is_active": True,
        "created_at": now,
    }

    # TAB LIPITOP 5 MG
    p_id_555 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000554")
    products[p_id_555] = {
        "id": p_id_555,
        "code": "MED-TABLIPIT",
        "name": 'TAB LIPITOP 5 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("14.45"),
        "default_purchase_price": Decimal("11.56"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_555 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000555")
    batches[b_id_555] = {
        "id": b_id_555,
        "product_id": p_id_555,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 16),
        "purchase_cost": Decimal("11.56"),
        "quantity": 153,
        "is_active": True,
        "created_at": now,
    }

    # TAB SITAMET 850 SR
    p_id_556 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000555")
    products[p_id_556] = {
        "id": p_id_556,
        "code": "MED-TABSITAM",
        "name": 'TAB SITAMET 850 SR',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("283.34"),
        "default_purchase_price": Decimal("226.67"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_556 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000556")
    batches[b_id_556] = {
        "id": b_id_556,
        "product_id": p_id_556,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 17),
        "purchase_cost": Decimal("226.67"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # TAB LINOX -M FORT
    p_id_557 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000556")
    products[p_id_557] = {
        "id": p_id_557,
        "code": "MED-TABLINOX-2",
        "name": 'TAB LINOX -M FORT',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("173.41"),
        "default_purchase_price": Decimal("138.73"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_557 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000557")
    batches[b_id_557] = {
        "id": b_id_557,
        "product_id": p_id_557,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 18),
        "purchase_cost": Decimal("138.73"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB PANROL 40MG
    p_id_558 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000557")
    products[p_id_558] = {
        "id": p_id_558,
        "code": "MED-TABPANRO",
        "name": 'TAB PANROL 40MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("122.41"),
        "default_purchase_price": Decimal("97.93"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_558 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000558")
    batches[b_id_558] = {
        "id": b_id_558,
        "product_id": p_id_558,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 19),
        "purchase_cost": Decimal("97.93"),
        "quantity": 1,
        "is_active": True,
        "created_at": now,
    }

    # TAB PANROL-D
    p_id_559 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000558")
    products[p_id_559] = {
        "id": p_id_559,
        "code": "MED-TABPANRO-1",
        "name": 'TAB PANROL-D',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("154.93"),
        "default_purchase_price": Decimal("123.94"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_559 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000559")
    batches[b_id_559] = {
        "id": b_id_559,
        "product_id": p_id_559,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 20),
        "purchase_cost": Decimal("123.94"),
        "quantity": 24,
        "is_active": True,
        "created_at": now,
    }

    # TAB ZOCLAV 625
    p_id_560 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000559")
    products[p_id_560] = {
        "id": p_id_560,
        "code": "MED-TABZOCLA",
        "name": 'TAB ZOCLAV 625',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("238.04"),
        "default_purchase_price": Decimal("190.43"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_560 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000560")
    batches[b_id_560] = {
        "id": b_id_560,
        "product_id": p_id_560,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 21),
        "purchase_cost": Decimal("190.43"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB AGLOR 90MG
    p_id_561 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000560")
    products[p_id_561] = {
        "id": p_id_561,
        "code": "MED-TABAGLOR",
        "name": 'TAB AGLOR 90MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("464.38"),
        "default_purchase_price": Decimal("371.50"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_561 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000561")
    batches[b_id_561] = {
        "id": b_id_561,
        "product_id": p_id_561,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 22),
        "purchase_cost": Decimal("371.50"),
        "quantity": 21,
        "is_active": True,
        "created_at": now,
    }

    # TAB ALADIN 120
    p_id_562 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000561")
    products[p_id_562] = {
        "id": p_id_562,
        "code": "MED-TABALADI",
        "name": 'TAB ALADIN 120',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("102.00"),
        "default_purchase_price": Decimal("81.60"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_562 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000562")
    batches[b_id_562] = {
        "id": b_id_562,
        "product_id": p_id_562,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 23),
        "purchase_cost": Decimal("81.60"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB ALADIN 180MG
    p_id_563 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000562")
    products[p_id_563] = {
        "id": p_id_563,
        "code": "MED-TABALADI-1",
        "name": 'TAB ALADIN 180MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("153.04"),
        "default_purchase_price": Decimal("122.43"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_563 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000563")
    batches[b_id_563] = {
        "id": b_id_563,
        "product_id": p_id_563,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 24),
        "purchase_cost": Decimal("122.43"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB ASTAT 20MG
    p_id_564 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000563")
    products[p_id_564] = {
        "id": p_id_564,
        "code": "MED-TABASTAT",
        "name": 'TAB ASTAT 20MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("210.16"),
        "default_purchase_price": Decimal("168.13"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_564 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000564")
    batches[b_id_564] = {
        "id": b_id_564,
        "product_id": p_id_564,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 25),
        "purchase_cost": Decimal("168.13"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # BENTIN CREM 15GM
    p_id_565 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000564")
    products[p_id_565] = {
        "id": p_id_565,
        "code": "MED-BENTINCR",
        "name": 'BENTIN CREM 15GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("132.61"),
        "default_purchase_price": Decimal("106.09"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_565 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000565")
    batches[b_id_565] = {
        "id": b_id_565,
        "product_id": p_id_565,
        "batch_number": "BCH-MEDBEN-28",
        "expiry_date": date(2028, 2, 26),
        "purchase_cost": Decimal("106.09"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # BETASALIC  CREAM 20GM
    p_id_566 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000565")
    products[p_id_566] = {
        "id": p_id_566,
        "code": "MED-BETASALI",
        "name": 'BETASALIC  CREAM 20GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("113.14"),
        "default_purchase_price": Decimal("90.51"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_566 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000566")
    batches[b_id_566] = {
        "id": b_id_566,
        "product_id": p_id_566,
        "batch_number": "BCH-MEDBET-27",
        "expiry_date": date(2027, 3, 27),
        "purchase_cost": Decimal("90.51"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # CAP BIOXY
    p_id_567 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000566")
    products[p_id_567] = {
        "id": p_id_567,
        "code": "MED-CAPBIOXY",
        "name": 'CAP BIOXY',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("61.20"),
        "default_purchase_price": Decimal("48.96"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_567 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000567")
    batches[b_id_567] = {
        "id": b_id_567,
        "product_id": p_id_567,
        "batch_number": "BCH-MEDCAP-28",
        "expiry_date": date(2028, 4, 1),
        "purchase_cost": Decimal("48.96"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # CLINDACIN GEL
    p_id_568 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000567")
    products[p_id_568] = {
        "id": p_id_568,
        "code": "MED-CLINDACI",
        "name": 'CLINDACIN GEL',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("137.74"),
        "default_purchase_price": Decimal("110.19"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_568 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000568")
    batches[b_id_568] = {
        "id": b_id_568,
        "product_id": p_id_568,
        "batch_number": "BCH-MEDCLI-27",
        "expiry_date": date(2027, 5, 2),
        "purchase_cost": Decimal("110.19"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # CLODERM G 30GM
    p_id_569 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000568")
    products[p_id_569] = {
        "id": p_id_569,
        "code": "MED-CLODERMG",
        "name": 'CLODERM G 30GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("160.16"),
        "default_purchase_price": Decimal("128.13"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_569 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000569")
    batches[b_id_569] = {
        "id": b_id_569,
        "product_id": p_id_569,
        "batch_number": "BCH-MEDCLO-28",
        "expiry_date": date(2028, 6, 3),
        "purchase_cost": Decimal("128.13"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # CLODERM 30GM CREAM
    p_id_570 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000569")
    products[p_id_570] = {
        "id": p_id_570,
        "code": "MED-CLODERM3",
        "name": 'CLODERM 30GM CREAM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("159.18"),
        "default_purchase_price": Decimal("127.34"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_570 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000570")
    batches[b_id_570] = {
        "id": b_id_570,
        "product_id": p_id_570,
        "batch_number": "BCH-MEDCLO-27",
        "expiry_date": date(2027, 7, 4),
        "purchase_cost": Decimal("127.34"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # CAP DFER
    p_id_571 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000570")
    products[p_id_571] = {
        "id": p_id_571,
        "code": "MED-CAPDFER",
        "name": 'CAP DFER',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("195.90"),
        "default_purchase_price": Decimal("156.72"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_571 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000571")
    batches[b_id_571] = {
        "id": b_id_571,
        "product_id": p_id_571,
        "batch_number": "BCH-MEDCAP-28",
        "expiry_date": date(2028, 8, 5),
        "purchase_cost": Decimal("156.72"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB DIABIN 0.2
    p_id_572 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000571")
    products[p_id_572] = {
        "id": p_id_572,
        "code": "MED-TABDIABI",
        "name": 'TAB DIABIN 0.2',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("112.48"),
        "default_purchase_price": Decimal("89.98"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_572 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000572")
    batches[b_id_572] = {
        "id": b_id_572,
        "product_id": p_id_572,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 6),
        "purchase_cost": Decimal("89.98"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # LINTOR M500 MG
    p_id_573 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000572")
    products[p_id_573] = {
        "id": p_id_573,
        "code": "MED-LINTORM5",
        "name": 'LINTOR M500 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("144.18"),
        "default_purchase_price": Decimal("115.34"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_573 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000573")
    batches[b_id_573] = {
        "id": b_id_573,
        "product_id": p_id_573,
        "batch_number": "BCH-MEDLIN-28",
        "expiry_date": date(2028, 10, 7),
        "purchase_cost": Decimal("115.34"),
        "quantity": 24,
        "is_active": True,
        "created_at": now,
    }

    # ALZIN TAB
    p_id_574 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000573")
    products[p_id_574] = {
        "id": p_id_574,
        "code": "MED-ALZINTAB",
        "name": 'ALZIN TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("275.49"),
        "default_purchase_price": Decimal("220.39"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_574 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000574")
    batches[b_id_574] = {
        "id": b_id_574,
        "product_id": p_id_574,
        "batch_number": "BCH-MEDALZ-27",
        "expiry_date": date(2027, 11, 8),
        "purchase_cost": Decimal("220.39"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB DIABIN 0.3
    p_id_575 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000574")
    products[p_id_575] = {
        "id": p_id_575,
        "code": "MED-TABDIABI-1",
        "name": 'TAB DIABIN 0.3',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("153.06"),
        "default_purchase_price": Decimal("122.45"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_575 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000575")
    batches[b_id_575] = {
        "id": b_id_575,
        "product_id": p_id_575,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 9),
        "purchase_cost": Decimal("122.45"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB EMPAZ 25MG
    p_id_576 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000575")
    products[p_id_576] = {
        "id": p_id_576,
        "code": "MED-TABEMPAZ-1",
        "name": 'TAB EMPAZ 25MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("303.27"),
        "default_purchase_price": Decimal("242.62"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_576 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000576")
    batches[b_id_576] = {
        "id": b_id_576,
        "product_id": p_id_576,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 10),
        "purchase_cost": Decimal("242.62"),
        "quantity": 17,
        "is_active": True,
        "created_at": now,
    }

    # TAB GLURIDE 1
    p_id_577 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000576")
    products[p_id_577] = {
        "id": p_id_577,
        "code": "MED-TABGLURI",
        "name": 'TAB GLURIDE 1',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("54.74"),
        "default_purchase_price": Decimal("43.79"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_577 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000577")
    batches[b_id_577] = {
        "id": b_id_577,
        "product_id": p_id_577,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 11),
        "purchase_cost": Decimal("43.79"),
        "quantity": 16,
        "is_active": True,
        "created_at": now,
    }

    # GLURIDE 3MG TAB
    p_id_578 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000577")
    products[p_id_578] = {
        "id": p_id_578,
        "code": "MED-GLURIDE3",
        "name": 'GLURIDE 3MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("115.72"),
        "default_purchase_price": Decimal("92.58"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_578 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000578")
    batches[b_id_578] = {
        "id": b_id_578,
        "product_id": p_id_578,
        "batch_number": "BCH-MEDGLU-27",
        "expiry_date": date(2027, 3, 12),
        "purchase_cost": Decimal("92.58"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB MOCAST L
    p_id_579 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000578")
    products[p_id_579] = {
        "id": p_id_579,
        "code": "MED-TABMOCAS",
        "name": 'TAB MOCAST L',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("183.65"),
        "default_purchase_price": Decimal("146.92"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_579 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000579")
    batches[b_id_579] = {
        "id": b_id_579,
        "product_id": p_id_579,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 13),
        "purchase_cost": Decimal("146.92"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB NEWLIN 75MG
    p_id_580 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000579")
    products[p_id_580] = {
        "id": p_id_580,
        "code": "MED-TABNEWLI",
        "name": 'TAB NEWLIN 75MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("86.65"),
        "default_purchase_price": Decimal("69.32"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_580 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000580")
    batches[b_id_580] = {
        "id": b_id_580,
        "product_id": p_id_580,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 14),
        "purchase_cost": Decimal("69.32"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # TAB OLACE 10 MG
    p_id_581 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000580")
    products[p_id_581] = {
        "id": p_id_581,
        "code": "MED-TABOLACE",
        "name": 'TAB OLACE 10 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("61.24"),
        "default_purchase_price": Decimal("48.99"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_581 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000581")
    batches[b_id_581] = {
        "id": b_id_581,
        "product_id": p_id_581,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 15),
        "purchase_cost": Decimal("48.99"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB Q-PIL 5MG
    p_id_582 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000581")
    products[p_id_582] = {
        "id": p_id_582,
        "code": "MED-TABQPIL5",
        "name": 'TAB Q-PIL 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("40.82"),
        "default_purchase_price": Decimal("32.66"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_582 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000582")
    batches[b_id_582] = {
        "id": b_id_582,
        "product_id": p_id_582,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 16),
        "purchase_cost": Decimal("32.66"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB REPANIDE 2MG
    p_id_583 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000582")
    products[p_id_583] = {
        "id": p_id_583,
        "code": "MED-TABREPAN",
        "name": 'TAB REPANIDE 2MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("122.42"),
        "default_purchase_price": Decimal("97.94"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_583 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000583")
    batches[b_id_583] = {
        "id": b_id_583,
        "product_id": p_id_583,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 17),
        "purchase_cost": Decimal("97.94"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB SIPTIN 25MG
    p_id_584 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000583")
    products[p_id_584] = {
        "id": p_id_584,
        "code": "MED-TABSIPTI",
        "name": 'TAB SIPTIN 25MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("153.75"),
        "default_purchase_price": Decimal("123.00"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_584 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000584")
    batches[b_id_584] = {
        "id": b_id_584,
        "product_id": p_id_584,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 18),
        "purchase_cost": Decimal("123.00"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB SIPTIN 50MG
    p_id_585 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000584")
    products[p_id_585] = {
        "id": p_id_585,
        "code": "MED-TABSIPTI-1",
        "name": 'TAB SIPTIN 50MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("257.00"),
        "default_purchase_price": Decimal("205.60"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_585 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000585")
    batches[b_id_585] = {
        "id": b_id_585,
        "product_id": p_id_585,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 19),
        "purchase_cost": Decimal("205.60"),
        "quantity": 9,
        "is_active": True,
        "created_at": now,
    }

    # TAB SOLAY
    p_id_586 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000585")
    products[p_id_586] = {
        "id": p_id_586,
        "code": "MED-TABSOLAY",
        "name": 'TAB SOLAY',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("382.57"),
        "default_purchase_price": Decimal("306.06"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_586 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000586")
    batches[b_id_586] = {
        "id": b_id_586,
        "product_id": p_id_586,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 20),
        "purchase_cost": Decimal("306.06"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # FUSID CR
    p_id_587 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000586")
    products[p_id_587] = {
        "id": p_id_587,
        "code": "MED-FUSIDCR",
        "name": 'FUSID CR',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("81.65"),
        "default_purchase_price": Decimal("65.32"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_587 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000587")
    batches[b_id_587] = {
        "id": b_id_587,
        "product_id": p_id_587,
        "batch_number": "BCH-MEDFUS-28",
        "expiry_date": date(2028, 12, 21),
        "purchase_cost": Decimal("65.32"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # THYRONICS 62.5
    p_id_588 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000587")
    products[p_id_588] = {
        "id": p_id_588,
        "code": "MED-THYRONIC",
        "name": 'THYRONICS 62.5',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("302.45"),
        "default_purchase_price": Decimal("241.96"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_588 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000588")
    batches[b_id_588] = {
        "id": b_id_588,
        "product_id": p_id_588,
        "batch_number": "BCH-MEDTHY-27",
        "expiry_date": date(2027, 1, 22),
        "purchase_cost": Decimal("241.96"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # THYRONICS 12.5
    p_id_589 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000588")
    products[p_id_589] = {
        "id": p_id_589,
        "code": "MED-THYRONIC-1",
        "name": 'THYRONICS 12.5',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("289.77"),
        "default_purchase_price": Decimal("231.82"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_589 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000589")
    batches[b_id_589] = {
        "id": b_id_589,
        "product_id": p_id_589,
        "batch_number": "BCH-MEDTHY-28",
        "expiry_date": date(2028, 2, 23),
        "purchase_cost": Decimal("231.82"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # THYRONICS 75
    p_id_590 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000589")
    products[p_id_590] = {
        "id": p_id_590,
        "code": "MED-THYRONIC-2",
        "name": 'THYRONICS 75',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("287.91"),
        "default_purchase_price": Decimal("230.33"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_590 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000590")
    batches[b_id_590] = {
        "id": b_id_590,
        "product_id": p_id_590,
        "batch_number": "BCH-MEDTHY-27",
        "expiry_date": date(2027, 3, 24),
        "purchase_cost": Decimal("230.33"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # THYRONICS 25
    p_id_591 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000590")
    products[p_id_591] = {
        "id": p_id_591,
        "code": "MED-THYRONIC-3",
        "name": 'THYRONICS 25',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("283.68"),
        "default_purchase_price": Decimal("226.94"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_591 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000591")
    batches[b_id_591] = {
        "id": b_id_591,
        "product_id": p_id_591,
        "batch_number": "BCH-MEDTHY-28",
        "expiry_date": date(2028, 4, 25),
        "purchase_cost": Decimal("226.94"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # THYRONICS 37.5
    p_id_592 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000591")
    products[p_id_592] = {
        "id": p_id_592,
        "code": "MED-THYRONIC-4",
        "name": 'THYRONICS 37.5',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("317.54"),
        "default_purchase_price": Decimal("254.03"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_592 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000592")
    batches[b_id_592] = {
        "id": b_id_592,
        "product_id": p_id_592,
        "batch_number": "BCH-MEDTHY-27",
        "expiry_date": date(2027, 5, 26),
        "purchase_cost": Decimal("254.03"),
        "quantity": 9,
        "is_active": True,
        "created_at": now,
    }

    # TAB THROBEX 10MG
    p_id_593 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000592")
    products[p_id_593] = {
        "id": p_id_593,
        "code": "MED-TABTHROB",
        "name": 'TAB THROBEX 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("714.09"),
        "default_purchase_price": Decimal("571.27"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_593 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000593")
    batches[b_id_593] = {
        "id": b_id_593,
        "product_id": p_id_593,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 27),
        "purchase_cost": Decimal("571.27"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB THROBEX 15MG
    p_id_594 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000593")
    products[p_id_594] = {
        "id": p_id_594,
        "code": "MED-TABTHROB-1",
        "name": 'TAB THROBEX 15MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("823.71"),
        "default_purchase_price": Decimal("658.97"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_594 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000594")
    batches[b_id_594] = {
        "id": b_id_594,
        "product_id": p_id_594,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 1),
        "purchase_cost": Decimal("658.97"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB T-ZINE
    p_id_595 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000594")
    products[p_id_595] = {
        "id": p_id_595,
        "code": "MED-TABTZINE",
        "name": 'TAB T-ZINE',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("45.90"),
        "default_purchase_price": Decimal("36.72"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_595 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000595")
    batches[b_id_595] = {
        "id": b_id_595,
        "product_id": p_id_595,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 2),
        "purchase_cost": Decimal("36.72"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB URADER 4MG
    p_id_596 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000595")
    products[p_id_596] = {
        "id": p_id_596,
        "code": "MED-TABURADE",
        "name": 'TAB URADER 4MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("204.06"),
        "default_purchase_price": Decimal("163.25"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_596 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000596")
    batches[b_id_596] = {
        "id": b_id_596,
        "product_id": p_id_596,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 3),
        "purchase_cost": Decimal("163.25"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB URADER 8MG
    p_id_597 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000596")
    products[p_id_597] = {
        "id": p_id_597,
        "code": "MED-TABURADE-1",
        "name": 'TAB URADER 8MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("357.05"),
        "default_purchase_price": Decimal("285.64"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_597 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000597")
    batches[b_id_597] = {
        "id": b_id_597,
        "product_id": p_id_597,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 4),
        "purchase_cost": Decimal("285.64"),
        "quantity": 1,
        "is_active": True,
        "created_at": now,
    }

    # TAB ZIDE 40MG
    p_id_598 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000597")
    products[p_id_598] = {
        "id": p_id_598,
        "code": "MED-TABZIDE4",
        "name": 'TAB ZIDE 40MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("61.24"),
        "default_purchase_price": Decimal("48.99"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_598 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000598")
    batches[b_id_598] = {
        "id": b_id_598,
        "product_id": p_id_598,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 5),
        "purchase_cost": Decimal("48.99"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB CALCITATE
    p_id_599 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000598")
    products[p_id_599] = {
        "id": p_id_599,
        "code": "MED-TABCALCI",
        "name": 'TAB CALCITATE',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("612.09"),
        "default_purchase_price": Decimal("489.67"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_599 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000599")
    batches[b_id_599] = {
        "id": b_id_599,
        "product_id": p_id_599,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 6),
        "purchase_cost": Decimal("489.67"),
        "quantity": 1,
        "is_active": True,
        "created_at": now,
    }

    # TAB CALPLUS
    p_id_600 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000599")
    products[p_id_600] = {
        "id": p_id_600,
        "code": "MED-TABCALPL",
        "name": 'TAB CALPLUS',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("490.91"),
        "default_purchase_price": Decimal("392.73"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_600 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000600")
    batches[b_id_600] = {
        "id": b_id_600,
        "product_id": p_id_600,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 7),
        "purchase_cost": Decimal("392.73"),
        "quantity": 4,
        "is_active": True,
        "created_at": now,
    }

    # TAB GLYFALL 500ER
    p_id_601 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000600")
    products[p_id_601] = {
        "id": p_id_601,
        "code": "MED-TABGLYFA",
        "name": 'TAB GLYFALL 500ER',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("53.99"),
        "default_purchase_price": Decimal("43.19"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_601 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000601")
    batches[b_id_601] = {
        "id": b_id_601,
        "product_id": p_id_601,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 8),
        "purchase_cost": Decimal("43.19"),
        "quantity": 7,
        "is_active": True,
        "created_at": now,
    }

    # HALOSOFT -F 10GM CREM
    p_id_602 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000601")
    products[p_id_602] = {
        "id": p_id_602,
        "code": "MED-HALOSOFT",
        "name": 'HALOSOFT -F 10GM CREM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("183.65"),
        "default_purchase_price": Decimal("146.92"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_602 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000602")
    batches[b_id_602] = {
        "id": b_id_602,
        "product_id": p_id_602,
        "batch_number": "BCH-MEDHAL-27",
        "expiry_date": date(2027, 3, 9),
        "purchase_cost": Decimal("146.92"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # HALOSOFT -S 20GM
    p_id_603 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000602")
    products[p_id_603] = {
        "id": p_id_603,
        "code": "MED-HALOSOFT-1",
        "name": 'HALOSOFT -S 20GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("244.84"),
        "default_purchase_price": Decimal("195.87"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_603 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000603")
    batches[b_id_603] = {
        "id": b_id_603,
        "product_id": p_id_603,
        "batch_number": "BCH-MEDHAL-28",
        "expiry_date": date(2028, 4, 10),
        "purchase_cost": Decimal("195.87"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB LOSPIL 25
    p_id_604 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000603")
    products[p_id_604] = {
        "id": p_id_604,
        "code": "MED-TABLOSPI-3",
        "name": 'TAB LOSPIL 25',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("44.91"),
        "default_purchase_price": Decimal("35.93"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_604 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000604")
    batches[b_id_604] = {
        "id": b_id_604,
        "product_id": p_id_604,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 11),
        "purchase_cost": Decimal("35.93"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB AMLONG -A
    p_id_605 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000604")
    products[p_id_605] = {
        "id": p_id_605,
        "code": "MED-TABAMLON-2",
        "name": 'TAB AMLONG -A',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("287.70"),
        "default_purchase_price": Decimal("230.16"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_605 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000605")
    batches[b_id_605] = {
        "id": b_id_605,
        "product_id": p_id_605,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 12),
        "purchase_cost": Decimal("230.16"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # TAB ASTAT 40MG
    p_id_606 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000605")
    products[p_id_606] = {
        "id": p_id_606,
        "code": "MED-TABASTAT-1",
        "name": 'TAB ASTAT 40MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("382.38"),
        "default_purchase_price": Decimal("305.90"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_606 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000606")
    batches[b_id_606] = {
        "id": b_id_606,
        "product_id": p_id_606,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 13),
        "purchase_cost": Decimal("305.90"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB LINAMET 1GM
    p_id_607 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000606")
    products[p_id_607] = {
        "id": p_id_607,
        "code": "MED-TABLINAM",
        "name": 'TAB LINAMET 1GM',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("261.04"),
        "default_purchase_price": Decimal("208.83"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_607 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000607")
    batches[b_id_607] = {
        "id": b_id_607,
        "product_id": p_id_607,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 14),
        "purchase_cost": Decimal("208.83"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB E-LINA 25MG
    p_id_608 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000607")
    products[p_id_608] = {
        "id": p_id_608,
        "code": "MED-TABELINA",
        "name": 'TAB E-LINA 25MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("511.88"),
        "default_purchase_price": Decimal("409.50"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_608 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000608")
    batches[b_id_608] = {
        "id": b_id_608,
        "product_id": p_id_608,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 15),
        "purchase_cost": Decimal("409.50"),
        "quantity": 4,
        "is_active": True,
        "created_at": now,
    }

    # E -LINA 10MG TAB
    p_id_609 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000608")
    products[p_id_609] = {
        "id": p_id_609,
        "code": "MED-ELINA10M",
        "name": 'E -LINA 10MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("440.81"),
        "default_purchase_price": Decimal("352.65"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_609 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000609")
    batches[b_id_609] = {
        "id": b_id_609,
        "product_id": p_id_609,
        "batch_number": "BCH-MEDELI-28",
        "expiry_date": date(2028, 10, 16),
        "purchase_cost": Decimal("352.65"),
        "quantity": 30,
        "is_active": True,
        "created_at": now,
    }

    # TAB DIBET 1MG
    p_id_610 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000609")
    products[p_id_610] = {
        "id": p_id_610,
        "code": "MED-TABDIBET",
        "name": 'TAB DIBET 1MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("76.29"),
        "default_purchase_price": Decimal("61.03"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_610 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000610")
    batches[b_id_610] = {
        "id": b_id_610,
        "product_id": p_id_610,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 17),
        "purchase_cost": Decimal("61.03"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB ROVASTIN 5MG
    p_id_611 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000610")
    products[p_id_611] = {
        "id": p_id_611,
        "code": "MED-TABROVAS",
        "name": 'TAB ROVASTIN 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("125.41"),
        "default_purchase_price": Decimal("100.33"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_611 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000611")
    batches[b_id_611] = {
        "id": b_id_611,
        "product_id": p_id_611,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 18),
        "purchase_cost": Decimal("100.33"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB CALRIK 60K
    p_id_612 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000611")
    products[p_id_612] = {
        "id": p_id_612,
        "code": "MED-TABCALRI",
        "name": 'TAB CALRIK 60K',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("414.94"),
        "default_purchase_price": Decimal("331.95"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_612 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000612")
    batches[b_id_612] = {
        "id": b_id_612,
        "product_id": p_id_612,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 19),
        "purchase_cost": Decimal("331.95"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB TENEPRIDE M 500
    p_id_613 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000612")
    products[p_id_613] = {
        "id": p_id_613,
        "code": "MED-TABTENEP",
        "name": 'TAB TENEPRIDE M 500',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("401.96"),
        "default_purchase_price": Decimal("321.57"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_613 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000613")
    batches[b_id_613] = {
        "id": b_id_613,
        "product_id": p_id_613,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 20),
        "purchase_cost": Decimal("321.57"),
        "quantity": 30,
        "is_active": True,
        "created_at": now,
    }

    # TAB NEFRO 20MG
    p_id_614 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000613")
    products[p_id_614] = {
        "id": p_id_614,
        "code": "MED-TABNEFRO",
        "name": 'TAB NEFRO 20MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("954.71"),
        "default_purchase_price": Decimal("763.77"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_614 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000614")
    batches[b_id_614] = {
        "id": b_id_614,
        "product_id": p_id_614,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 21),
        "purchase_cost": Decimal("763.77"),
        "quantity": 9,
        "is_active": True,
        "created_at": now,
    }

    # TAB DIAPRIDE M 0.5MG
    p_id_615 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000614")
    products[p_id_615] = {
        "id": p_id_615,
        "code": "MED-TABDIAPR-1",
        "name": 'TAB DIAPRIDE M 0.5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("85.59"),
        "default_purchase_price": Decimal("68.47"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_615 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000615")
    batches[b_id_615] = {
        "id": b_id_615,
        "product_id": p_id_615,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 22),
        "purchase_cost": Decimal("68.47"),
        "quantity": 55,
        "is_active": True,
        "created_at": now,
    }

    # TAB OLMAT -AM 40MG
    p_id_616 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000615")
    products[p_id_616] = {
        "id": p_id_616,
        "code": "MED-TABOLMAT",
        "name": 'TAB OLMAT -AM 40MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("637.15"),
        "default_purchase_price": Decimal("509.72"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_616 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000616")
    batches[b_id_616] = {
        "id": b_id_616,
        "product_id": p_id_616,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 23),
        "purchase_cost": Decimal("509.72"),
        "quantity": 4,
        "is_active": True,
        "created_at": now,
    }

    # TAB CHOLIROL 60K
    p_id_617 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000616")
    products[p_id_617] = {
        "id": p_id_617,
        "code": "MED-TABCHOLI",
        "name": 'TAB CHOLIROL 60K',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("271.10"),
        "default_purchase_price": Decimal("216.88"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_617 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000617")
    batches[b_id_617] = {
        "id": b_id_617,
        "product_id": p_id_617,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 24),
        "purchase_cost": Decimal("216.88"),
        "quantity": 7,
        "is_active": True,
        "created_at": now,
    }

    # TAB FARIN 3MG
    p_id_618 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000617")
    products[p_id_618] = {
        "id": p_id_618,
        "code": "MED-TABFARIN-1",
        "name": 'TAB FARIN 3MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("51.39"),
        "default_purchase_price": Decimal("41.11"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_618 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000618")
    batches[b_id_618] = {
        "id": b_id_618,
        "product_id": p_id_618,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 25),
        "purchase_cost": Decimal("41.11"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # TAB REXTER 10MG
    p_id_619 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000618")
    products[p_id_619] = {
        "id": p_id_619,
        "code": "MED-TABREXTE",
        "name": 'TAB REXTER 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("67.44"),
        "default_purchase_price": Decimal("53.95"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_619 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000619")
    batches[b_id_619] = {
        "id": b_id_619,
        "product_id": p_id_619,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 26),
        "purchase_cost": Decimal("53.95"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB FARIN 2MG
    p_id_620 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000619")
    products[p_id_620] = {
        "id": p_id_620,
        "code": "MED-TABFARIN-2",
        "name": 'TAB FARIN 2MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("46.50"),
        "default_purchase_price": Decimal("37.20"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_620 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000620")
    batches[b_id_620] = {
        "id": b_id_620,
        "product_id": p_id_620,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 27),
        "purchase_cost": Decimal("37.20"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # TAB ZINEP DT 10MG
    p_id_621 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000620")
    products[p_id_621] = {
        "id": p_id_621,
        "code": "MED-TABZINEP",
        "name": 'TAB ZINEP DT 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("43.21"),
        "default_purchase_price": Decimal("34.57"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_621 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000621")
    batches[b_id_621] = {
        "id": b_id_621,
        "product_id": p_id_621,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 1),
        "purchase_cost": Decimal("34.57"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # THYRONICS 50MG TAB
    p_id_622 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000621")
    products[p_id_622] = {
        "id": p_id_622,
        "code": "MED-THYRONIC-5",
        "name": 'THYRONICS 50MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("216.06"),
        "default_purchase_price": Decimal("172.85"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_622 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000622")
    batches[b_id_622] = {
        "id": b_id_622,
        "product_id": p_id_622,
        "batch_number": "BCH-MEDTHY-27",
        "expiry_date": date(2027, 11, 2),
        "purchase_cost": Decimal("172.85"),
        "quantity": 9,
        "is_active": True,
        "created_at": now,
    }

    # TAB GLYFALL G1
    p_id_623 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000622")
    products[p_id_623] = {
        "id": p_id_623,
        "code": "MED-TABGLYFA-1",
        "name": 'TAB GLYFALL G1',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("154.55"),
        "default_purchase_price": Decimal("123.64"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_623 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000623")
    batches[b_id_623] = {
        "id": b_id_623,
        "product_id": p_id_623,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 3),
        "purchase_cost": Decimal("123.64"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # TAB SOBICA 1GM
    p_id_624 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000623")
    products[p_id_624] = {
        "id": p_id_624,
        "code": "MED-TABSOBIC-2",
        "name": 'TAB SOBICA 1GM',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("492.55"),
        "default_purchase_price": Decimal("394.04"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_624 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000624")
    batches[b_id_624] = {
        "id": b_id_624,
        "product_id": p_id_624,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 4),
        "purchase_cost": Decimal("394.04"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB OZIN 10MG
    p_id_625 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000624")
    products[p_id_625] = {
        "id": p_id_625,
        "code": "MED-TABOZIN1",
        "name": 'TAB OZIN 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("246.60"),
        "default_purchase_price": Decimal("197.28"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_625 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000625")
    batches[b_id_625] = {
        "id": b_id_625,
        "product_id": p_id_625,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 5),
        "purchase_cost": Decimal("197.28"),
        "quantity": 30,
        "is_active": True,
        "created_at": now,
    }

    # TAB SIPTIN M 1000 MG
    p_id_626 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000625")
    products[p_id_626] = {
        "id": p_id_626,
        "code": "MED-TABSIPTI-2",
        "name": 'TAB SIPTIN M 1000 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("290.60"),
        "default_purchase_price": Decimal("232.48"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_626 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000626")
    batches[b_id_626] = {
        "id": b_id_626,
        "product_id": p_id_626,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 6),
        "purchase_cost": Decimal("232.48"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB FORMET G1
    p_id_627 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000626")
    products[p_id_627] = {
        "id": p_id_627,
        "code": "MED-TABFORME",
        "name": 'TAB FORMET G1',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("102.52"),
        "default_purchase_price": Decimal("82.02"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_627 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000627")
    batches[b_id_627] = {
        "id": b_id_627,
        "product_id": p_id_627,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 7),
        "purchase_cost": Decimal("82.02"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB FORMET G2
    p_id_628 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000627")
    products[p_id_628] = {
        "id": p_id_628,
        "code": "MED-TABFORME-1",
        "name": 'TAB FORMET G2',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("143.45"),
        "default_purchase_price": Decimal("114.76"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_628 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000628")
    batches[b_id_628] = {
        "id": b_id_628,
        "product_id": p_id_628,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 8),
        "purchase_cost": Decimal("114.76"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB METFLICS G1 FORTE
    p_id_629 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000628")
    products[p_id_629] = {
        "id": p_id_629,
        "code": "MED-TABMETFL",
        "name": 'TAB METFLICS G1 FORTE',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("118.56"),
        "default_purchase_price": Decimal("94.85"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_629 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000629")
    batches[b_id_629] = {
        "id": b_id_629,
        "product_id": p_id_629,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 9),
        "purchase_cost": Decimal("94.85"),
        "quantity": 16,
        "is_active": True,
        "created_at": now,
    }

    # TAB DOLOWIN SR
    p_id_630 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000629")
    products[p_id_630] = {
        "id": p_id_630,
        "code": "MED-TABDOLOW",
        "name": 'TAB DOLOWIN SR',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("145.29"),
        "default_purchase_price": Decimal("116.23"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_630 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000630")
    batches[b_id_630] = {
        "id": b_id_630,
        "product_id": p_id_630,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 10),
        "purchase_cost": Decimal("116.23"),
        "quantity": 60,
        "is_active": True,
        "created_at": now,
    }

    # TAB APIXA 5MG
    p_id_631 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000630")
    products[p_id_631] = {
        "id": p_id_631,
        "code": "MED-TABAPIXA",
        "name": 'TAB APIXA 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("310.35"),
        "default_purchase_price": Decimal("248.28"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_631 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000631")
    batches[b_id_631] = {
        "id": b_id_631,
        "product_id": p_id_631,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 11),
        "purchase_cost": Decimal("248.28"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB REGLIN 50MG
    p_id_632 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000631")
    products[p_id_632] = {
        "id": p_id_632,
        "code": "MED-TABREGLI",
        "name": 'TAB REGLIN 50MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("286.88"),
        "default_purchase_price": Decimal("229.50"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_632 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000632")
    batches[b_id_632] = {
        "id": b_id_632,
        "product_id": p_id_632,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 12),
        "purchase_cost": Decimal("229.50"),
        "quantity": 25,
        "is_active": True,
        "created_at": now,
    }

    # TAB SITAPRO M500MG
    p_id_633 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000632")
    products[p_id_633] = {
        "id": p_id_633,
        "code": "MED-TABSITAP",
        "name": 'TAB SITAPRO M500MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("387.71"),
        "default_purchase_price": Decimal("310.17"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_633 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000633")
    batches[b_id_633] = {
        "id": b_id_633,
        "product_id": p_id_633,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 13),
        "purchase_cost": Decimal("310.17"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB MOXILONG 0.3
    p_id_634 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000633")
    products[p_id_634] = {
        "id": p_id_634,
        "code": "MED-TABMOXIL",
        "name": 'TAB MOXILONG 0.3',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("348.04"),
        "default_purchase_price": Decimal("278.43"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_634 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000634")
    batches[b_id_634] = {
        "id": b_id_634,
        "product_id": p_id_634,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 14),
        "purchase_cost": Decimal("278.43"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # TAB MOXILONG 0.2 MG
    p_id_635 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000634")
    products[p_id_635] = {
        "id": p_id_635,
        "code": "MED-TABMOXIL-1",
        "name": 'TAB MOXILONG 0.2 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("251.54"),
        "default_purchase_price": Decimal("201.23"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_635 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000635")
    batches[b_id_635] = {
        "id": b_id_635,
        "product_id": p_id_635,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 15),
        "purchase_cost": Decimal("201.23"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB TOFATOP 5MG
    p_id_636 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000635")
    products[p_id_636] = {
        "id": p_id_636,
        "code": "MED-TABTOFAT",
        "name": 'TAB TOFATOP 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("297.94"),
        "default_purchase_price": Decimal("238.35"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_636 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000636")
    batches[b_id_636] = {
        "id": b_id_636,
        "product_id": p_id_636,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 16),
        "purchase_cost": Decimal("238.35"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB ARNI -50MG
    p_id_637 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000636")
    products[p_id_637] = {
        "id": p_id_637,
        "code": "MED-TABARNI5",
        "name": 'TAB ARNI -50MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("464.17"),
        "default_purchase_price": Decimal("371.34"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_637 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000637")
    batches[b_id_637] = {
        "id": b_id_637,
        "product_id": p_id_637,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 17),
        "purchase_cost": Decimal("371.34"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # TAB VILDAPRIDE 50MG
    p_id_638 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000637")
    products[p_id_638] = {
        "id": p_id_638,
        "code": "MED-TABVILDA",
        "name": 'TAB VILDAPRIDE 50MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("314.60"),
        "default_purchase_price": Decimal("251.68"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_638 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000638")
    batches[b_id_638] = {
        "id": b_id_638,
        "product_id": p_id_638,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 18),
        "purchase_cost": Decimal("251.68"),
        "quantity": 16,
        "is_active": True,
        "created_at": now,
    }

    # TAB METFLICS G2 TAB
    p_id_639 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000638")
    products[p_id_639] = {
        "id": p_id_639,
        "code": "MED-TABMETFL-1",
        "name": 'TAB METFLICS G2 TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("188.90"),
        "default_purchase_price": Decimal("151.12"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_639 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000639")
    batches[b_id_639] = {
        "id": b_id_639,
        "product_id": p_id_639,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 19),
        "purchase_cost": Decimal("151.12"),
        "quantity": 24,
        "is_active": True,
        "created_at": now,
    }

    # TAB S-AMPRO L
    p_id_640 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000639")
    products[p_id_640] = {
        "id": p_id_640,
        "code": "MED-TABSAMPR",
        "name": 'TAB S-AMPRO L',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("141.64"),
        "default_purchase_price": Decimal("113.31"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_640 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000640")
    batches[b_id_640] = {
        "id": b_id_640,
        "product_id": p_id_640,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 20),
        "purchase_cost": Decimal("113.31"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB DAPXIGA 10MG
    p_id_641 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000640")
    products[p_id_641] = {
        "id": p_id_641,
        "code": "MED-TABDAPXI",
        "name": 'TAB DAPXIGA 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("368.59"),
        "default_purchase_price": Decimal("294.87"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_641 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000641")
    batches[b_id_641] = {
        "id": b_id_641,
        "product_id": p_id_641,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 21),
        "purchase_cost": Decimal("294.87"),
        "quantity": 4,
        "is_active": True,
        "created_at": now,
    }

    # METFOR G2 -850
    p_id_642 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000641")
    products[p_id_642] = {
        "id": p_id_642,
        "code": "MED-METFORG2-1",
        "name": 'METFOR G2 -850',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("143.84"),
        "default_purchase_price": Decimal("115.07"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_642 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000642")
    batches[b_id_642] = {
        "id": b_id_642,
        "product_id": p_id_642,
        "batch_number": "BCH-MEDMET-27",
        "expiry_date": date(2027, 7, 22),
        "purchase_cost": Decimal("115.07"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELCLOR 6.25/40
    p_id_643 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000642")
    products[p_id_643] = {
        "id": p_id_643,
        "code": "MED-TABTELCL",
        "name": 'TAB TELCLOR 6.25/40',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("100.68"),
        "default_purchase_price": Decimal("80.54"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_643 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000643")
    batches[b_id_643] = {
        "id": b_id_643,
        "product_id": p_id_643,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 23),
        "purchase_cost": Decimal("80.54"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB WINCAL (250MG +200IU)
    p_id_644 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000643")
    products[p_id_644] = {
        "id": p_id_644,
        "code": "MED-TABWINCA",
        "name": 'TAB WINCAL (250MG +200IU)',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("112.39"),
        "default_purchase_price": Decimal("89.91"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_644 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000644")
    batches[b_id_644] = {
        "id": b_id_644,
        "product_id": p_id_644,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 24),
        "purchase_cost": Decimal("89.91"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # TAB ACLOV 400MG
    p_id_645 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000644")
    products[p_id_645] = {
        "id": p_id_645,
        "code": "MED-TABACLOV",
        "name": 'TAB ACLOV 400MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("204.36"),
        "default_purchase_price": Decimal("163.49"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_645 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000645")
    batches[b_id_645] = {
        "id": b_id_645,
        "product_id": p_id_645,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 25),
        "purchase_cost": Decimal("163.49"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB LINICS E10 MG
    p_id_646 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000645")
    products[p_id_646] = {
        "id": p_id_646,
        "code": "MED-TABLINIC-2",
        "name": 'TAB LINICS E10 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("431.89"),
        "default_purchase_price": Decimal("345.51"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_646 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000646")
    batches[b_id_646] = {
        "id": b_id_646,
        "product_id": p_id_646,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 26),
        "purchase_cost": Decimal("345.51"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB EMFOZI 10MG
    p_id_647 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000646")
    products[p_id_647] = {
        "id": p_id_647,
        "code": "MED-TABEMFOZ",
        "name": 'TAB EMFOZI 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("205.03"),
        "default_purchase_price": Decimal("164.02"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_647 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000647")
    batches[b_id_647] = {
        "id": b_id_647,
        "product_id": p_id_647,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 27),
        "purchase_cost": Decimal("164.02"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB EMFOZI 25MG
    p_id_648 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000647")
    products[p_id_648] = {
        "id": p_id_648,
        "code": "MED-TABEMFOZ-1",
        "name": 'TAB EMFOZI 25MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("492.09"),
        "default_purchase_price": Decimal("393.67"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_648 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000648")
    batches[b_id_648] = {
        "id": b_id_648,
        "product_id": p_id_648,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 1),
        "purchase_cost": Decimal("393.67"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB AMPRO L
    p_id_649 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000648")
    products[p_id_649] = {
        "id": p_id_649,
        "code": "MED-TABAMPRO",
        "name": 'TAB AMPRO L',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("133.28"),
        "default_purchase_price": Decimal("106.62"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_649 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000649")
    batches[b_id_649] = {
        "id": b_id_649,
        "product_id": p_id_649,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 2),
        "purchase_cost": Decimal("106.62"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB LIPTA M 850 IR
    p_id_650 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000649")
    products[p_id_650] = {
        "id": p_id_650,
        "code": "MED-TABLIPTA-1",
        "name": 'TAB LIPTA M 850 IR',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("154.08"),
        "default_purchase_price": Decimal("123.26"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_650 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000650")
    batches[b_id_650] = {
        "id": b_id_650,
        "product_id": p_id_650,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 3),
        "purchase_cost": Decimal("123.26"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB LINTOR M FORT SR 1000
    p_id_651 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000650")
    products[p_id_651] = {
        "id": p_id_651,
        "code": "MED-TABLINTO",
        "name": 'TAB LINTOR M FORT SR 1000',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("278.12"),
        "default_purchase_price": Decimal("222.50"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_651 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000651")
    batches[b_id_651] = {
        "id": b_id_651,
        "product_id": p_id_651,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 4),
        "purchase_cost": Decimal("222.50"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB METFLICF G2 FORT
    p_id_652 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000651")
    products[p_id_652] = {
        "id": p_id_652,
        "code": "MED-TABMETFL-2",
        "name": 'TAB METFLICF G2 FORT',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("170.86"),
        "default_purchase_price": Decimal("136.69"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_652 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000652")
    batches[b_id_652] = {
        "id": b_id_652,
        "product_id": p_id_652,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 5),
        "purchase_cost": Decimal("136.69"),
        "quantity": 18,
        "is_active": True,
        "created_at": now,
    }

    # TAB OLMAT 40 H
    p_id_653 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000652")
    products[p_id_653] = {
        "id": p_id_653,
        "code": "MED-TABOLMAT-1",
        "name": 'TAB OLMAT 40 H',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("809.10"),
        "default_purchase_price": Decimal("647.28"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_653 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000653")
    batches[b_id_653] = {
        "id": b_id_653,
        "product_id": p_id_653,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 6),
        "purchase_cost": Decimal("647.28"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB LOSAGEM 25MG
    p_id_654 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000653")
    products[p_id_654] = {
        "id": p_id_654,
        "code": "MED-TABLOSAG-1",
        "name": 'TAB LOSAGEM 25MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("45.86"),
        "default_purchase_price": Decimal("36.69"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_654 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000654")
    batches[b_id_654] = {
        "id": b_id_654,
        "product_id": p_id_654,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 7),
        "purchase_cost": Decimal("36.69"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

    # TAB FINERO 20MG
    p_id_655 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000654")
    products[p_id_655] = {
        "id": p_id_655,
        "code": "MED-TABFINER",
        "name": 'TAB FINERO 20MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("979.21"),
        "default_purchase_price": Decimal("783.37"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_655 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000655")
    batches[b_id_655] = {
        "id": b_id_655,
        "product_id": p_id_655,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 8),
        "purchase_cost": Decimal("783.37"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # SYRP DETUSS 100ML
    p_id_656 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000655")
    products[p_id_656] = {
        "id": p_id_656,
        "code": "MED-SYRPDETU",
        "name": 'SYRP DETUSS 100ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("110.50"),
        "default_purchase_price": Decimal("88.40"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_656 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000656")
    batches[b_id_656] = {
        "id": b_id_656,
        "product_id": p_id_656,
        "batch_number": "BCH-MEDSYR-27",
        "expiry_date": date(2027, 9, 9),
        "purchase_cost": Decimal("88.40"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # SYR HAEMOGEN 200ML
    p_id_657 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000656")
    products[p_id_657] = {
        "id": p_id_657,
        "code": "MED-SYRHAEMO",
        "name": 'SYR HAEMOGEN 200ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("87.42"),
        "default_purchase_price": Decimal("69.94"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_657 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000657")
    batches[b_id_657] = {
        "id": b_id_657,
        "product_id": p_id_657,
        "batch_number": "BCH-MEDSYR-28",
        "expiry_date": date(2028, 10, 10),
        "purchase_cost": Decimal("69.94"),
        "quantity": 7,
        "is_active": True,
        "created_at": now,
    }

    # TAB RABELOC 20MG
    p_id_658 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000657")
    products[p_id_658] = {
        "id": p_id_658,
        "code": "MED-TABRABEL",
        "name": 'TAB RABELOC 20MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("267.31"),
        "default_purchase_price": Decimal("213.85"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_658 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000658")
    batches[b_id_658] = {
        "id": b_id_658,
        "product_id": p_id_658,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 11),
        "purchase_cost": Decimal("213.85"),
        "quantity": 14,
        "is_active": True,
        "created_at": now,
    }

    # LINAMET 850MG TAB
    p_id_659 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000658")
    products[p_id_659] = {
        "id": p_id_659,
        "code": "MED-LINAMET8",
        "name": 'LINAMET 850MG TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("231.96"),
        "default_purchase_price": Decimal("185.57"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_659 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000659")
    batches[b_id_659] = {
        "id": b_id_659,
        "product_id": p_id_659,
        "batch_number": "BCH-MEDLIN-28",
        "expiry_date": date(2028, 12, 12),
        "purchase_cost": Decimal("185.57"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # SYRP OSTOVIT 200ML
    p_id_660 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000659")
    products[p_id_660] = {
        "id": p_id_660,
        "code": "MED-SYRPOSTO",
        "name": 'SYRP OSTOVIT 200ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("97.93"),
        "default_purchase_price": Decimal("78.34"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_660 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000660")
    batches[b_id_660] = {
        "id": b_id_660,
        "product_id": p_id_660,
        "batch_number": "BCH-MEDSYR-27",
        "expiry_date": date(2027, 1, 13),
        "purchase_cost": Decimal("78.34"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB CETOZONE FORT
    p_id_661 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000660")
    products[p_id_661] = {
        "id": p_id_661,
        "code": "MED-TABCETOZ",
        "name": 'TAB CETOZONE FORT',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("40.80"),
        "default_purchase_price": Decimal("32.64"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_661 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000661")
    batches[b_id_661] = {
        "id": b_id_661,
        "product_id": p_id_661,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 14),
        "purchase_cost": Decimal("32.64"),
        "quantity": 30,
        "is_active": True,
        "created_at": now,
    }

    # SAMPOO KETANOL 2% 30ML
    p_id_662 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000661")
    products[p_id_662] = {
        "id": p_id_662,
        "code": "MED-SAMPOOKE",
        "name": 'SAMPOO KETANOL 2% 30ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("232.03"),
        "default_purchase_price": Decimal("185.62"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_662 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000662")
    batches[b_id_662] = {
        "id": b_id_662,
        "product_id": p_id_662,
        "batch_number": "BCH-MEDSAM-27",
        "expiry_date": date(2027, 3, 15),
        "purchase_cost": Decimal("185.62"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB PRONAL 10MG
    p_id_663 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000662")
    products[p_id_663] = {
        "id": p_id_663,
        "code": "MED-TABPRONA",
        "name": 'TAB PRONAL 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("41.28"),
        "default_purchase_price": Decimal("33.02"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_663 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000663")
    batches[b_id_663] = {
        "id": b_id_663,
        "product_id": p_id_663,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 16),
        "purchase_cost": Decimal("33.02"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB EMPADAY 10MG
    p_id_664 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000663")
    products[p_id_664] = {
        "id": p_id_664,
        "code": "MED-TABEMPAD",
        "name": 'TAB EMPADAY 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("206.29"),
        "default_purchase_price": Decimal("165.03"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_664 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000664")
    batches[b_id_664] = {
        "id": b_id_664,
        "product_id": p_id_664,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 17),
        "purchase_cost": Decimal("165.03"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB LINAMET 500IR
    p_id_665 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000664")
    products[p_id_665] = {
        "id": p_id_665,
        "code": "MED-TABLINAM-1",
        "name": 'TAB LINAMET 500IR',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("213.35"),
        "default_purchase_price": Decimal("170.68"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_665 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000665")
    batches[b_id_665] = {
        "id": b_id_665,
        "product_id": p_id_665,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 18),
        "purchase_cost": Decimal("170.68"),
        "quantity": 33,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELCLOR 6.25/80
    p_id_666 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000665")
    products[p_id_666] = {
        "id": p_id_666,
        "code": "MED-TABTELCL-1",
        "name": 'TAB TELCLOR 6.25/80',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("144.04"),
        "default_purchase_price": Decimal("115.23"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_666 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000666")
    batches[b_id_666] = {
        "id": b_id_666,
        "product_id": p_id_666,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 19),
        "purchase_cost": Decimal("115.23"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB TENEPRIDE M 1000MG
    p_id_667 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000666")
    products[p_id_667] = {
        "id": p_id_667,
        "code": "MED-TABTENEP-1",
        "name": 'TAB TENEPRIDE M 1000MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("438.33"),
        "default_purchase_price": Decimal("350.66"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_667 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000667")
    batches[b_id_667] = {
        "id": b_id_667,
        "product_id": p_id_667,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 20),
        "purchase_cost": Decimal("350.66"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB REXTER 100MG
    p_id_668 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000667")
    products[p_id_668] = {
        "id": p_id_668,
        "code": "MED-TABREXTE-1",
        "name": 'TAB REXTER 100MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("431.97"),
        "default_purchase_price": Decimal("345.58"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_668 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000668")
    batches[b_id_668] = {
        "id": b_id_668,
        "product_id": p_id_668,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 21),
        "purchase_cost": Decimal("345.58"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB NEUROPEN M50
    p_id_669 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000668")
    products[p_id_669] = {
        "id": p_id_669,
        "code": "MED-TABNEURO",
        "name": 'TAB NEUROPEN M50',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("258.66"),
        "default_purchase_price": Decimal("206.93"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_669 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000669")
    batches[b_id_669] = {
        "id": b_id_669,
        "product_id": p_id_669,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 22),
        "purchase_cost": Decimal("206.93"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB NEUROPEN M75
    p_id_670 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000669")
    products[p_id_670] = {
        "id": p_id_670,
        "code": "MED-TABNEURO-1",
        "name": 'TAB NEUROPEN M75',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("331.09"),
        "default_purchase_price": Decimal("264.87"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_670 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000670")
    batches[b_id_670] = {
        "id": b_id_670,
        "product_id": p_id_670,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 23),
        "purchase_cost": Decimal("264.87"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB THYRONICS 100MCG
    p_id_671 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000670")
    products[p_id_671] = {
        "id": p_id_671,
        "code": "MED-TABTHYRO",
        "name": 'TAB THYRONICS 100MCG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("262.18"),
        "default_purchase_price": Decimal("209.74"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_671 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000671")
    batches[b_id_671] = {
        "id": b_id_671,
        "product_id": p_id_671,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 24),
        "purchase_cost": Decimal("209.74"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # SYP D-KOF
    p_id_672 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000671")
    products[p_id_672] = {
        "id": p_id_672,
        "code": "MED-SYPDKOF",
        "name": 'SYP D-KOF',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("71.54"),
        "default_purchase_price": Decimal("57.23"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_672 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000672")
    batches[b_id_672] = {
        "id": b_id_672,
        "product_id": p_id_672,
        "batch_number": "BCH-MEDSYP-27",
        "expiry_date": date(2027, 1, 25),
        "purchase_cost": Decimal("57.23"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELCLOR 12.5/40
    p_id_673 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000672")
    products[p_id_673] = {
        "id": p_id_673,
        "code": "MED-TABTELCL-2",
        "name": 'TAB TELCLOR 12.5/40',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("111.58"),
        "default_purchase_price": Decimal("89.26"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_673 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000673")
    batches[b_id_673] = {
        "id": b_id_673,
        "product_id": p_id_673,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 26),
        "purchase_cost": Decimal("89.26"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB EMPADAY 25MG
    p_id_674 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000673")
    products[p_id_674] = {
        "id": p_id_674,
        "code": "MED-TABEMPAD-1",
        "name": 'TAB EMPADAY 25MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("309.01"),
        "default_purchase_price": Decimal("247.21"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_674 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000674")
    batches[b_id_674] = {
        "id": b_id_674,
        "product_id": p_id_674,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 27),
        "purchase_cost": Decimal("247.21"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB DAPA 5MG
    p_id_675 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000674")
    products[p_id_675] = {
        "id": p_id_675,
        "code": "MED-TABDAPA5",
        "name": 'TAB DAPA 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("174.03"),
        "default_purchase_price": Decimal("139.22"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_675 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000675")
    batches[b_id_675] = {
        "id": b_id_675,
        "product_id": p_id_675,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 1),
        "purchase_cost": Decimal("139.22"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # TAB THYRONICS 88
    p_id_676 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000675")
    products[p_id_676] = {
        "id": p_id_676,
        "code": "MED-TABTHYRO-1",
        "name": 'TAB THYRONICS 88',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("339.10"),
        "default_purchase_price": Decimal("271.28"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_676 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000676")
    batches[b_id_676] = {
        "id": b_id_676,
        "product_id": p_id_676,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 2),
        "purchase_cost": Decimal("271.28"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELSARTAN CT 40/12.5
    p_id_677 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000676")
    products[p_id_677] = {
        "id": p_id_677,
        "code": "MED-TABTELSA-3",
        "name": 'TAB TELSARTAN CT 40/12.5',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("113.04"),
        "default_purchase_price": Decimal("90.43"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_677 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000677")
    batches[b_id_677] = {
        "id": b_id_677,
        "product_id": p_id_677,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 3),
        "purchase_cost": Decimal("90.43"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # PANTOTAB TAB
    p_id_678 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000677")
    products[p_id_678] = {
        "id": p_id_678,
        "code": "MED-PANTOTAB-1",
        "name": 'PANTOTAB TAB',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("105.24"),
        "default_purchase_price": Decimal("84.19"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_678 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000678")
    batches[b_id_678] = {
        "id": b_id_678,
        "product_id": p_id_678,
        "batch_number": "BCH-MEDPAN-27",
        "expiry_date": date(2027, 7, 4),
        "purchase_cost": Decimal("84.19"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB MYLOD AT H
    p_id_679 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000678")
    products[p_id_679] = {
        "id": p_id_679,
        "code": "MED-TABMYLOD",
        "name": 'TAB MYLOD AT H',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("102.62"),
        "default_purchase_price": Decimal("82.10"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_679 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000679")
    batches[b_id_679] = {
        "id": b_id_679,
        "product_id": p_id_679,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 5),
        "purchase_cost": Decimal("82.10"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB LIPTA M 850
    p_id_680 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000679")
    products[p_id_680] = {
        "id": p_id_680,
        "code": "MED-TABLIPTA-2",
        "name": 'TAB LIPTA M 850',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("152.31"),
        "default_purchase_price": Decimal("121.85"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_680 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000680")
    batches[b_id_680] = {
        "id": b_id_680,
        "product_id": p_id_680,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 6),
        "purchase_cost": Decimal("121.85"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB FLUGRAN 10MG
    p_id_681 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000680")
    products[p_id_681] = {
        "id": p_id_681,
        "code": "MED-TABFLUGR",
        "name": 'TAB FLUGRAN 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("76.17"),
        "default_purchase_price": Decimal("60.94"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_681 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000681")
    batches[b_id_681] = {
        "id": b_id_681,
        "product_id": p_id_681,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 7),
        "purchase_cost": Decimal("60.94"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # YAB STAYCALM PLUS
    p_id_682 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000681")
    products[p_id_682] = {
        "id": p_id_682,
        "code": "MED-YABSTAYC",
        "name": 'YAB STAYCALM PLUS',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("56.88"),
        "default_purchase_price": Decimal("45.50"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_682 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000682")
    batches[b_id_682] = {
        "id": b_id_682,
        "product_id": p_id_682,
        "batch_number": "BCH-MEDYAB-27",
        "expiry_date": date(2027, 11, 8),
        "purchase_cost": Decimal("45.50"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB PROATE 200 MG
    p_id_683 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000682")
    products[p_id_683] = {
        "id": p_id_683,
        "code": "MED-TABPROAT",
        "name": 'TAB PROATE 200 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("71.08"),
        "default_purchase_price": Decimal("56.86"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_683 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000683")
    batches[b_id_683] = {
        "id": b_id_683,
        "product_id": p_id_683,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 9),
        "purchase_cost": Decimal("56.86"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB PROATE 300MG
    p_id_684 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000683")
    products[p_id_684] = {
        "id": p_id_684,
        "code": "MED-TABPROAT-1",
        "name": 'TAB PROATE 300MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("101.56"),
        "default_purchase_price": Decimal("81.25"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_684 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000684")
    batches[b_id_684] = {
        "id": b_id_684,
        "product_id": p_id_684,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 10),
        "purchase_cost": Decimal("81.25"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB PROATE 500 MG
    p_id_685 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000684")
    products[p_id_685] = {
        "id": p_id_685,
        "code": "MED-TABPROAT-2",
        "name": 'TAB PROATE 500 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("162.46"),
        "default_purchase_price": Decimal("129.97"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_685 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000685")
    batches[b_id_685] = {
        "id": b_id_685,
        "product_id": p_id_685,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 11),
        "purchase_cost": Decimal("129.97"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # SYR PROATE OS 200ML
    p_id_686 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000685")
    products[p_id_686] = {
        "id": p_id_686,
        "code": "MED-SYRPROAT",
        "name": 'SYR PROATE OS 200ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("203.06"),
        "default_purchase_price": Decimal("162.45"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_686 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000686")
    batches[b_id_686] = {
        "id": b_id_686,
        "product_id": p_id_686,
        "batch_number": "BCH-MEDSYR-27",
        "expiry_date": date(2027, 3, 12),
        "purchase_cost": Decimal("162.45"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB ES - PRAM 20 MG
    p_id_687 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000686")
    products[p_id_687] = {
        "id": p_id_687,
        "code": "MED-TABESPRA",
        "name": 'TAB ES - PRAM 20 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("263.95"),
        "default_purchase_price": Decimal("211.16"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_687 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000687")
    batches[b_id_687] = {
        "id": b_id_687,
        "product_id": p_id_687,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 13),
        "purchase_cost": Decimal("211.16"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB OLZAP 10 MG
    p_id_688 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000687")
    products[p_id_688] = {
        "id": p_id_688,
        "code": "MED-TABOLZAP",
        "name": 'TAB OLZAP 10 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("101.53"),
        "default_purchase_price": Decimal("81.22"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_688 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000688")
    batches[b_id_688] = {
        "id": b_id_688,
        "product_id": p_id_688,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 14),
        "purchase_cost": Decimal("81.22"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB PENISOL -VK
    p_id_689 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000688")
    products[p_id_689] = {
        "id": p_id_689,
        "code": "MED-TABPENIS",
        "name": 'TAB PENISOL -VK',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("60.91"),
        "default_purchase_price": Decimal("48.73"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_689 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000689")
    batches[b_id_689] = {
        "id": b_id_689,
        "product_id": p_id_689,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 15),
        "purchase_cost": Decimal("48.73"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB MYPRESS -L
    p_id_690 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000689")
    products[p_id_690] = {
        "id": p_id_690,
        "code": "MED-TABMYPRE",
        "name": 'TAB MYPRESS -L',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("131.99"),
        "default_purchase_price": Decimal("105.59"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_690 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000690")
    batches[b_id_690] = {
        "id": b_id_690,
        "product_id": p_id_690,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 16),
        "purchase_cost": Decimal("105.59"),
        "quantity": 8,
        "is_active": True,
        "created_at": now,
    }

    # TAB AMFAST 5
    p_id_691 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000690")
    products[p_id_691] = {
        "id": p_id_691,
        "code": "MED-TABAMFAS",
        "name": 'TAB AMFAST 5',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("50.80"),
        "default_purchase_price": Decimal("40.64"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_691 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000691")
    batches[b_id_691] = {
        "id": b_id_691,
        "product_id": p_id_691,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 17),
        "purchase_cost": Decimal("40.64"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB LIPTA M 500
    p_id_692 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000691")
    products[p_id_692] = {
        "id": p_id_692,
        "code": "MED-TABLIPTA-3",
        "name": 'TAB LIPTA M 500',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("142.16"),
        "default_purchase_price": Decimal("113.73"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_692 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000692")
    batches[b_id_692] = {
        "id": b_id_692,
        "product_id": p_id_692,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 18),
        "purchase_cost": Decimal("113.73"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB ROSUVAST 5MG
    p_id_693 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000692")
    products[p_id_693] = {
        "id": p_id_693,
        "code": "MED-TABROSUV",
        "name": 'TAB ROSUVAST 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("111.69"),
        "default_purchase_price": Decimal("89.35"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_693 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000693")
    batches[b_id_693] = {
        "id": b_id_693,
        "product_id": p_id_693,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 19),
        "purchase_cost": Decimal("89.35"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB ROSUVAST 10 MG
    p_id_694 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000693")
    products[p_id_694] = {
        "id": p_id_694,
        "code": "MED-TABROSUV-1",
        "name": 'TAB ROSUVAST 10 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("203.06"),
        "default_purchase_price": Decimal("162.45"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_694 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000694")
    batches[b_id_694] = {
        "id": b_id_694,
        "product_id": p_id_694,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 20),
        "purchase_cost": Decimal("162.45"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB NETFORMIN G2 FORTE
    p_id_695 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000694")
    products[p_id_695] = {
        "id": p_id_695,
        "code": "MED-TABNETFO",
        "name": 'TAB NETFORMIN G2 FORTE',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("157.38"),
        "default_purchase_price": Decimal("125.90"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_695 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000695")
    batches[b_id_695] = {
        "id": b_id_695,
        "product_id": p_id_695,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 21),
        "purchase_cost": Decimal("125.90"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB NETFORMIN   G1 FORTE
    p_id_696 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000695")
    products[p_id_696] = {
        "id": p_id_696,
        "code": "MED-TABNETFO-1",
        "name": 'TAB NETFORMIN   G1 FORTE',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("111.69"),
        "default_purchase_price": Decimal("89.35"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_696 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000696")
    batches[b_id_696] = {
        "id": b_id_696,
        "product_id": p_id_696,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 22),
        "purchase_cost": Decimal("89.35"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # DOLOFEN GEL 30 GM
    p_id_697 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000696")
    products[p_id_697] = {
        "id": p_id_697,
        "code": "MED-DOLOFENG",
        "name": 'DOLOFEN GEL 30 GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("152.31"),
        "default_purchase_price": Decimal("121.85"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_697 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000697")
    batches[b_id_697] = {
        "id": b_id_697,
        "product_id": p_id_697,
        "batch_number": "BCH-MEDDOL-28",
        "expiry_date": date(2028, 2, 23),
        "purchase_cost": Decimal("121.85"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB RELIEF
    p_id_698 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000697")
    products[p_id_698] = {
        "id": p_id_698,
        "code": "MED-TABRELIE",
        "name": 'TAB RELIEF',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("20.31"),
        "default_purchase_price": Decimal("16.25"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_698 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000698")
    batches[b_id_698] = {
        "id": b_id_698,
        "product_id": p_id_698,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 24),
        "purchase_cost": Decimal("16.25"),
        "quantity": 50,
        "is_active": True,
        "created_at": now,
    }

    # TAB PANSAM D
    p_id_699 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000698")
    products[p_id_699] = {
        "id": p_id_699,
        "code": "MED-TABPANSA",
        "name": 'TAB PANSAM D',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("162.46"),
        "default_purchase_price": Decimal("129.97"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_699 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000699")
    batches[b_id_699] = {
        "id": b_id_699,
        "product_id": p_id_699,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 25),
        "purchase_cost": Decimal("129.97"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB PANTAFAST 40 MG
    p_id_700 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000699")
    products[p_id_700] = {
        "id": p_id_700,
        "code": "MED-TABPANTA",
        "name": 'TAB PANTAFAST 40 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("81.24"),
        "default_purchase_price": Decimal("64.99"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_700 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000700")
    batches[b_id_700] = {
        "id": b_id_700,
        "product_id": p_id_700,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 26),
        "purchase_cost": Decimal("64.99"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # TAB DAFODIL M XR 10/1G
    p_id_701 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000700")
    products[p_id_701] = {
        "id": p_id_701,
        "code": "MED-TABDAFOD-1",
        "name": 'TAB DAFODIL M XR 10/1G',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("310.48"),
        "default_purchase_price": Decimal("248.38"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_701 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000701")
    batches[b_id_701] = {
        "id": b_id_701,
        "product_id": p_id_701,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 27),
        "purchase_cost": Decimal("248.38"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TA DAFODIL M XR 10/500
    p_id_702 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000701")
    products[p_id_702] = {
        "id": p_id_702,
        "code": "MED-TADAFODI",
        "name": 'TA DAFODIL M XR 10/500',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("279.44"),
        "default_purchase_price": Decimal("223.55"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_702 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000702")
    batches[b_id_702] = {
        "id": b_id_702,
        "product_id": p_id_702,
        "batch_number": "BCH-MEDTAD-27",
        "expiry_date": date(2027, 7, 1),
        "purchase_cost": Decimal("223.55"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB DAFODIL M XL 5/500
    p_id_703 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000702")
    products[p_id_703] = {
        "id": p_id_703,
        "code": "MED-TABDAFOD-2",
        "name": 'TAB DAFODIL M XL 5/500',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("206.99"),
        "default_purchase_price": Decimal("165.59"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_703 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000703")
    batches[b_id_703] = {
        "id": b_id_703,
        "product_id": p_id_703,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 2),
        "purchase_cost": Decimal("165.59"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB DAFODIL M XL 5/1G
    p_id_704 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000703")
    products[p_id_704] = {
        "id": p_id_704,
        "code": "MED-TABDAFOD-3",
        "name": 'TAB DAFODIL M XL 5/1G',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("238.04"),
        "default_purchase_price": Decimal("190.43"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_704 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000704")
    batches[b_id_704] = {
        "id": b_id_704,
        "product_id": p_id_704,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 3),
        "purchase_cost": Decimal("190.43"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB VECOXIB 60
    p_id_705 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000704")
    products[p_id_705] = {
        "id": p_id_705,
        "code": "MED-TABVECOX-2",
        "name": 'TAB VECOXIB 60',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("202.99"),
        "default_purchase_price": Decimal("162.39"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_705 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000705")
    batches[b_id_705] = {
        "id": b_id_705,
        "product_id": p_id_705,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 4),
        "purchase_cost": Decimal("162.39"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB AZIREST -500MG
    p_id_706 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000705")
    products[p_id_706] = {
        "id": p_id_706,
        "code": "MED-TABAZIRE",
        "name": 'TAB AZIREST -500MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("75.97"),
        "default_purchase_price": Decimal("60.78"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_706 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000706")
    batches[b_id_706] = {
        "id": b_id_706,
        "product_id": p_id_706,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 5),
        "purchase_cost": Decimal("60.78"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # TAB IRGONOL -100MG
    p_id_707 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000706")
    products[p_id_707] = {
        "id": p_id_707,
        "code": "MED-TABIRGON",
        "name": 'TAB IRGONOL -100MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("81.02"),
        "default_purchase_price": Decimal("64.82"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_707 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000707")
    batches[b_id_707] = {
        "id": b_id_707,
        "product_id": p_id_707,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 6),
        "purchase_cost": Decimal("64.82"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELMI 80 AM
    p_id_708 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000707")
    products[p_id_708] = {
        "id": p_id_708,
        "code": "MED-TABTELMI",
        "name": 'TAB TELMI 80 AM',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("253.21"),
        "default_purchase_price": Decimal("202.57"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_708 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000708")
    batches[b_id_708] = {
        "id": b_id_708,
        "product_id": p_id_708,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 7),
        "purchase_cost": Decimal("202.57"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB FORMIN SR 1000 MG
    p_id_709 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000708")
    products[p_id_709] = {
        "id": p_id_709,
        "code": "MED-TABFORMI",
        "name": 'TAB FORMIN SR 1000 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("60.80"),
        "default_purchase_price": Decimal("48.64"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_709 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000709")
    batches[b_id_709] = {
        "id": b_id_709,
        "product_id": p_id_709,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 8),
        "purchase_cost": Decimal("48.64"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB FORMIN SR 500
    p_id_710 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000709")
    products[p_id_710] = {
        "id": p_id_710,
        "code": "MED-TABFORMI-1",
        "name": 'TAB FORMIN SR 500',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("35.48"),
        "default_purchase_price": Decimal("28.38"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_710 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000710")
    batches[b_id_710] = {
        "id": b_id_710,
        "product_id": p_id_710,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 9),
        "purchase_cost": Decimal("28.38"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB SITAMET SR 1000
    p_id_711 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000710")
    products[p_id_711] = {
        "id": p_id_711,
        "code": "MED-TABSITAM-1",
        "name": 'TAB SITAMET SR 1000',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("293.75"),
        "default_purchase_price": Decimal("235.00"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_711 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000711")
    batches[b_id_711] = {
        "id": b_id_711,
        "product_id": p_id_711,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 10),
        "purchase_cost": Decimal("235.00"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB TRIPLIN 10MG
    p_id_712 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000711")
    products[p_id_712] = {
        "id": p_id_712,
        "code": "MED-TABTRIPL",
        "name": 'TAB TRIPLIN 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("34.05"),
        "default_purchase_price": Decimal("27.24"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_712 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000712")
    batches[b_id_712] = {
        "id": b_id_712,
        "product_id": p_id_712,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 11),
        "purchase_cost": Decimal("27.24"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # TAB METHAPRED 16MG
    p_id_713 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000712")
    products[p_id_713] = {
        "id": p_id_713,
        "code": "MED-TABMETHA",
        "name": 'TAB METHAPRED 16MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("222.41"),
        "default_purchase_price": Decimal("177.93"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_713 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000713")
    batches[b_id_713] = {
        "id": b_id_713,
        "product_id": p_id_713,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 12),
        "purchase_cost": Decimal("177.93"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB METHAPRED 4MG
    p_id_714 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000713")
    products[p_id_714] = {
        "id": p_id_714,
        "code": "MED-TABMETHA-1",
        "name": 'TAB METHAPRED 4MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("80.86"),
        "default_purchase_price": Decimal("64.69"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_714 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000714")
    batches[b_id_714] = {
        "id": b_id_714,
        "product_id": p_id_714,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 13),
        "purchase_cost": Decimal("64.69"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # TAB METHAPRED 8MG
    p_id_715 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000714")
    products[p_id_715] = {
        "id": p_id_715,
        "code": "MED-TABMETHA-2",
        "name": 'TAB METHAPRED 8MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("111.23"),
        "default_purchase_price": Decimal("88.98"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_715 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000715")
    batches[b_id_715] = {
        "id": b_id_715,
        "product_id": p_id_715,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 14),
        "purchase_cost": Decimal("88.98"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # CAP OMNIPLEX
    p_id_716 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000715")
    products[p_id_716] = {
        "id": p_id_716,
        "code": "MED-CAPOMNIP",
        "name": 'CAP OMNIPLEX',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("42.11"),
        "default_purchase_price": Decimal("33.69"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_716 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000716")
    batches[b_id_716] = {
        "id": b_id_716,
        "product_id": p_id_716,
        "batch_number": "BCH-MEDCAP-27",
        "expiry_date": date(2027, 9, 15),
        "purchase_cost": Decimal("33.69"),
        "quantity": 24,
        "is_active": True,
        "created_at": now,
    }

    # TAB HYOSPAN
    p_id_717 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000716")
    products[p_id_717] = {
        "id": p_id_717,
        "code": "MED-TABHYOSP",
        "name": 'TAB HYOSPAN',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("110.30"),
        "default_purchase_price": Decimal("88.24"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_717 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000717")
    batches[b_id_717] = {
        "id": b_id_717,
        "product_id": p_id_717,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 16),
        "purchase_cost": Decimal("88.24"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # TAB PRESIN L
    p_id_718 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000717")
    products[p_id_718] = {
        "id": p_id_718,
        "code": "MED-TABPRESI",
        "name": 'TAB PRESIN L',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("181.96"),
        "default_purchase_price": Decimal("145.57"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_718 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000718")
    batches[b_id_718] = {
        "id": b_id_718,
        "product_id": p_id_718,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 17),
        "purchase_cost": Decimal("145.57"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # SYRP BHASKARZYME 100 ML
    p_id_719 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000718")
    products[p_id_719] = {
        "id": p_id_719,
        "code": "MED-SYRPBHAS",
        "name": 'SYRP BHASKARZYME 100 ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("126.36"),
        "default_purchase_price": Decimal("101.09"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_719 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000719")
    batches[b_id_719] = {
        "id": b_id_719,
        "product_id": p_id_719,
        "batch_number": "BCH-MEDSYR-28",
        "expiry_date": date(2028, 12, 18),
        "purchase_cost": Decimal("101.09"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # SYRP BHASKARZYME 200ML
    p_id_720 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000719")
    products[p_id_720] = {
        "id": p_id_720,
        "code": "MED-SYRPBHAS-1",
        "name": 'SYRP BHASKARZYME 200ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("214.83"),
        "default_purchase_price": Decimal("171.86"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_720 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000720")
    batches[b_id_720] = {
        "id": b_id_720,
        "product_id": p_id_720,
        "batch_number": "BCH-MEDSYR-27",
        "expiry_date": date(2027, 1, 19),
        "purchase_cost": Decimal("171.86"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # BHASKARZYME DROP
    p_id_721 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000720")
    products[p_id_721] = {
        "id": p_id_721,
        "code": "MED-BHASKARZ",
        "name": 'BHASKARZYME DROP',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("101.09"),
        "default_purchase_price": Decimal("80.87"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_721 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000721")
    batches[b_id_721] = {
        "id": b_id_721,
        "product_id": p_id_721,
        "batch_number": "BCH-MEDBHA-28",
        "expiry_date": date(2028, 2, 20),
        "purchase_cost": Decimal("80.87"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # LAXOFT  POWDER
    p_id_722 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000721")
    products[p_id_722] = {
        "id": p_id_722,
        "code": "MED-LAXOFTPO",
        "name": 'LAXOFT  POWDER',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("236.55"),
        "default_purchase_price": Decimal("189.24"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_722 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000722")
    batches[b_id_722] = {
        "id": b_id_722,
        "product_id": p_id_722,
        "batch_number": "BCH-MEDLAX-27",
        "expiry_date": date(2027, 3, 21),
        "purchase_cost": Decimal("189.24"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # LAXOFT -SF 100MG POWDER
    p_id_723 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000722")
    products[p_id_723] = {
        "id": p_id_723,
        "code": "MED-LAXOFTSF",
        "name": 'LAXOFT -SF 100MG POWDER',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("282.04"),
        "default_purchase_price": Decimal("225.63"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_723 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000723")
    batches[b_id_723] = {
        "id": b_id_723,
        "product_id": p_id_723,
        "batch_number": "BCH-MEDLAX-28",
        "expiry_date": date(2028, 4, 22),
        "purchase_cost": Decimal("225.63"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # SYRP FEMICORDIAL FORT 450ML
    p_id_724 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000723")
    products[p_id_724] = {
        "id": p_id_724,
        "code": "MED-SYRPFEMI",
        "name": 'SYRP FEMICORDIAL FORT 450ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("517.02"),
        "default_purchase_price": Decimal("413.62"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_724 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000724")
    batches[b_id_724] = {
        "id": b_id_724,
        "product_id": p_id_724,
        "batch_number": "BCH-MEDSYR-27",
        "expiry_date": date(2027, 5, 23),
        "purchase_cost": Decimal("413.62"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # SYRP AMYCORDIAL 450ML
    p_id_725 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000724")
    products[p_id_725] = {
        "id": p_id_725,
        "code": "MED-SYRPAMYC",
        "name": 'SYRP AMYCORDIAL 450ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("492.88"),
        "default_purchase_price": Decimal("394.30"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_725 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000725")
    batches[b_id_725] = {
        "id": b_id_725,
        "product_id": p_id_725,
        "batch_number": "BCH-MEDSYR-28",
        "expiry_date": date(2028, 6, 24),
        "purchase_cost": Decimal("394.30"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # SEBO SHILED F/W 100ML
    p_id_726 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000725")
    products[p_id_726] = {
        "id": p_id_726,
        "code": "MED-SEBOSHIL",
        "name": 'SEBO SHILED F/W 100ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("402.66"),
        "default_purchase_price": Decimal("322.13"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_726 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000726")
    batches[b_id_726] = {
        "id": b_id_726,
        "product_id": p_id_726,
        "batch_number": "BCH-MEDSEB-27",
        "expiry_date": date(2027, 7, 25),
        "purchase_cost": Decimal("322.13"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # BETAVET N 20GM
    p_id_727 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000726")
    products[p_id_727] = {
        "id": p_id_727,
        "code": "MED-BETAVETN",
        "name": 'BETAVET N 20GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("51.71"),
        "default_purchase_price": Decimal("41.37"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_727 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000727")
    batches[b_id_727] = {
        "id": b_id_727,
        "product_id": p_id_727,
        "batch_number": "BCH-MEDBET-28",
        "expiry_date": date(2028, 8, 26),
        "purchase_cost": Decimal("41.37"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB RIVOXAN 20MG
    p_id_728 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000727")
    products[p_id_728] = {
        "id": p_id_728,
        "code": "MED-TABRIVOX",
        "name": 'TAB RIVOXAN 20MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("982.26"),
        "default_purchase_price": Decimal("785.81"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_728 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000728")
    batches[b_id_728] = {
        "id": b_id_728,
        "product_id": p_id_728,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 27),
        "purchase_cost": Decimal("785.81"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB ALPINE -LH
    p_id_729 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000728")
    products[p_id_729] = {
        "id": p_id_729,
        "code": "MED-TABALPIN",
        "name": 'TAB ALPINE -LH',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("83.32"),
        "default_purchase_price": Decimal("66.66"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_729 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000729")
    batches[b_id_729] = {
        "id": b_id_729,
        "product_id": p_id_729,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 1),
        "purchase_cost": Decimal("66.66"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # MELACARE 15GM CREM
    p_id_730 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000729")
    products[p_id_730] = {
        "id": p_id_730,
        "code": "MED-MELACARE",
        "name": 'MELACARE 15GM CREM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("238.51"),
        "default_purchase_price": Decimal("190.81"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_730 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000730")
    batches[b_id_730] = {
        "id": b_id_730,
        "product_id": p_id_730,
        "batch_number": "BCH-MEDMEL-27",
        "expiry_date": date(2027, 11, 2),
        "purchase_cost": Decimal("190.81"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # ADACLIN GEL
    p_id_731 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000730")
    products[p_id_731] = {
        "id": p_id_731,
        "code": "MED-ADACLING",
        "name": 'ADACLIN GEL',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("166.94"),
        "default_purchase_price": Decimal("133.55"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_731 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000731")
    batches[b_id_731] = {
        "id": b_id_731,
        "product_id": p_id_731,
        "batch_number": "BCH-MEDADA-28",
        "expiry_date": date(2028, 12, 3),
        "purchase_cost": Decimal("133.55"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB ETAPRAM P 0.25MG
    p_id_732 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000731")
    products[p_id_732] = {
        "id": p_id_732,
        "code": "MED-TABETAPR",
        "name": 'TAB ETAPRAM P 0.25MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("135.28"),
        "default_purchase_price": Decimal("108.22"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_732 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000732")
    batches[b_id_732] = {
        "id": b_id_732,
        "product_id": p_id_732,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 4),
        "purchase_cost": Decimal("108.22"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB LOSANGI 50 MG
    p_id_733 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000732")
    products[p_id_733] = {
        "id": p_id_733,
        "code": "MED-TABLOSAN",
        "name": 'TAB LOSANGI 50 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("118.65"),
        "default_purchase_price": Decimal("94.92"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_733 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000733")
    batches[b_id_733] = {
        "id": b_id_733,
        "product_id": p_id_733,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 5),
        "purchase_cost": Decimal("94.92"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # DSM GEL 30GM CREAM
    p_id_734 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000733")
    products[p_id_734] = {
        "id": p_id_734,
        "code": "MED-DSMGEL30",
        "name": 'DSM GEL 30GM CREAM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("111.50"),
        "default_purchase_price": Decimal("89.20"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_734 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000734")
    batches[b_id_734] = {
        "id": b_id_734,
        "product_id": p_id_734,
        "batch_number": "BCH-MEDDSM-27",
        "expiry_date": date(2027, 3, 6),
        "purchase_cost": Decimal("89.20"),
        "quantity": 7,
        "is_active": True,
        "created_at": now,
    }

    # ING MAXICEF 250 MG
    p_id_735 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000734")
    products[p_id_735] = {
        "id": p_id_735,
        "code": "MED-INGMAXIC",
        "name": 'ING MAXICEF 250 MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("196.31"),
        "default_purchase_price": Decimal("157.05"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_735 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000735")
    batches[b_id_735] = {
        "id": b_id_735,
        "product_id": p_id_735,
        "batch_number": "BCH-MEDING-28",
        "expiry_date": date(2028, 4, 7),
        "purchase_cost": Decimal("157.05"),
        "quantity": 13,
        "is_active": True,
        "created_at": now,
    }

    # ING MAXICEF 1GM
    p_id_736 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000735")
    products[p_id_736] = {
        "id": p_id_736,
        "code": "MED-INGMAXIC-1",
        "name": 'ING MAXICEF 1GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("457.34"),
        "default_purchase_price": Decimal("365.87"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_736 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000736")
    batches[b_id_736] = {
        "id": b_id_736,
        "product_id": p_id_736,
        "batch_number": "BCH-MEDING-27",
        "expiry_date": date(2027, 5, 8),
        "purchase_cost": Decimal("365.87"),
        "quantity": 7,
        "is_active": True,
        "created_at": now,
    }

    # TAB THYROX 125
    p_id_737 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000736")
    products[p_id_737] = {
        "id": p_id_737,
        "code": "MED-TABTHYRO-2",
        "name": 'TAB THYROX 125',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("381.39"),
        "default_purchase_price": Decimal("305.11"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_737 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000737")
    batches[b_id_737] = {
        "id": b_id_737,
        "product_id": p_id_737,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 9),
        "purchase_cost": Decimal("305.11"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB THYROX 150 MG
    p_id_738 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000737")
    products[p_id_738] = {
        "id": p_id_738,
        "code": "MED-TABTHYRO-3",
        "name": 'TAB THYROX 150 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("383.65"),
        "default_purchase_price": Decimal("306.92"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_738 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000738")
    batches[b_id_738] = {
        "id": b_id_738,
        "product_id": p_id_738,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 10),
        "purchase_cost": Decimal("306.92"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELMA CT 40/12.5
    p_id_739 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000738")
    products[p_id_739] = {
        "id": p_id_739,
        "code": "MED-TABTELMA",
        "name": 'TAB TELMA CT 40/12.5',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("543.12"),
        "default_purchase_price": Decimal("434.50"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_739 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000739")
    batches[b_id_739] = {
        "id": b_id_739,
        "product_id": p_id_739,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 11),
        "purchase_cost": Decimal("434.50"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB ACCEPT T
    p_id_740 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000739")
    products[p_id_740] = {
        "id": p_id_740,
        "code": "MED-TABACCEP",
        "name": 'TAB ACCEPT T',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("156.79"),
        "default_purchase_price": Decimal("125.43"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_740 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000740")
    batches[b_id_740] = {
        "id": b_id_740,
        "product_id": p_id_740,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 12),
        "purchase_cost": Decimal("125.43"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB NAPROSAFE 500
    p_id_741 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000740")
    products[p_id_741] = {
        "id": p_id_741,
        "code": "MED-TABNAPRO",
        "name": 'TAB NAPROSAFE 500',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("236.11"),
        "default_purchase_price": Decimal("188.89"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_741 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000741")
    batches[b_id_741] = {
        "id": b_id_741,
        "product_id": p_id_741,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 13),
        "purchase_cost": Decimal("188.89"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB LIJENTA 5MG
    p_id_742 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000741")
    products[p_id_742] = {
        "id": p_id_742,
        "code": "MED-TABLIJEN",
        "name": 'TAB LIJENTA 5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("314.81"),
        "default_purchase_price": Decimal("251.85"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_742 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000742")
    batches[b_id_742] = {
        "id": b_id_742,
        "product_id": p_id_742,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 14),
        "purchase_cost": Decimal("251.85"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB ILA -10
    p_id_743 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000742")
    products[p_id_743] = {
        "id": p_id_743,
        "code": "MED-TABILA10",
        "name": 'TAB ILA -10',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("168.96"),
        "default_purchase_price": Decimal("135.17"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_743 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000743")
    batches[b_id_743] = {
        "id": b_id_743,
        "product_id": p_id_743,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 15),
        "purchase_cost": Decimal("135.17"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB FENOREX 145 MG
    p_id_744 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000743")
    products[p_id_744] = {
        "id": p_id_744,
        "code": "MED-TABFENOR",
        "name": 'TAB FENOREX 145 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("122.85"),
        "default_purchase_price": Decimal("98.28"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_744 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000744")
    batches[b_id_744] = {
        "id": b_id_744,
        "product_id": p_id_744,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 16),
        "purchase_cost": Decimal("98.28"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB HEPACT 300MG
    p_id_745 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000744")
    products[p_id_745] = {
        "id": p_id_745,
        "code": "MED-TABHEPAC",
        "name": 'TAB HEPACT 300MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("414.68"),
        "default_purchase_price": Decimal("331.74"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_745 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000745")
    batches[b_id_745] = {
        "id": b_id_745,
        "product_id": p_id_745,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 17),
        "purchase_cost": Decimal("331.74"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB AMLOTAN 27.5
    p_id_746 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000745")
    products[p_id_746] = {
        "id": p_id_746,
        "code": "MED-TABAMLOT",
        "name": 'TAB AMLOTAN 27.5',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("68.41"),
        "default_purchase_price": Decimal("54.73"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_746 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000746")
    batches[b_id_746] = {
        "id": b_id_746,
        "product_id": p_id_746,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 18),
        "purchase_cost": Decimal("54.73"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # OROFRESH KIDS 50GM
    p_id_747 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000746")
    products[p_id_747] = {
        "id": p_id_747,
        "code": "MED-OROFRESH",
        "name": 'OROFRESH KIDS 50GM',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("337.59"),
        "default_purchase_price": Decimal("270.07"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_747 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000747")
    batches[b_id_747] = {
        "id": b_id_747,
        "product_id": p_id_747,
        "batch_number": "BCH-MEDORO-28",
        "expiry_date": date(2028, 4, 19),
        "purchase_cost": Decimal("270.07"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # OROFRESH MOUTH WASH 100M
    p_id_748 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000747")
    products[p_id_748] = {
        "id": p_id_748,
        "code": "MED-OROFRESH-1",
        "name": 'OROFRESH MOUTH WASH 100M',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("266.04"),
        "default_purchase_price": Decimal("212.83"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_748 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000748")
    batches[b_id_748] = {
        "id": b_id_748,
        "product_id": p_id_748,
        "batch_number": "BCH-MEDORO-27",
        "expiry_date": date(2027, 5, 20),
        "purchase_cost": Decimal("212.83"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB SPMIDE
    p_id_749 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000748")
    products[p_id_749] = {
        "id": p_id_749,
        "code": "MED-TABSPMID",
        "name": 'TAB SPMIDE',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("91.25"),
        "default_purchase_price": Decimal("73.00"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_749 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000749")
    batches[b_id_749] = {
        "id": b_id_749,
        "product_id": p_id_749,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 21),
        "purchase_cost": Decimal("73.00"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB LOSIUM 25MG
    p_id_750 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000749")
    products[p_id_750] = {
        "id": p_id_750,
        "code": "MED-TABLOSIU",
        "name": 'TAB LOSIUM 25MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("132.41"),
        "default_purchase_price": Decimal("105.93"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_750 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000750")
    batches[b_id_750] = {
        "id": b_id_750,
        "product_id": p_id_750,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 22),
        "purchase_cost": Decimal("105.93"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB ACENIL 100MG
    p_id_751 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000750")
    products[p_id_751] = {
        "id": p_id_751,
        "code": "MED-TABACENI",
        "name": 'TAB ACENIL 100MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("52.02"),
        "default_purchase_price": Decimal("41.62"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_751 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000751")
    batches[b_id_751] = {
        "id": b_id_751,
        "product_id": p_id_751,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 23),
        "purchase_cost": Decimal("41.62"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB TISART 40MG
    p_id_752 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000751")
    products[p_id_752] = {
        "id": p_id_752,
        "code": "MED-TABTISAR",
        "name": 'TAB TISART 40MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("199.62"),
        "default_purchase_price": Decimal("159.70"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_752 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000752")
    batches[b_id_752] = {
        "id": b_id_752,
        "product_id": p_id_752,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 24),
        "purchase_cost": Decimal("159.70"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB VGLOR 90MG
    p_id_753 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000752")
    products[p_id_753] = {
        "id": p_id_753,
        "code": "MED-TABVGLOR",
        "name": 'TAB VGLOR 90MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("460.68"),
        "default_purchase_price": Decimal("368.54"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_753 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000753")
    batches[b_id_753] = {
        "id": b_id_753,
        "product_id": p_id_753,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 25),
        "purchase_cost": Decimal("368.54"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB AMFAST -T
    p_id_754 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000753")
    products[p_id_754] = {
        "id": p_id_754,
        "code": "MED-TABAMFAS-1",
        "name": 'TAB AMFAST -T',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("166.64"),
        "default_purchase_price": Decimal("133.31"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_754 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000754")
    batches[b_id_754] = {
        "id": b_id_754,
        "product_id": p_id_754,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 26),
        "purchase_cost": Decimal("133.31"),
        "quantity": 25,
        "is_active": True,
        "created_at": now,
    }

    # TAB AVAS 20MG
    p_id_755 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000754")
    products[p_id_755] = {
        "id": p_id_755,
        "code": "MED-TABAVAS2",
        "name": 'TAB AVAS 20MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("644.79"),
        "default_purchase_price": Decimal("515.83"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_755 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000755")
    batches[b_id_755] = {
        "id": b_id_755,
        "product_id": p_id_755,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 27),
        "purchase_cost": Decimal("515.83"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB DAPAMIN M
    p_id_756 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000755")
    products[p_id_756] = {
        "id": p_id_756,
        "code": "MED-TABDAPAM",
        "name": 'TAB DAPAMIN M',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("415.42"),
        "default_purchase_price": Decimal("332.34"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_756 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000756")
    batches[b_id_756] = {
        "id": b_id_756,
        "product_id": p_id_756,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 1),
        "purchase_cost": Decimal("332.34"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB DAPAMIN M FORT
    p_id_757 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000756")
    products[p_id_757] = {
        "id": p_id_757,
        "code": "MED-TABDAPAM-1",
        "name": 'TAB DAPAMIN M FORT',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("307.73"),
        "default_purchase_price": Decimal("246.18"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_757 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000757")
    batches[b_id_757] = {
        "id": b_id_757,
        "product_id": p_id_757,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 2),
        "purchase_cost": Decimal("246.18"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELVAS AM 40/5MG
    p_id_758 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000757")
    products[p_id_758] = {
        "id": p_id_758,
        "code": "MED-TABTELVA",
        "name": 'TAB TELVAS AM 40/5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("225.01"),
        "default_purchase_price": Decimal("180.01"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_758 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000758")
    batches[b_id_758] = {
        "id": b_id_758,
        "product_id": p_id_758,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 3),
        "purchase_cost": Decimal("180.01"),
        "quantity": 40,
        "is_active": True,
        "created_at": now,
    }

    # TAB ESTAGLIP-50
    p_id_759 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000758")
    products[p_id_759] = {
        "id": p_id_759,
        "code": "MED-TABESTAG",
        "name": 'TAB ESTAGLIP-50',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("256.42"),
        "default_purchase_price": Decimal("205.14"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_759 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000759")
    batches[b_id_759] = {
        "id": b_id_759,
        "product_id": p_id_759,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 4),
        "purchase_cost": Decimal("205.14"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB FORMIN 850MG
    p_id_760 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000759")
    products[p_id_760] = {
        "id": p_id_760,
        "code": "MED-TABFORMI-2",
        "name": 'TAB FORMIN 850MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("35.84"),
        "default_purchase_price": Decimal("28.67"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_760 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000760")
    batches[b_id_760] = {
        "id": b_id_760,
        "product_id": p_id_760,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 5),
        "purchase_cost": Decimal("28.67"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # TAB ROZAT 10MG
    p_id_761 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000760")
    products[p_id_761] = {
        "id": p_id_761,
        "code": "MED-TABROZAT",
        "name": 'TAB ROZAT 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("436.76"),
        "default_purchase_price": Decimal("349.41"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_761 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000761")
    batches[b_id_761] = {
        "id": b_id_761,
        "product_id": p_id_761,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 6),
        "purchase_cost": Decimal("349.41"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB AMLOD AT H
    p_id_762 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000761")
    products[p_id_762] = {
        "id": p_id_762,
        "code": "MED-TABAMLOD",
        "name": 'TAB AMLOD AT H',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("51.61"),
        "default_purchase_price": Decimal("41.29"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_762 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000762")
    batches[b_id_762] = {
        "id": b_id_762,
        "product_id": p_id_762,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 7),
        "purchase_cost": Decimal("41.29"),
        "quantity": 40,
        "is_active": True,
        "created_at": now,
    }

    # TAB FLUCAZ 150 MG
    p_id_763 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000762")
    products[p_id_763] = {
        "id": p_id_763,
        "code": "MED-TABFLUCA",
        "name": 'TAB FLUCAZ 150 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("19.11"),
        "default_purchase_price": Decimal("15.29"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_763 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000763")
    batches[b_id_763] = {
        "id": b_id_763,
        "product_id": p_id_763,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 8),
        "purchase_cost": Decimal("15.29"),
        "quantity": 39,
        "is_active": True,
        "created_at": now,
    }

    # TAB VEGAPRAZ 10MG
    p_id_764 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000763")
    products[p_id_764] = {
        "id": p_id_764,
        "code": "MED-TABVEGAP",
        "name": 'TAB VEGAPRAZ 10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("247.71"),
        "default_purchase_price": Decimal("198.17"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_764 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000764")
    batches[b_id_764] = {
        "id": b_id_764,
        "product_id": p_id_764,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 9),
        "purchase_cost": Decimal("198.17"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELSARTAN AM 80MG
    p_id_765 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000764")
    products[p_id_765] = {
        "id": p_id_765,
        "code": "MED-TABTELSA-4",
        "name": 'TAB TELSARTAN AM 80MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("227.07"),
        "default_purchase_price": Decimal("181.66"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_765 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000765")
    batches[b_id_765] = {
        "id": b_id_765,
        "product_id": p_id_765,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 10),
        "purchase_cost": Decimal("181.66"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB SITAPRIDE 100
    p_id_766 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000765")
    products[p_id_766] = {
        "id": p_id_766,
        "code": "MED-TABSITAP-1",
        "name": 'TAB SITAPRIDE 100',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("299.86"),
        "default_purchase_price": Decimal("239.89"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_766 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000766")
    batches[b_id_766] = {
        "id": b_id_766,
        "product_id": p_id_766,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 11),
        "purchase_cost": Decimal("239.89"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB SITAPRID 50MG
    p_id_767 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000766")
    products[p_id_767] = {
        "id": p_id_767,
        "code": "MED-TABSITAP-2",
        "name": 'TAB SITAPRID 50MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("247.18"),
        "default_purchase_price": Decimal("197.74"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_767 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000767")
    batches[b_id_767] = {
        "id": b_id_767,
        "product_id": p_id_767,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 12),
        "purchase_cost": Decimal("197.74"),
        "quantity": 4,
        "is_active": True,
        "created_at": now,
    }

    # TAB XYPHEN
    p_id_768 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000767")
    products[p_id_768] = {
        "id": p_id_768,
        "code": "MED-TABXYPHE",
        "name": 'TAB XYPHEN',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("82.61"),
        "default_purchase_price": Decimal("66.09"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_768 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000768")
    batches[b_id_768] = {
        "id": b_id_768,
        "product_id": p_id_768,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 13),
        "purchase_cost": Decimal("66.09"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB METFOR G1 850
    p_id_769 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000768")
    products[p_id_769] = {
        "id": p_id_769,
        "code": "MED-TABMETFO",
        "name": 'TAB METFOR G1 850',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("102.85"),
        "default_purchase_price": Decimal("82.28"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_769 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000769")
    batches[b_id_769] = {
        "id": b_id_769,
        "product_id": p_id_769,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 14),
        "purchase_cost": Decimal("82.28"),
        "quantity": 25,
        "is_active": True,
        "created_at": now,
    }

    # TAB METFLICS M 1000 SR
    p_id_770 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000769")
    products[p_id_770] = {
        "id": p_id_770,
        "code": "MED-TABMETFL-3",
        "name": 'TAB METFLICS M 1000 SR',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("200.74"),
        "default_purchase_price": Decimal("160.59"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_770 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000770")
    batches[b_id_770] = {
        "id": b_id_770,
        "product_id": p_id_770,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 15),
        "purchase_cost": Decimal("160.59"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAM METFLICS 1000MG
    p_id_771 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000770")
    products[p_id_771] = {
        "id": p_id_771,
        "code": "MED-TAMMETFL",
        "name": 'TAM METFLICS 1000MG',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("64.34"),
        "default_purchase_price": Decimal("51.47"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_771 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000771")
    batches[b_id_771] = {
        "id": b_id_771,
        "product_id": p_id_771,
        "batch_number": "BCH-MEDTAM-28",
        "expiry_date": date(2028, 4, 16),
        "purchase_cost": Decimal("51.47"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB DOLOWIN
    p_id_772 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000771")
    products[p_id_772] = {
        "id": p_id_772,
        "code": "MED-TABDOLOW-1",
        "name": 'TAB DOLOWIN',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("88.22"),
        "default_purchase_price": Decimal("70.58"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_772 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000772")
    batches[b_id_772] = {
        "id": b_id_772,
        "product_id": p_id_772,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 17),
        "purchase_cost": Decimal("70.58"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB ARNI 100MG
    p_id_773 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000772")
    products[p_id_773] = {
        "id": p_id_773,
        "code": "MED-TABARNI1",
        "name": 'TAB ARNI 100MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("777.11"),
        "default_purchase_price": Decimal("621.69"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_773 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000773")
    batches[b_id_773] = {
        "id": b_id_773,
        "product_id": p_id_773,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 18),
        "purchase_cost": Decimal("621.69"),
        "quantity": 4,
        "is_active": True,
        "created_at": now,
    }

    # TAB LIPTA M 1000MG
    p_id_774 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000773")
    products[p_id_774] = {
        "id": p_id_774,
        "code": "MED-TABLIPTA-4",
        "name": 'TAB LIPTA M 1000MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("173.69"),
        "default_purchase_price": Decimal("138.95"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_774 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000774")
    batches[b_id_774] = {
        "id": b_id_774,
        "product_id": p_id_774,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 19),
        "purchase_cost": Decimal("138.95"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # TAB DAPAMETS 10/1000MG
    p_id_775 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000774")
    products[p_id_775] = {
        "id": p_id_775,
        "code": "MED-TABDAPAM-2",
        "name": 'TAB DAPAMETS 10/1000MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("447.15"),
        "default_purchase_price": Decimal("357.72"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_775 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000775")
    batches[b_id_775] = {
        "id": b_id_775,
        "product_id": p_id_775,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 20),
        "purchase_cost": Decimal("357.72"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELMI 80 H
    p_id_776 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000775")
    products[p_id_776] = {
        "id": p_id_776,
        "code": "MED-TABTELMI-1",
        "name": 'TAB TELMI 80 H',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("256.99"),
        "default_purchase_price": Decimal("205.59"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_776 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000776")
    batches[b_id_776] = {
        "id": b_id_776,
        "product_id": p_id_776,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 21),
        "purchase_cost": Decimal("205.59"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB AMPRO TH (5+40MG )
    p_id_777 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000776")
    products[p_id_777] = {
        "id": p_id_777,
        "code": "MED-TABAMPRO-1",
        "name": 'TAB AMPRO TH (5+40MG )',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("124.54"),
        "default_purchase_price": Decimal("99.63"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_777 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000777")
    batches[b_id_777] = {
        "id": b_id_777,
        "product_id": p_id_777,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 22),
        "purchase_cost": Decimal("99.63"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB ADEP 40MG
    p_id_778 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000777")
    products[p_id_778] = {
        "id": p_id_778,
        "code": "MED-TABADEP4",
        "name": 'TAB ADEP 40MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("143.21"),
        "default_purchase_price": Decimal("114.57"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_778 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000778")
    batches[b_id_778] = {
        "id": b_id_778,
        "product_id": p_id_778,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 23),
        "purchase_cost": Decimal("114.57"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # SYRP RITE -O-CEF 60ML
    p_id_779 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000778")
    products[p_id_779] = {
        "id": p_id_779,
        "code": "MED-SYRPRITE",
        "name": 'SYRP RITE -O-CEF 60ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("118.30"),
        "default_purchase_price": Decimal("94.64"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_779 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000779")
    batches[b_id_779] = {
        "id": b_id_779,
        "product_id": p_id_779,
        "batch_number": "BCH-MEDSYR-28",
        "expiry_date": date(2028, 12, 24),
        "purchase_cost": Decimal("94.64"),
        "quantity": 24,
        "is_active": True,
        "created_at": now,
    }

    # TAB GLYCOMET GP 2 FORT
    p_id_780 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000779")
    products[p_id_780] = {
        "id": p_id_780,
        "code": "MED-TABGLYCO-1",
        "name": 'TAB GLYCOMET GP 2 FORT',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("192.79"),
        "default_purchase_price": Decimal("154.23"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_780 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000780")
    batches[b_id_780] = {
        "id": b_id_780,
        "product_id": p_id_780,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 25),
        "purchase_cost": Decimal("154.23"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # SYRP NOWORM 10ML
    p_id_781 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000780")
    products[p_id_781] = {
        "id": p_id_781,
        "code": "MED-SYRPNOWO",
        "name": 'SYRP NOWORM 10ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("16.80"),
        "default_purchase_price": Decimal("13.44"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_781 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000781")
    batches[b_id_781] = {
        "id": b_id_781,
        "product_id": p_id_781,
        "batch_number": "BCH-MEDSYR-28",
        "expiry_date": date(2028, 2, 26),
        "purchase_cost": Decimal("13.44"),
        "quantity": 20,
        "is_active": True,
        "created_at": now,
    }

    # TAB SWICH 200MG
    p_id_782 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000781")
    products[p_id_782] = {
        "id": p_id_782,
        "code": "MED-TABSWICH",
        "name": 'TAB SWICH 200MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("204.21"),
        "default_purchase_price": Decimal("163.37"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_782 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000782")
    batches[b_id_782] = {
        "id": b_id_782,
        "product_id": p_id_782,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 27),
        "purchase_cost": Decimal("163.37"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB DOXCEF -200MG
    p_id_783 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000782")
    products[p_id_783] = {
        "id": p_id_783,
        "code": "MED-TABDOXCE",
        "name": 'TAB DOXCEF -200MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("230.66"),
        "default_purchase_price": Decimal("184.53"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_783 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000783")
    batches[b_id_783] = {
        "id": b_id_783,
        "product_id": p_id_783,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 1),
        "purchase_cost": Decimal("184.53"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB SMARTAN AM
    p_id_784 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000783")
    products[p_id_784] = {
        "id": p_id_784,
        "code": "MED-TABSMART",
        "name": 'TAB SMARTAN AM',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("218.75"),
        "default_purchase_price": Decimal("175.00"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_784 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000784")
    batches[b_id_784] = {
        "id": b_id_784,
        "product_id": p_id_784,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 2),
        "purchase_cost": Decimal("175.00"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB ROSLET 10
    p_id_785 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000784")
    products[p_id_785] = {
        "id": p_id_785,
        "code": "MED-TABROSLE",
        "name": 'TAB ROSLET 10',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("312.55"),
        "default_purchase_price": Decimal("250.04"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_785 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000785")
    batches[b_id_785] = {
        "id": b_id_785,
        "product_id": p_id_785,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 3),
        "purchase_cost": Decimal("250.04"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # SYRP CLAVAM BID DIS 30ML
    p_id_786 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000785")
    products[p_id_786] = {
        "id": p_id_786,
        "code": "MED-SYRPCLAV",
        "name": 'SYRP CLAVAM BID DIS 30ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("74.50"),
        "default_purchase_price": Decimal("59.60"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_786 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000786")
    batches[b_id_786] = {
        "id": b_id_786,
        "product_id": p_id_786,
        "batch_number": "BCH-MEDSYR-27",
        "expiry_date": date(2027, 7, 4),
        "purchase_cost": Decimal("59.60"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # CLAVAM DRY SYP 30ML
    p_id_787 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000786")
    products[p_id_787] = {
        "id": p_id_787,
        "code": "MED-CLAVAMDR-1",
        "name": 'CLAVAM DRY SYP 30ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("90.54"),
        "default_purchase_price": Decimal("72.43"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_787 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000787")
    batches[b_id_787] = {
        "id": b_id_787,
        "product_id": p_id_787,
        "batch_number": "BCH-MEDCLA-28",
        "expiry_date": date(2028, 8, 5),
        "purchase_cost": Decimal("72.43"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB MONORAL 200MG
    p_id_788 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000787")
    products[p_id_788] = {
        "id": p_id_788,
        "code": "MED-TABMONOR",
        "name": 'TAB MONORAL 200MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("208.47"),
        "default_purchase_price": Decimal("166.78"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_788 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000788")
    batches[b_id_788] = {
        "id": b_id_788,
        "product_id": p_id_788,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 6),
        "purchase_cost": Decimal("166.78"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB GRANDAM MD
    p_id_789 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000788")
    products[p_id_789] = {
        "id": p_id_789,
        "code": "MED-TABGRAND",
        "name": 'TAB GRANDAM MD',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("179.70"),
        "default_purchase_price": Decimal("143.76"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_789 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000789")
    batches[b_id_789] = {
        "id": b_id_789,
        "product_id": p_id_789,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 7),
        "purchase_cost": Decimal("143.76"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB GRANDAM -1MG -
    p_id_790 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000789")
    products[p_id_790] = {
        "id": p_id_790,
        "code": "MED-TABGRAND-1",
        "name": 'TAB GRANDAM -1MG -',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("164.31"),
        "default_purchase_price": Decimal("131.45"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_790 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000790")
    batches[b_id_790] = {
        "id": b_id_790,
        "product_id": p_id_790,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 8),
        "purchase_cost": Decimal("131.45"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB AMLOSAFE 2.5MG
    p_id_791 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000790")
    products[p_id_791] = {
        "id": p_id_791,
        "code": "MED-TABAMLOS",
        "name": 'TAB AMLOSAFE 2.5MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("24.14"),
        "default_purchase_price": Decimal("19.31"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_791 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000791")
    batches[b_id_791] = {
        "id": b_id_791,
        "product_id": p_id_791,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 9),
        "purchase_cost": Decimal("19.31"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB ARISTOGLY 400MG
    p_id_792 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000791")
    products[p_id_792] = {
        "id": p_id_792,
        "code": "MED-TABARIST",
        "name": 'TAB ARISTOGLY 400MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("27.15"),
        "default_purchase_price": Decimal("21.72"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_792 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000792")
    batches[b_id_792] = {
        "id": b_id_792,
        "product_id": p_id_792,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 10),
        "purchase_cost": Decimal("21.72"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB ALSARTAN  50MG
    p_id_793 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000792")
    products[p_id_793] = {
        "id": p_id_793,
        "code": "MED-TABALSAR",
        "name": 'TAB ALSARTAN  50MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("74.24"),
        "default_purchase_price": Decimal("59.39"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_793 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000793")
    batches[b_id_793] = {
        "id": b_id_793,
        "product_id": p_id_793,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 11),
        "purchase_cost": Decimal("59.39"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB ALSARTAN -H-62.5 MG
    p_id_794 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000793")
    products[p_id_794] = {
        "id": p_id_794,
        "code": "MED-TABALSAR-1",
        "name": 'TAB ALSARTAN -H-62.5 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("168.78"),
        "default_purchase_price": Decimal("135.02"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_794 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000794")
    batches[b_id_794] = {
        "id": b_id_794,
        "product_id": p_id_794,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 12),
        "purchase_cost": Decimal("135.02"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # LULICAN 30ML LOTION
    p_id_795 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000794")
    products[p_id_795] = {
        "id": p_id_795,
        "code": "MED-LULICAN3",
        "name": 'LULICAN 30ML LOTION',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("417.38"),
        "default_purchase_price": Decimal("333.90"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_795 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000795")
    batches[b_id_795] = {
        "id": b_id_795,
        "product_id": p_id_795,
        "batch_number": "BCH-MEDLUL-28",
        "expiry_date": date(2028, 4, 13),
        "purchase_cost": Decimal("333.90"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB CANDIBIOTIC -EAR DROP 5 ML
    p_id_796 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000795")
    products[p_id_796] = {
        "id": p_id_796,
        "code": "MED-TABCANDI",
        "name": 'TAB CANDIBIOTIC -EAR DROP 5 ML',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("108.26"),
        "default_purchase_price": Decimal("86.61"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_796 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000796")
    batches[b_id_796] = {
        "id": b_id_796,
        "product_id": p_id_796,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 14),
        "purchase_cost": Decimal("86.61"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # CANDID -EAR DROPS 10ML
    p_id_797 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000796")
    products[p_id_797] = {
        "id": p_id_797,
        "code": "MED-CANDIDEA",
        "name": 'CANDID -EAR DROPS 10ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("187.70"),
        "default_purchase_price": Decimal("150.16"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_797 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000797")
    batches[b_id_797] = {
        "id": b_id_797,
        "product_id": p_id_797,
        "batch_number": "BCH-MEDCAN-28",
        "expiry_date": date(2028, 6, 15),
        "purchase_cost": Decimal("150.16"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # CANDID -LOTION 30ML
    p_id_798 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000797")
    products[p_id_798] = {
        "id": p_id_798,
        "code": "MED-CANDIDLO",
        "name": 'CANDID -LOTION 30ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("219.06"),
        "default_purchase_price": Decimal("175.25"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_798 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000798")
    batches[b_id_798] = {
        "id": b_id_798,
        "product_id": p_id_798,
        "batch_number": "BCH-MEDCAN-27",
        "expiry_date": date(2027, 7, 16),
        "purchase_cost": Decimal("175.25"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # CANDID -TV SUSP 75ML
    p_id_799 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000798")
    products[p_id_799] = {
        "id": p_id_799,
        "code": "MED-CANDIDTV",
        "name": 'CANDID -TV SUSP 75ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("526.14"),
        "default_purchase_price": Decimal("420.91"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_799 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000799")
    batches[b_id_799] = {
        "id": b_id_799,
        "product_id": p_id_799,
        "batch_number": "BCH-MEDCAN-28",
        "expiry_date": date(2028, 8, 17),
        "purchase_cost": Decimal("420.91"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # CAP  AIRTEC -FB 400
    p_id_800 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000799")
    products[p_id_800] = {
        "id": p_id_800,
        "code": "MED-CAPAIRTE",
        "name": 'CAP  AIRTEC -FB 400',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("391.40"),
        "default_purchase_price": Decimal("313.12"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_800 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000800")
    batches[b_id_800] = {
        "id": b_id_800,
        "product_id": p_id_800,
        "batch_number": "BCH-MEDCAP-27",
        "expiry_date": date(2027, 9, 18),
        "purchase_cost": Decimal("313.12"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # CAP AIRTEC -FB 200
    p_id_801 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000800")
    products[p_id_801] = {
        "id": p_id_801,
        "code": "MED-CAPAIRTE-1",
        "name": 'CAP AIRTEC -FB 200',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("322.11"),
        "default_purchase_price": Decimal("257.69"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_801 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000801")
    batches[b_id_801] = {
        "id": b_id_801,
        "product_id": p_id_801,
        "batch_number": "BCH-MEDCAP-28",
        "expiry_date": date(2028, 10, 19),
        "purchase_cost": Decimal("257.69"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB MICROCEF 100DT
    p_id_802 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000801")
    products[p_id_802] = {
        "id": p_id_802,
        "code": "MED-TABMICRO",
        "name": 'TAB MICROCEF 100DT',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("218.85"),
        "default_purchase_price": Decimal("175.08"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_802 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000802")
    batches[b_id_802] = {
        "id": b_id_802,
        "product_id": p_id_802,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 20),
        "purchase_cost": Decimal("175.08"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # SYRP MICROCEF 100 MG   30ML
    p_id_803 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000802")
    products[p_id_803] = {
        "id": p_id_803,
        "code": "MED-SYRPMICR",
        "name": 'SYRP MICROCEF 100 MG   30ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("251.11"),
        "default_purchase_price": Decimal("200.89"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_803 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000803")
    batches[b_id_803] = {
        "id": b_id_803,
        "product_id": p_id_803,
        "batch_number": "BCH-MEDSYR-28",
        "expiry_date": date(2028, 12, 21),
        "purchase_cost": Decimal("200.89"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # SYRP MICROCEF 50 MG 30ML
    p_id_804 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000803")
    products[p_id_804] = {
        "id": p_id_804,
        "code": "MED-SYRPMICR-1",
        "name": 'SYRP MICROCEF 50 MG 30ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("164.14"),
        "default_purchase_price": Decimal("131.31"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_804 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000804")
    batches[b_id_804] = {
        "id": b_id_804,
        "product_id": p_id_804,
        "batch_number": "BCH-MEDSYR-27",
        "expiry_date": date(2027, 1, 22),
        "purchase_cost": Decimal("131.31"),
        "quantity": 12,
        "is_active": True,
        "created_at": now,
    }

    # TAB BACTOCLAV 375 MG
    p_id_805 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000804")
    products[p_id_805] = {
        "id": p_id_805,
        "code": "MED-TABBACTO",
        "name": 'TAB BACTOCLAV 375 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("321.86"),
        "default_purchase_price": Decimal("257.49"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_805 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000805")
    batches[b_id_805] = {
        "id": b_id_805,
        "product_id": p_id_805,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 23),
        "purchase_cost": Decimal("257.49"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB BACTOCLAV 625 MG
    p_id_806 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000805")
    products[p_id_806] = {
        "id": p_id_806,
        "code": "MED-TABBACTO-1",
        "name": 'TAB BACTOCLAV 625 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("280.86"),
        "default_purchase_price": Decimal("224.69"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_806 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000806")
    batches[b_id_806] = {
        "id": b_id_806,
        "product_id": p_id_806,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 3, 24),
        "purchase_cost": Decimal("224.69"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # SYRP BACTOCLAV 30ML
    p_id_807 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000806")
    products[p_id_807] = {
        "id": p_id_807,
        "code": "MED-SYRPBACT",
        "name": 'SYRP BACTOCLAV 30ML',
        "category": "Medicine",
        "unit": "Bottle",
        "mrp": Decimal("94.75"),
        "default_purchase_price": Decimal("75.80"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_807 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000807")
    batches[b_id_807] = {
        "id": b_id_807,
        "product_id": p_id_807,
        "batch_number": "BCH-MEDSYR-28",
        "expiry_date": date(2028, 4, 25),
        "purchase_cost": Decimal("75.80"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB MONTRAL
    p_id_808 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000807")
    products[p_id_808] = {
        "id": p_id_808,
        "code": "MED-TABMONTR",
        "name": 'TAB MONTRAL',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("191.81"),
        "default_purchase_price": Decimal("153.45"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_808 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000808")
    batches[b_id_808] = {
        "id": b_id_808,
        "product_id": p_id_808,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 5, 26),
        "purchase_cost": Decimal("153.45"),
        "quantity": 11,
        "is_active": True,
        "created_at": now,
    }

    # TAB ALLERCET -L
    p_id_809 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000808")
    products[p_id_809] = {
        "id": p_id_809,
        "code": "MED-TABALLER",
        "name": 'TAB ALLERCET -L',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("82.78"),
        "default_purchase_price": Decimal("66.22"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_809 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000809")
    batches[b_id_809] = {
        "id": b_id_809,
        "product_id": p_id_809,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 27),
        "purchase_cost": Decimal("66.22"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # DROP ARISTOZYME 15ML
    p_id_810 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000809")
    products[p_id_810] = {
        "id": p_id_810,
        "code": "MED-DROPARIS",
        "name": 'DROP ARISTOZYME 15ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("114.28"),
        "default_purchase_price": Decimal("91.42"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_810 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000810")
    batches[b_id_810] = {
        "id": b_id_810,
        "product_id": p_id_810,
        "batch_number": "BCH-MEDDRO-27",
        "expiry_date": date(2027, 7, 1),
        "purchase_cost": Decimal("91.42"),
        "quantity": 10,
        "is_active": True,
        "created_at": now,
    }

    # TAB NOVASTAT -10MG
    p_id_811 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000810")
    products[p_id_811] = {
        "id": p_id_811,
        "code": "MED-TABNOVAS",
        "name": 'TAB NOVASTAT -10MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("624.40"),
        "default_purchase_price": Decimal("499.52"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_811 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000811")
    batches[b_id_811] = {
        "id": b_id_811,
        "product_id": p_id_811,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 2),
        "purchase_cost": Decimal("499.52"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB NOVASTAT -20 MG
    p_id_812 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000811")
    products[p_id_812] = {
        "id": p_id_812,
        "code": "MED-TABNOVAS-1",
        "name": 'TAB NOVASTAT -20 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("1265.40"),
        "default_purchase_price": Decimal("1012.32"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_812 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000812")
    batches[b_id_812] = {
        "id": b_id_812,
        "product_id": p_id_812,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 3),
        "purchase_cost": Decimal("1012.32"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELISTA -40MG
    p_id_813 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000812")
    products[p_id_813] = {
        "id": p_id_813,
        "code": "MED-TABTELIS",
        "name": 'TAB TELISTA -40MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("189.38"),
        "default_purchase_price": Decimal("151.50"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_813 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000813")
    batches[b_id_813] = {
        "id": b_id_813,
        "product_id": p_id_813,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 10, 4),
        "purchase_cost": Decimal("151.50"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELISTA -H
    p_id_814 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000813")
    products[p_id_814] = {
        "id": p_id_814,
        "code": "MED-TABTELIS-1",
        "name": 'TAB TELISTA -H',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("498.95"),
        "default_purchase_price": Decimal("399.16"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_814 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000814")
    batches[b_id_814] = {
        "id": b_id_814,
        "product_id": p_id_814,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 5),
        "purchase_cost": Decimal("399.16"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELISTA AM
    p_id_815 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000814")
    products[p_id_815] = {
        "id": p_id_815,
        "code": "MED-TABTELIS-2",
        "name": 'TAB TELISTA AM',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("512.59"),
        "default_purchase_price": Decimal("410.07"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_815 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000815")
    batches[b_id_815] = {
        "id": b_id_815,
        "product_id": p_id_815,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 6),
        "purchase_cost": Decimal("410.07"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB TELISTA 20MG
    p_id_816 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000815")
    products[p_id_816] = {
        "id": p_id_816,
        "code": "MED-TABTELIS-3",
        "name": 'TAB TELISTA 20MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("107.95"),
        "default_purchase_price": Decimal("86.36"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_816 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000816")
    batches[b_id_816] = {
        "id": b_id_816,
        "product_id": p_id_816,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 7),
        "purchase_cost": Decimal("86.36"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # LACTODEX -2 NO MILK
    p_id_817 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000816")
    products[p_id_817] = {
        "id": p_id_817,
        "code": "MED-LACTODEX",
        "name": 'LACTODEX -2 NO MILK',
        "category": "Baby",
        "unit": "Piece",
        "mrp": Decimal("958.00"),
        "default_purchase_price": Decimal("766.40"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_817 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000817")
    batches[b_id_817] = {
        "id": b_id_817,
        "product_id": p_id_817,
        "batch_number": "BCH-MEDLAC-28",
        "expiry_date": date(2028, 2, 8),
        "purchase_cost": Decimal("766.40"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # LACTODEX 3 NO MILK
    p_id_818 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000817")
    products[p_id_818] = {
        "id": p_id_818,
        "code": "MED-LACTODEX-1",
        "name": 'LACTODEX 3 NO MILK',
        "category": "Baby",
        "unit": "Piece",
        "mrp": Decimal("998.51"),
        "default_purchase_price": Decimal("798.81"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_818 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000818")
    batches[b_id_818] = {
        "id": b_id_818,
        "product_id": p_id_818,
        "batch_number": "BCH-MEDLAC-27",
        "expiry_date": date(2027, 3, 9),
        "purchase_cost": Decimal("798.81"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB ROSUMAC 10
    p_id_819 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000818")
    products[p_id_819] = {
        "id": p_id_819,
        "code": "MED-TABROSUM",
        "name": 'TAB ROSUMAC 10',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("485.69"),
        "default_purchase_price": Decimal("388.55"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_819 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000819")
    batches[b_id_819] = {
        "id": b_id_819,
        "product_id": p_id_819,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 4, 10),
        "purchase_cost": Decimal("388.55"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # LACTODEX 1 NO MILK
    p_id_820 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000819")
    products[p_id_820] = {
        "id": p_id_820,
        "code": "MED-LACTODEX-2",
        "name": 'LACTODEX 1 NO MILK',
        "category": "Baby",
        "unit": "Piece",
        "mrp": Decimal("936.71"),
        "default_purchase_price": Decimal("749.37"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_820 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000820")
    batches[b_id_820] = {
        "id": b_id_820,
        "product_id": p_id_820,
        "batch_number": "BCH-MEDLAC-27",
        "expiry_date": date(2027, 5, 11),
        "purchase_cost": Decimal("749.37"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB SGLIP 100 MG
    p_id_821 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000820")
    products[p_id_821] = {
        "id": p_id_821,
        "code": "MED-TABSGLIP-2",
        "name": 'TAB SGLIP 100 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("303.76"),
        "default_purchase_price": Decimal("243.01"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_821 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000821")
    batches[b_id_821] = {
        "id": b_id_821,
        "product_id": p_id_821,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 6, 12),
        "purchase_cost": Decimal("243.01"),
        "quantity": 5,
        "is_active": True,
        "created_at": now,
    }

    # TAB ASIDOL -P
    p_id_822 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000821")
    products[p_id_822] = {
        "id": p_id_822,
        "code": "MED-TABASIDO",
        "name": 'TAB ASIDOL -P',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("124.00"),
        "default_purchase_price": Decimal("99.20"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_822 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000822")
    batches[b_id_822] = {
        "id": b_id_822,
        "product_id": p_id_822,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 7, 13),
        "purchase_cost": Decimal("99.20"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB ANASEN -250DT
    p_id_823 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000822")
    products[p_id_823] = {
        "id": p_id_823,
        "code": "MED-TABANASE",
        "name": 'TAB ANASEN -250DT',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("38.16"),
        "default_purchase_price": Decimal("30.53"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_823 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000823")
    batches[b_id_823] = {
        "id": b_id_823,
        "product_id": p_id_823,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 8, 14),
        "purchase_cost": Decimal("30.53"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # TAB ANASEN -500DT
    p_id_824 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000823")
    products[p_id_824] = {
        "id": p_id_824,
        "code": "MED-TABANASE-1",
        "name": 'TAB ANASEN -500DT',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("66.78"),
        "default_purchase_price": Decimal("53.42"),
        "barcode": None,
        "reorder_level": 5,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_824 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000824")
    batches[b_id_824] = {
        "id": b_id_824,
        "product_id": p_id_824,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 9, 15),
        "purchase_cost": Decimal("53.42"),
        "quantity": 6,
        "is_active": True,
        "created_at": now,
    }

    # NEW HAIR 4U 5% 60ML
    p_id_825 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000824")
    products[p_id_825] = {
        "id": p_id_825,
        "code": "MED-NEWHAIR4",
        "name": 'NEW HAIR 4U 5% 60ML',
        "category": "Medicine",
        "unit": "Piece",
        "mrp": Decimal("1298.81"),
        "default_purchase_price": Decimal("1039.05"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_825 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000825")
    batches[b_id_825] = {
        "id": b_id_825,
        "product_id": p_id_825,
        "batch_number": "BCH-MEDNEW-28",
        "expiry_date": date(2028, 10, 16),
        "purchase_cost": Decimal("1039.05"),
        "quantity": 1,
        "is_active": True,
        "created_at": now,
    }

    # TAB ETOMAX 400MG
    p_id_826 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000825")
    products[p_id_826] = {
        "id": p_id_826,
        "code": "MED-TABETOMA",
        "name": 'TAB ETOMAX 400MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("156.12"),
        "default_purchase_price": Decimal("124.90"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_826 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000826")
    batches[b_id_826] = {
        "id": b_id_826,
        "product_id": p_id_826,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 11, 17),
        "purchase_cost": Decimal("124.90"),
        "quantity": 2,
        "is_active": True,
        "created_at": now,
    }

    # TAB CORTILONE 2.5 MG
    p_id_827 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000826")
    products[p_id_827] = {
        "id": p_id_827,
        "code": "MED-TABCORTI",
        "name": 'TAB CORTILONE 2.5 MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("15.61"),
        "default_purchase_price": Decimal("12.49"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_827 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000827")
    batches[b_id_827] = {
        "id": b_id_827,
        "product_id": p_id_827,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 12, 18),
        "purchase_cost": Decimal("12.49"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB DULETIN -20MG
    p_id_828 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000827")
    products[p_id_828] = {
        "id": p_id_828,
        "code": "MED-TABDULET",
        "name": 'TAB DULETIN -20MG',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("104.06"),
        "default_purchase_price": Decimal("83.25"),
        "barcode": None,
        "reorder_level": 2,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_828 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000828")
    batches[b_id_828] = {
        "id": b_id_828,
        "product_id": p_id_828,
        "batch_number": "BCH-MEDTAB-27",
        "expiry_date": date(2027, 1, 19),
        "purchase_cost": Decimal("83.25"),
        "quantity": 3,
        "is_active": True,
        "created_at": now,
    }

    # TAB D-PAIN
    p_id_829 = uuid.UUID("dddddddd-dddd-dddd-dddd-000000000828")
    products[p_id_829] = {
        "id": p_id_829,
        "code": "MED-TABDPAIN",
        "name": 'TAB D-PAIN',
        "category": "Medicine",
        "unit": "Strip",
        "mrp": Decimal("13.90"),
        "default_purchase_price": Decimal("11.12"),
        "barcode": None,
        "reorder_level": 10,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    b_id_829 = uuid.UUID("eeeeeeee-eeee-eeee-eeee-000000000829")
    batches[b_id_829] = {
        "id": b_id_829,
        "product_id": p_id_829,
        "batch_number": "BCH-MEDTAB-28",
        "expiry_date": date(2028, 2, 20),
        "purchase_cost": Decimal("11.12"),
        "quantity": 15,
        "is_active": True,
        "created_at": now,
    }

