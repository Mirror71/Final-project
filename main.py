
# main.py

import cart

def menu():
    print("\n==== Shopping Cart Menu ====")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Exit")
    print("6. Visualize Cart")

while True:
    try:
        menu()
        choice = int(input("Choose an option (1-6): "))

        if choice == 1:
            cart.show_products()
        elif choice == 2:
            item = input("Enter item to add: ").lower()
            cart.add_to_cart(item)
        elif choice == 3:
            item = input("Enter item to remove: ").lower()
            cart.remove_from_cart(item)
        elif choice == 4:
            cart.view_cart()
        elif choice == 5:
            with open("cart_summary.txt", "w") as file:
                file.write("Your Cart:\n")
                total = 0
                for item in cart.cart:
                    price = cart.products[item]
                    file.write(f"- {item.capitalize()}: ${price}\n")
                    total += price
                file.write(f"\nTotal: ${total:.2f}")
            print("Cart saved to cart_summary.txt. Goodbye!")
            break
        elif choice == 6:
            cart.visualize_cart()
        else:
            print("Invalid choice. Choose from 1 to 6.")
    except Exception as e:
        print("Error:", e)
