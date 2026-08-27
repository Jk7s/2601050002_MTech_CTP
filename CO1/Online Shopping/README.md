## Objective

To develop asimple shopping cart system in Python

## Algorithm

1. **Start**
2. Create a dictionary containing the **product number, product name, and price**.
3. Create an empty dictionary called `cart` to store selected products and their quantities.
4. Display the shopping cart menu.
5. Ask the user to enter their choice.
6. If the choice is **1**, display all available products.
7. If the choice is **2**:

   * Display the products.
   * Ask for the product number and quantity.
   * Add the product and quantity to the cart.
8. If the choice is **3**:

   * Check whether the cart is empty.
   * If not empty, display each product, price, and quantity.
9. If the choice is **4**:

   * Ask for the product number.
   * If it exists in the cart, remove it.
10. If the choice is **5**:

    * Ask for the product number and new quantity.
    * Update the quantity if the product exists in the cart.
11. If the choice is **6**:

    * Calculate the subtotal using:
      **Price × Quantity**
    * Ask for the discount percentage.
    * Calculate the discount amount.
    * Subtract the discount from the subtotal.
    * Calculate **18% GST**.
    * Add GST to get the final amount.
    * Display the bill details.
12. If the choice is **7**, display a thank-you message and stop the program.
13. For any other choice, display **Invalid choice**.
14. **Repeat steps 4–13 until the user chooses Exit.**
15. **Stop**.
