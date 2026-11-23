def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


students = []
total_marks = 0

while True:
    try:
        student_count = int(input("How many students do you want to enter? "))

        if student_count > 0:
            break

        print("Please enter at least 1 student.")
    except ValueError:
        print("Please enter a whole number.")

for student_number in range(1, student_count + 1):
    print(f"\nStudent {student_number}")
    name = input("Enter the student's name: ").strip()

    while True:
        try:
            marks = float(input("Enter marks (0–100): "))

            if 0 <= marks <= 100:
                break

            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a number, such as 85 or 85.5.")

    grade = get_grade(marks)
    students.append((name, marks, grade))
    total_marks += marks

average = total_marks / student_count

print("\nStudent Results")
print(f"{'Name':<20} {'Marks':>8} {'Grade':>8}")
print("-" * 38)

for name, marks, grade in students:
    print(f"{name:<20} {marks:>8.2f} {grade:>8}")

print(f"\nClass average: {average:.2f} out of 100")