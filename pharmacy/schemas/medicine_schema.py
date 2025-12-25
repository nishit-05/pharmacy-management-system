ALLOWED_UNIT_TYPES = {
    "tablet",
    "capsule",
    "sachet",
    "bottle",
    "vial",
    "ampoule",
    "syringe",
    "injection_kit",
    "tube",
    "spray",
    "strip",
    "pack",
    "unit"
}

def validate_medicine_payload(name, unit_type, stock_quantity, min_stock_level):
    if not name or not name.strip():
        return False, "Medicine name is required"

    unit_type = unit_type.lower().strip() if unit_type else ""

    if unit_type not in ALLOWED_UNIT_TYPES:
        return False, f"Invalid unit type. Allowed: {', '.join(sorted(ALLOWED_UNIT_TYPES))}"

    try:
        stock_quantity = int(stock_quantity)
        min_stock_level = int(min_stock_level)
    except (TypeError, ValueError):
        return False, "Stock values must be integers"

    if stock_quantity < 0:
        return False, "Stock quantity cannot be negative"

    if min_stock_level < 0:
        return False, "Minimum stock level cannot be negative"

    return True, {
        "name": name.strip(),
        "unit_type": unit_type,
        "stock_quantity": stock_quantity,
        "min_stock_level": min_stock_level
    }
