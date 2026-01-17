student_marks = {
    "Joey": 85,
    "Chandler": 92,
    "Monika": 78,
    "Rachel": 88,
    "Ross": 95
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")




