products = {
    1: ["Laptop", 50000],
    2: ["Mouse", 1000],
    3: ["Keyboard", 2000],
    4: ["Headphones", 3000],
    5: ["Monitor", 15000]
}

cart = {}


while True:

    print("\n===== SHOPPING CART =====")
    print("1. View Products")
    print("2. Add Product")
    print("3. View Cart")
    print("4. Remove Product")
    print("5. Change Quantity")
    print("6. Final Bill")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    # View products
    if choice == 1:

        for number, product in products.items():
            print(number, product[0], "₹", product[1])

    # Add product
    elif choice == 2:

        for number, product in products.items():
            print(number, product[0], "₹", product[1])

        number = int(input("Enter product number: "))
        quantity = int(input("Enter quantity: "))

        cart[number] = quantity

        print("Product added to cart.")

    # View cart
    elif choice == 3:

        if not cart:
            print("Cart is empty.")

        else:
            for number, quantity in cart.items():
                product = products[number]

                print(
                    product[0],
                    "₹", product[1],
                    "Quantity:", quantity
                )

    # Remove product
    elif choice == 4:

        number = int(input("Enter product number to remove: "))

        if number in cart:
            del cart[number]
            print("Product removed.")
        else:
            print("Product not found.")

    # Change quantity
    elif choice == 5:

        number = int(input("Enter product number: "))
        quantity = int(input("Enter new quantity: "))

        if number in cart:
            cart[number] = quantity
            print("Quantity changed.")
        else:
            print("Product not found.")

    # Final bill
    elif choice == 6:

        subtotal = 0

        for number, quantity in cart.items():

            price = products[number][1]

            subtotal += price * quantity

        print("\nSubtotal:", subtotal)

        discount = float(input("Enter discount percentage: "))

        discount_amount = subtotal * discount / 100

        amount = subtotal - discount_amount

        gst = amount * 18 / 100

        final_amount = amount + gst

        print("Discount:", discount_amount)
        print("GST:", gst)
        print("Final Amount:", final_amount)

    # Exit
    elif choice == 7:

        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice.")