 ### A. Computational Thinking Decomposition, Abstraction & Pattern Recognition:
## 1. Online Food Delivery System
You are asked to design an algorithm for an online food-delivery 
application. The application must handle user login, restaurant selection, 
food ordering, payment, and delivery tracking.
# Question: 
How would you decompose this large problem into smaller subproblems?
# Solution
According to the scenario, the large Online Food Delivery problem can be divided into smaller sub-problems using Decomposition.

# Example – Swiggy

Imagine a user wants to order food using Swiggy.
# Decomposition

The complete food-ordering process is divided into smaller tasks:

Login → Select Location → Select Restaurant → Select Food → Add to Cart → Payment → Delivery Tracking

1. User login
2. Select restaurant
3. Select food items
4. Add food to cart
5. Place order
6. Make payment
7. Track delivery
8. Complete order

Suppose the user orders:

| Food Item | Quantity |    Price |
| --------- | -------: | -------: |
| Burger    |        1 |     ₹150 |
| Coke      |        2 |     ₹100 |
| **Total** |          | **₹250** |

Then the process is:

**Burger + Coke → Add to Cart → ₹250 → Payment → Food Prepared → Delivered**

# Algorithm

### Input

* Username and password
* Restaurant selection
* Food items
* Quantity
* Payment method

### Steps

1. **Start**
2. Enter username and password.
3. Check whether the login details are valid.
4. Display available restaurants.
5. Select a restaurant.
6. Display the restaurant menu.
7. Select a food item and enter its quantity.
8. Add the food item to the cart.
9. Repeat Steps 7–8 until the user enters **"done"**.
10. Calculate the total bill.
11. Display the cart and total amount.
12. Ask the user to confirm the order.
13. If the order is confirmed, select a payment method.
14. Process the payment.
15. If payment is successful, confirm the order.
16. If payment fails, cancel the order.
17. Display the delivery status.
18. Mark the order as delivered.
19. **Stop**

---

# Python Implementation

```python
# Online Food Delivery System

restaurants = {
    1: {"name": "Pizza Palace",
        "menu": {"Pizza": 250, "Burger": 150, "Pasta": 200}},
    2: {"name": "Burger House",
        "menu": {"Burger": 150, "Fries": 100, "Coke": 50}}
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

        if input("Confirm order? ").lower() == "yes":

            print("\n1. UPI")
            print("2. Cash on Delivery")

            payment = int(input("Payment: "))

            if payment == 1:
                result = input("Payment successful? (yes/no): ")

                if result.lower() == "yes":
                    print("Payment Successful")
                else:
                    print("Payment Failed")
                    print("Order Cancelled")
                    exit()

            elif payment == 2:
                print("Cash on Delivery selected")

            else:
                print("Invalid Payment")
                exit()

            print("\nOrder Placed")
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
```

# Output

Example:

```text
===== FOOD DELIVERY =====

Username: user
Password: 1234

1 Pizza Palace
2 Burger House

Select restaurant: 1

Menu: {'Pizza': 250, 'Burger': 150, 'Pasta': 200}

Food (done to finish): Pizza
Quantity: 2

Food (done to finish): Pasta
Quantity: 1

Food (done to finish): done

Cart: {'Pizza': 2, 'Pasta': 1}
Total = 700

Confirm order? yes

1. UPI
2. Cash on Delivery

Payment: 1
Payment successful? (yes/no): yes

Payment Successful

Order Placed
Food Preparing
Picked Up
On the Way
Delivered
```

# Time Complexity

### Best Case

**O(1)**

If the user performs only a constant amount of work, such as logging in and stopping without adding food items.

### Worst Case

**O(K)**
where K is number of food items added to the cart
If the user orders a large number of food items, the loop and bill calculation process all those items.
