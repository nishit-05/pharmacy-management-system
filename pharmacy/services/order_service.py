from ..extensions import db
from ..models.order import Order

def create_order(medicine, quantity, created_by):
    order = Order(
        medicine_id=medicine.id,
        medicine_name=medicine.name,
        quantity=quantity,
        created_by=created_by
    )

    db.session.add(order)

def get_all_orders():
    return Order.query.order_by(Order.created_at.desc()).all()
