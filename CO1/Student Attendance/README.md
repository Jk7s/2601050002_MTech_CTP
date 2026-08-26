### Algorithm: Student Attendance Management System

1. **Start**
2. Get the number of students `n`.
3. For each student:

   * Enter the student's name.
   * Enter the total number of classes conducted.
   * Enter the number of classes attended.
   * Store the details.
4. Calculate the attendance percentage for each student using:

   * `Attendance % = (Classes Attended / Total Classes) × 100`
5. Store the calculated percentage for every student.
6. Check each student's percentage:

   * If percentage `< 75`, add the student to the below-threshold list.
7. Find the student with the **highest attendance percentage**.
8. Calculate the **class average attendance**:

   * `Average = Sum of all attendance percentages / Number of students`
9. Display:

   * Each student's attendance percentage.
   * Students below 75%.
   * Student with the highest attendance.
   * Class average attendance.
10. **Stop**.

