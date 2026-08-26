## 2. Hospital Locations — Closest Pair

### Object

To find the **two hospitals that are geographically closest to each other** using their `(x, y)` coordinates.

### Algorithm

1. Start.

2. Store the names and coordinates `(x, y)` of all hospitals.

3. Select the first hospital.

4. Compare it with every other hospital.

5. Calculate the distance between the two hospitals using:

   `Distance = √((x2-x1)² + (y2-y1)²)`

6. Store the smallest distance found.

7. Repeat the comparison for all possible pairs of hospitals.

8. Store the names of the two hospitals having the smallest distance.

9. Display the closest hospitals and their distance.

10. Stop.
