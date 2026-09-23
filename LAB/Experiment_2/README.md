# 0/1 Knapsack using Dynamic Programming

## 1. Algorithm / Procedure

1. Read the weights, values, and knapsack capacity.
2. Create a DP table.
3. For each item, check whether it can fit in the knapsack.
4. If it fits, choose the maximum of:

   * Including the item
   * Excluding the item
5. If it does not fit, exclude the item.
6. The last cell gives the maximum value.

---

## 2. Very Simple Python Code

```python
def knapsack(w, v, c):
    n = len(w)
    dp = [[0] * (c + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(c + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(v[i - 1] + dp[i - 1][j - w[i - 1]],
                               dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][c]


w = [2, 3, 4, 5]
v = [3, 4, 5, 6]
c = 5

print("Maximum value:", knapsack(w, v, c))
```

---

## 3. Input

```text
Weights: 2 3 4 5
Values:  3 4 5 6
Capacity: 5
```

## 4. Output

```text
Maximum value: 7
```

The items with **weight 2 and 3** are selected.

---

## 5. Inference

The 0/1 Knapsack problem is successfully solved using **Dynamic Programming**. The maximum value obtained is **7**.

---

## 6. Analysis

For `n` items and capacity `c`:

* **Time Complexity:** `O(n × c)`
* **Space Complexity:** `O(n × c)`

The DP table stores the best value for each item and capacity.

