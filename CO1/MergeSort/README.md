### Algorithm: Merge Sort for Student Marks

1. **Start**
2. Create a list of students containing their **name and marks**.
3. Check the length of the student list:

   * If the length is `0` or `1`, return the list because it is already sorted.
4. Find the middle position of the list.
5. Divide the list into two halves:

   * Left half
   * Right half
6. Recursively apply **Merge Sort** to both halves.
7. Merge the two sorted halves:

   * Compare the marks of the first student in each half.
   * Place the student with **higher marks first**.
   * Continue until all students are added to the result.
8. Add any remaining students from either half.
9. Return the completely sorted list.
10. Display the students in **descending order of marks**.
11. Check each student's marks:

* If marks are `90` or above, display the student as **eligible for scholarship**.

12. **Stop**.

