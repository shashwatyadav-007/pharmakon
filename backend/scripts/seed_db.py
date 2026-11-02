"""
Database Seeding Script for PharmaKon.
Seeds the PostgreSQL database with the complete pharmacy catalog (732 products, 733 batches, 3 suppliers).
Idempotent: skips seeding if products already exist in the database.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from sqlalchemy import select
from app.core.database import SessionLocal, check_db_connection
from app.models.product import Product
from app.models.supplier import Supplier
from app.models.inventory import Batch
from app.services import data_store


def seed_database():
    is_connected, msg = check_db_connection()
    if not is_connected:
        print(f"Error: Unable to connect to database: {msg}")
        sys.exit(1)

    print("Connected to PostgreSQL successfully.")
    
    # Load sample operational data from data_store
    data_store.seed_sample_data()

    with SessionLocal() as db:
        # Check if products already exist
        existing_products_count = db.execute(select(Product.id)).scalars().all()
        if len(existing_products_count) > 0:
            print(f"Database already contains {len(existing_products_count)} products. Skipping seed.")
            return

        print(f"Seeding {len(data_store.suppliers)} suppliers...")
        for s_data in data_store.suppliers.values():
            supplier = Supplier(
                id=s_data["id"],
                name=s_data["name"],
                contact_person=s_data.get("contact_person"),
                phone=s_data["phone"],
                email=s_data.get("email"),
                address=s_data.get("address"),
                pan_vat_number=s_data.get("pan_vat_number"),
                is_active=s_data.get("is_active", True),
                created_at=s_data["created_at"],
                updated_at=s_data["updated_at"],
            )
            db.add(supplier)
        db.commit()
        print("Suppliers seeded successfully.")

        print(f"Seeding {len(data_store.products)} products...")
        for p_data in data_store.products.values():
            product = Product(
                id=p_data["id"],
                code=p_data["code"],
                name=p_data["name"],
                category=p_data["category"],
                unit=p_data["unit"],
                mrp=p_data["mrp"],
                default_purchase_price=p_data.get("default_purchase_price"),
                barcode=p_data.get("barcode"),
                reorder_level=p_data.get("reorder_level", 10),
                is_active=p_data.get("is_active", True),
                created_at=p_data["created_at"],
                updated_at=p_data["updated_at"],
            )
            db.add(product)
        db.commit()
        print("Products seeded successfully.")

        print(f"Seeding {len(data_store.batches)} batches...")
        for b_data in data_store.batches.values():
            batch = Batch(
                id=b_data["id"],
                product_id=b_data["product_id"],
                batch_number=b_data["batch_number"],
                expiry_date=b_data["expiry_date"],
                purchase_cost=b_data["purchase_cost"],
                quantity=b_data["quantity"],
                is_active=b_data.get("is_active", True),
                created_at=b_data["created_at"],
                updated_at=b_data.get("updated_at", b_data["created_at"]),
            )
            db.add(batch)
        db.commit()
        print("Batches seeded successfully.")

        print("\nDatabase seeding completed successfully!")
        print(f"- Suppliers: {len(data_store.suppliers)}")
        print(f"- Products:  {len(data_store.products)}")
        print(f"- Batches:   {len(data_store.batches)}")


if __name__ == "__main__":
    seed_database()
