import math

def round_2(amount: float) -> float:
    return math.floor(amount * 100 + 0.5) / 100.0


def apply_discount(unit_price: float, qty: int, discount_pct: float) -> dict:
    """
    Returns discount details.
    discount_pct is percentage (e.g., 10 for 10%).
    """
    subtotal = unit_price * qty
    discount_amount = subtotal * (discount_pct / 100.0)
    discounted_subtotal = subtotal - discount_amount

    return {
        "subtotal": round_2(subtotal),
        "discount_pct": discount_pct,
        "discount_amount": round_2(discount_amount),
        "discounted_subtotal": round_2(discounted_subtotal),
    }


def add_gst(amount: float, gst_pct: float) -> dict:
    """
    Returns GST details added on a given amount.
    gst_pct is percentage (e.g., 18 for 18%).
    """
    gst_amount = amount * (gst_pct / 100.0)
    total_with_gst = amount + gst_amount

    return {
        "base_amount": round_2(amount),
        "gst_pct": gst_pct,
        "gst_amount": round_2(gst_amount),
        "total_with_gst": round_2(total_with_gst),
    }


def compute_total(unit_price: float, qty: int, discount_pct: float, gst_pct: float) -> dict:
    """
    Full billing pipeline:
    1) Subtotal
    2) Apply discount
    3) Add GST
    Returns a structured breakdown.
    """
    d = apply_discount(unit_price, qty, discount_pct)
    g = add_gst(d["discounted_subtotal"], gst_pct)

    return {
        "unit_price": round_2(unit_price),
        "qty": qty,
        "subtotal": d["subtotal"],
        "discount_pct": discount_pct,
        "discount_amount": d["discount_amount"],
        "discounted_subtotal": d["discounted_subtotal"],
        "gst_pct": gst_pct,
        "gst_amount": g["gst_amount"],
        "final_total": g["total_with_gst"],
    }
def print_bill(bill: dict) -> None: #Jst for visuals of bill
    print("=" * 40)
    print("BILL SUMMARY")
    print("=" * 40)

    print(f"Unit Price           : {bill['unit_price']:>10.2f}")
    print(f"Quantity             : {bill['qty']:>10}")
    print(f"Subtotal             : {bill['subtotal']:>10.2f}")
    print("-" * 40)

    print(f"Discount (%)         : {bill['discount_pct']:>10.2f}")
    print(f"Discount Amount      : {bill['discount_amount']:>10.2f}")
    print(f"After Discount       : {bill['discounted_subtotal']:>10.2f}")
    print("-" * 40)

    print(f"GST (%)              : {bill['gst_pct']:>10.2f}")
    print(f"GST Amount           : {bill['gst_amount']:>10.2f}")
    print("=" * 40)

    print(f"FINAL TOTAL          : {bill['final_total']:>10.2f}")
    print("=" * 40)

bill = compute_total(23.4,5,20.0,12.0)
print_bill(bill)

