### Algorithm: Library Book Search Using Binary Search

1. **Start**
2. Create a sorted array containing book numbers from `1` to `1,000,000`.
3. Take the **book number** to be searched as input.
4. Set:

   * `low = 0`
   * `high = length of array - 1`
5. Repeat while `low <= high`:

   * Calculate the middle position:
     `mid = low + (high - low) // 2`
   * If `array[mid] == target`:

     * The book is found.
     * Return `mid`.
   * If `array[mid] < target`:

     * Search the right half.
     * Set `low = mid + 1`.
   * Otherwise:

     * Search the left half.
     * Set `high = mid - 1`.
6. If the loop ends without finding the book, return `-1`.
7. If the result is `-1`, display **"book not found"**.
8. Otherwise, display the position of the book.
9. **Stop**.
