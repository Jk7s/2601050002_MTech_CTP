def get_student_data():
    """Takes input for each student: name, total classes, classes attended."""
    students = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Enter student name: ")
        total_classes = int(input(f"Enter total classes conducted for {name}: "))
        attended = int(input(f"Enter classes attended by {name}: "))
        students[name] = {"total": total_classes, "attended": attended}
    return students

def calculate_percentage(students):
    """Calculates attendance % for each student."""
    percentages = {}
    for name, data in students.items():
        percent = (data["attended"] / data["total"]) * 100
        percentages[name] = round(percent, 2)
    return percentages

def below_threshold(percentages, threshold=75):
    """Returns list of students below the given attendance threshold."""
    return [name for name, pct in percentages.items() if pct < threshold]

def highest_attendance(percentages):
    """Returns the student with the highest attendance percentage."""
    return max(percentages, key=percentages.get)

def class_average(percentages):
    """Calculates the average attendance percentage of the whole class."""
    return round(sum(percentages.values()) / len(percentages), 2)

def display_report(percentages, below_75, topper, avg):
    print("\n----- Student Attendance Report -----")
    for name, pct in percentages.items():
        print(f"{name}: {pct}%")

    print("\nStudents below 75% attendance:")
    if below_75:
        for name in below_75:
            print(f"- {name}")
    else:
        print("None")

    print(f"\nStudent with highest attendance: {topper} ({percentages[topper]}%)")
    print(f"Class average attendance: {avg}%")


def main():
    students = get_student_data()
    percentages = calculate_percentage(students)
    below_75 = below_threshold(percentages)
    topper = highest_attendance(percentages)
    avg = class_average(percentages)
    display_report(percentages, below_75, topper, avg)


if __name__ == "__main__":
    main()