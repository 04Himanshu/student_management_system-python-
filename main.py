from models.student import Student
from services.StudentManager import StudentManager
from utils import InputHelper


def show_menu():
    print("\n------ Student Management System ------")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student")
    print("4. View Student")
    print("5. List All Students")
    print("6. Exit")


def main():
    manager = StudentManager()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        try:
            match choice:
                case "1":  # Add student
                    student_id = InputHelper.safe_int_input("Enter Id: ")
                    name = input("Enter name: ")
                    age = int(input("Enter age: "))
                    course = input("Enter course: ")
                    marks = float(input("Enter marks: "))

                    student = Student(student_id, name, age, course, marks)
                    manager.add_student(student)
                    print("Student added successfully.")

                case "2":  # Remove student
                    student_id = int(input("Enter student ID to remove: "))
                    manager.remove_student(student_id)
                    print("Student removed successfully.")

                case "3":  # Update student
                    student_id = int(input("Enter student ID to update: "))
                    name = input("Enter new name (leave blank to skip): ")
                    age = input("Enter new age (leave blank to skip): ")
                    course = input("Enter new course (leave blank to skip): ")
                    marks = input("Enter new marks (leave blank to skip): ")

                    manager.update_student(
                        student_id,
                        name=name if name else None,
                        age=int(age) if age else None,
                        course=course if course else None,
                        marks=float(marks) if marks else None
                    )
                    print("Student updated successfully.")

                case "4":  # View student
                    student_id = int(input("Enter student ID: "))
                    student = manager.get_student(student_id)
                    if student:
                        print(student)
                    else:
                        print("Student not found.")

                case "5":  # List all students
                    students = manager.student_list()
                    if not students:
                        print("No students available.")
                    else:
                        for student in students:
                            print(student)

                case "6":  # Exit
                    print("Exiting system. Goodbye!")
                    break

                case _:
                    print("Invalid choice. Please try again.")

        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()