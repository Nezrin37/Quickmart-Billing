
# QuickMart Billing System
# Main Program

# Import user-defined functions
from functions import (
    line_total,
    subtotal,
    apply_discount,
    gst,
    category_totals,
    top_items,
    print_bill
)

# Starter Data
cart = [
    {"name": "Notebook", "category": "Stationery", "price": 40, "qty": 5},
    {"name": "Pen", "category": "Stationery", "price": 10, "qty": 11},
    {"name": "Biscuits", "category": "Snacks", "price": 25, "qty": 4},
    {"name": "Juice", "category": "Drinks", "price": 45, "qty": 3},
    {"name": "Chips", "category": "Snacks", "price": 20, "qty": 6}
]

# Main Function
def main():

    # Task 1: Line Total
    print("Task 1: Line total")
    print(line_total(cart[0]))

    # Task 2: Subtotal
    print("\nTask 2: Subtotal")
    print(subtotal(cart))

    # Task 3: Discount
    print("\nTask 3: Discount")
    print(apply_discount(500))
    print(apply_discount(500, 10))

    # Task 4: GST
    print("\nTask 4: GST")
    print(gst(100))
    print(gst(100, 5))

    # Task 5: Category Totals
    print("\nTask 5: Category totals")

    for cat, total in sorted(category_totals(cart).items()):
        print(f"{cat:<12}{total}")

    # Task 6: Top Items
    print("\nTask 6: Top items")
    print(top_items(cart))
    print(top_items(cart, 3))

    # Task 7: Bill
    print("\nTask 7: Bill")
    print_bill(cart, 10)

    # Task 8: Tests
    print("\nTask 8: Tests")

    assert line_total({
        "name": "x",
        "category": "y",
        "price": 5,
        "qty": 3
    }) == 15

    assert apply_discount(200, 50) == 100

    assert gst(200) == 36

    assert top_items(cart, 1) == ["Notebook"]

    print("All tests passed")

# Calling Main Function
if __name__ == "__main__":
    main()