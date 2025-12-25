from flask import Blueprint, render_template, request, redirect, abort



from ..services.medicine_service import (
    get_all_medicines,
    add_medicine,
    delete_medicine,
    dispense_medicine
)

medicine_bp = Blueprint("medicine", __name__)

# -------------------------
# VIEW INVENTORY
# -------------------------
@medicine_bp.route("/", methods=["GET"])
def home():
    medicines = get_all_medicines()
    return render_template("dashboard.html", medicines=medicines)



# -------------------------
# ADD MEDICINE (INVENTORY ENTRY)
# -------------------------
@medicine_bp.route("/", methods=["POST"])

def add():
    try:
        add_medicine(request.form)
    except ValueError as e:
        abort(400, description=str(e))
    return redirect("/")


# -------------------------
# DELETE MEDICINE (ADMIN ONLY)
# -------------------------
@medicine_bp.route("/delete/<int:medicine_id>", methods=["POST"])

def delete(medicine_id):
    try:
        delete_medicine(medicine_id)
    except ValueError as e:
        abort(400, description=str(e))
    return redirect("/")


# -------------------------
# DISPENSE MEDICINE (STOCK OUT)
# -------------------------
@medicine_bp.route("/dispense/<int:medicine_id>", methods=["POST"])

def dispense(medicine_id):
    quantity = request.form.get("quantity")
    try:
        dispense_medicine(medicine_id, quantity)
    except ValueError as e:
        abort(400, description=str(e))
    return redirect("/")
