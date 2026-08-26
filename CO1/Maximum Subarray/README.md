## 3. Stock Profit — Maximum Subarray

### Object

To find the **continuous sequence of days that gives the maximum total profit** from a list of daily stock profits and losses.

### Algorithm

1. Start.
2. Store the daily profit/loss values in an array.
3. Initialize `current_sum` and `max_sum` with the first value.
4. Traverse the array from the second element.
5. Add the current value to `current_sum`.
6. If the current value is greater than `current_sum`, start a new subarray from the current value.
7. Compare `current_sum` with `max_sum`.
8. If `current_sum` is greater, update `max_sum`.
9. Continue until all values are checked.
10. Record the starting and ending positions of the maximum subarray.
11. Display the maximum profit and the corresponding continuous period.
12. Stop.
