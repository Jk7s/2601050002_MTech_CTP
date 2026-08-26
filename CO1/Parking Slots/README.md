### Algorithm: Parking Slot Management System

1. **Start**
2. Create a parking system with **100 slots**.
3. Store the already booked slots along with:

   * Vehicle type (`2W` or `4W`)
   * Entry time
4. Display the menu:

   * Show Slots
   * Book Slot
   * Release Slot
   * Exit

### Show Slots

5. Display slots from **1 to 100**.
6. If a slot is booked, display `*`.
7. Otherwise, display the slot number.
8. Display the number of available slots.

### Book Slot

9. Check whether all 100 slots are booked.

   * If yes, display **"Parking area is full."**
10. Ask the user to select the vehicle type:

* `1` → Two Wheeler
* `2` → Four Wheeler

11. Ask the user to enter the slot number.
12. Check whether the slot number is between `1` and `100`.
13. Check whether the selected slot is already booked.
14. If the slot is available:

* Store the vehicle type.
* Store the current entry time.
* Display **"Slot booked successfully."**

### Release Slot

15. Ask the user to enter the slot number.
16. Check whether the slot is booked.
17. If it is not booked, display **"Slot is already empty."**
18. Get the vehicle type and entry time.
19. Record the current time as the exit time.
20. Calculate the parking duration in hours.
21. Round the duration up to the next whole hour, with a minimum charge of **1 hour**.
22. Calculate the parking charge:

* Two Wheeler → `hours × ₹20`
* Four Wheeler → `hours × ₹40`

23. Display:

* Exit time
* Parking duration
* Parking charge

24. Remove the slot from the booked slots.
25. Display **"Slot released successfully."**

### Main Parking System

26. Continue displaying the menu until the user selects **Exit**.
27. Perform the selected operation.
28. If an invalid choice is entered, display **"Invalid choice."**
29. **Stop**.

