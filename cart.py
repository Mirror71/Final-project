# cart.py

import matplotlib.pyplot as plt
from collections import Counter

# Products dictionary
products = {
    "apple": 1.5,
    "banana": 1.0,
    "milk": 2.5,
    "bread": 2.0,
    "oil": 3.5,
    "eggs": 2.8
}

# Cart list
cart = []

# Show all products
def show_products():
    print("\nAvailable Products:")
    for item, price in products.items():
        print(f"- {item.capitalize()}: ${price}")

# Add item to cart
def add_to_cart(item):
    if item in products:
        cart.append(item)
        print(f"{item.capitalize()} added to cart.")
    else:
        print("Item not found.")

# Remove item from cart
def remove_from_cart(item):
    try:
        cart.remove(item)
        print(f"{item.capitalize()} removed from cart.")
    except ValueError:
        print("Item not in cart.")

# View items in cart
def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return
    print("\nYour Cart:")
    total = 0
    for item in cart:
        print(f"- {item.capitalize()} - ${products[item]}")
        total += products[item]
    print(f"Total: ${total:.2f}")

# Visualize cart with a bar chart
def visualize_cart():
    if not cart:
        print("Cart is empty. Nothing to show.")
        return

    counts = Counter(cart)
    items = list(counts.keys())
    quantities = list(counts.values())

    plt.figure(figsize=(6, 4))
    plt.bar(items, quantities, color='skyblue')
    plt.title("Items in Cart")
    plt.xlabel("Item")
    plt.ylabel("Quantity")
    plt.tight_layout()
    plt.show()
