from datetime import datetime
from ..extensions import db


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    # Reference to the medicine that was dispensed
    medicine_id = db.Column(
        db.Integer,
        db.ForeignKey("medicine.id"),
        nullable=False
    )

    # Snapshot of medicine name at time of sale
    medicine_name = db.Column(
        db.String(100),
        nullable=False
    )

    # Quantity dispensed / sold
    quantity = db.Column(
        db.Integer,
        nullable=False
    )

    # Who performed the action (admin / pharmacist / staff)
    created_by = db.Column(
        db.String(50),
        nullable=False
    )

    # Timestamp of the order
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return (
            f"<Order id={self.id} "
            f"medicine={self.medicine_name} "
            f"qty={self.quantity} "
            f"by={self.created_by}>"
        )
