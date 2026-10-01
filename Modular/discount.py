BULK_QTY = 5
BULK_RATE = 0.05
SENIOR_RATE = 0.20


def compute_totals(orders, is_senior):
    subtotal = 0.0
    total_qty = 0
    for item, qty, price in orders:
        subtotal += qty * price
        total_qty += qty

    if is_senior:
        discount, label = subtotal * SENIOR_RATE, "Senior/PWD Discount (20%)"
    elif total_qty >= BULK_QTY:
        discount, label = subtotal * BULK_RATE, "Discount (5%)"
    else:
        discount, label = 0.0, None

    return subtotal, discount, label, subtotal - discount