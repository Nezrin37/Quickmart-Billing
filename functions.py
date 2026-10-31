# QuickMart Billing System

# Task 1: Line total
def line_total(item):
    return item["price"] * item["qty"]

# Task 2: Subtotal
def subtotal(cart):
    return sum(line_total(item) for item in cart)

# Task 3: Apply Discount
def apply_discount(amount, percent=0):
    return amount - amount * percent / 100

# Task 4: GST
def gst(amount, rate=18):
    return amount * rate / 100

# Task 5: Category Totals
def category_totals(cart):
    totals = {}

    for item in cart:
        totals[item["category"]] = (
            totals.get(item["category"], 0) + line_total(item)
        )

    return totals

# Task 6: Top Items
def top_items(cart, n=2):
    ranked = sorted(cart, key=line_total, reverse=True)

    return [item["name"] for item in ranked[:n]]

# Task 7: Print Bill
def print_bill(cart, discount_percent=0):

    print(f"{'Item':<10}{'Price':>6}{'Qty':>5}{'Total':>8}")
    print("-" * 29)

    for item in cart:
        print(
            f"{item['name']:<10}"
            f"{item['price']:>6}"
            f"{item['qty']:>5}"
            f"{line_total(item):>8}"
        )

    print("-" * 29)

    sub = subtotal(cart)
    after = apply_discount(sub, discount_percent)
    tax = gst(after)

    print(f"{'Subtotal':<21}{sub:>8.2f}")
    print(f"{'Discount ' + str(discount_percent) + '%':<21}{sub - after:>8.2f}")
    print(f"{'GST 18%':<21}{tax:>8.2f}")
    print(f"{'Grand total':<21}{after + tax:>8.2f}")