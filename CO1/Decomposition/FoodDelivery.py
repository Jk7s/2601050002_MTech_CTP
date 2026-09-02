# Online Food Delivery System
restaurants = {
    1: {"name": "Pizza Palace", "menu": {"Pizza": 250, "Burger": 150, "Pasta": 200}},
    2: {"name": "Burger House", "menu": {"Burger": 150, "Fries": 100, "Coke": 50}}
}

print("===== FOOD DELIVERY =====")

if input("Username: ") == "user" and input("Password: ") == "1234":

    for i, r in restaurants.items():
        print(i, r["name"])

    r = int(input("Select restaurant: "))

    if r in restaurants:
        menu = restaurants[r]["menu"]
        print("\nMenu:", menu)

        cart = {}
        while True:
            food = input("Food (done to finish): ")

            if food.lower() == "done":
                break

            if food in menu:
                qty = int(input("Quantity: "))
                cart[food] = cart.get(food, 0) + qty
            else:
                print("Not available")

        total = sum(menu[f] * q for f, q in cart.items())

        print("\nCart:", cart)
        print("Total =", total)

        if input("Confirm order? ") == "yes":
            print("\n1. UPI")
            print("2. Cash on Delivery")
            input("Payment: ")

            print("Order Placed")
            print("Food Preparing")
            print("Picked Up")
            print("On the Way")
            print("Delivered")
        else:
            print("Order Cancelled")
    else:
        print("Invalid restaurant")
else:
    print("Invalid Login")
