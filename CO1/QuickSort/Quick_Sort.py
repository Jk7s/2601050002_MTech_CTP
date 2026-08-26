employees = [
    ["Rahul", 45000],
    ["Anitha", 65000],
    ["Vivek", 48000],
    ["Lakshmi", 72000],
    ["Ramesh", 55000]
]


def quick_sort(arr, low, high):

    if low < high:

        pivot = arr[high][1]
        i = low - 1

        for j in range(low, high):

            if arr[j][1] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        p = i + 1

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


quick_sort(employees, 0, len(employees) - 1)


print("Employees sorted by salary:")

for employee in employees:
    print(employee[0], employee[1])


print("\nBonus Eligible Employees:")

for employee in employees:

    if employee[1] >= 50000:
        print(employee[0], employee[1])