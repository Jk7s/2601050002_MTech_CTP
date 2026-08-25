def merge_sort(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2

    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # Descending order
        if left[i][1] >= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


students = [
    ("Rahul", 85),
    ("Priya", 95),
    ("Arun", 72),
    ("Sneha", 90),
    ("Kiran", 88),
    ("Anu", 97)
]

students = merge_sort(students)

print("Students sorted by marks:")
for name, marks in students:
    print(name, marks)

print("\nStudents eligible for scholarship:")
for name, marks in students:
    if marks >= 90:
        print(name)
