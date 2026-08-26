profits = [-2, 3, -1, 5, -6, 4, 2]

current_sum = profits[0]
max_sum = profits[0]

start = 0
best_start = 0
best_end = 0


for i in range(1, len(profits)):

    if current_sum + profits[i] < profits[i]:
        current_sum = profits[i]
        start = i
    else:
        current_sum += profits[i]

    if current_sum > max_sum:
        max_sum = current_sum
        best_start = start
        best_end = i


print("Maximum Profit:", max_sum)

print("Profit Period:")

for i in range(best_start, best_end + 1):
    print(profits[i], end=" ")