def calculate_average(marks):
    if len(marks) == 0:
        return None

    for mark in marks:
        if mark < 0 or mark > 100:
            return None

    return sum(marks) / len(marks)


def classify_performance(average):
    if average is None:
        return "Invalid Marks"

    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def display_report(students):
    if len(students) == 0:
        print("No student records available.")
        return

    for s in students:
        average = calculate_average(s[2])

        print("ID:", s[0])
        print("Name:", s[1])

        if average is None:
            print("Average: Invalid")
            print("Performance: Invalid Marks")
        else:
            print("Average:", round(average, 2))
            print("Performance:", classify_performance(average))

        print()


students = [
    [201, "Sufian", [78, 85, 90]],
    [202, "Showrov", [65, 70, 68]],
    [203, "Sufu", [92, 88, 95]],
    [204, "Zishan", [55, 60, 65]],
    [205, "Simon", [80, 80, 80]]
]

display_report(students)