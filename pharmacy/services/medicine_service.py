from .order_service import create_order
from ..models.medicine import Medicine
from ..extensions import db
from ..schemas.medicine_schema import validate_medicine_payload

def get_all_medicines():
    return Medicine.query.all()

def add_medicine(data):
    is_valid, result = validate_medicine_payload(
        data.get("name"),
        data.get("unit_type"),
        data.get("stock_quantity"),
        data.get("min_stock_level")
    )

    if not is_valid:
        raise ValueError(result)

    existing = Medicine.query.filter_by(name=result["name"]).first()
    if existing:
        raise ValueError("Medicine already exists")

    medicine = Medicine(**result)
    db.session.add(medicine)
    db.session.commit()

def delete_medicine(medicine_id):
    medicine = Medicine.query.get(medicine_id)
    if not medicine:
        raise ValueError("Medicine not found")

    db.session.delete(medicine)
    db.session.commit()

def dispense_medicine(medicine_id, quantity):
    try:
        quantity = int(quantity)
    except (TypeError, ValueError):
        raise ValueError("Dispense quantity must be an integer")

    if quantity <= 0:
        raise ValueError("Dispense quantity must be greater than zero")

    medicine = Medicine.query.get(medicine_id)
    if not medicine:
        raise ValueError("Medicine not found")

    if medicine.stock_quantity < quantity:
        raise ValueError("Insufficient stock")

    # ✅ ALL validations passed — safe to proceed

    medicine.stock_quantity -= quantity

    create_order(
        medicine=medicine,
        quantity=quantity,
        created_by="pharmacist"
    )

    db.session.commit()

