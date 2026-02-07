from models.student import Student
from services.StudentManager import StudentManager
from utils.InputHelper import safe_int_input

def main():
    manager = StudentManager()

    while True:
        print("\n------ Student Management System (v2) ------")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Remove Student")
        print("5. View All Students")
        print("0. Exit")

        choice = int(input("Enter choice: "))

        try:
            match choice:
                case 1:
                    roll_no = safe_int_input("Roll_No: ")
                    name = input("Name: ")
                    age = int(input("Age: "))
                    marks = safe_int_input("Marks: ") 
                    course = input("Course: ") 

                    student = Student(roll_no, name, age , marks, course)
                    manager.add_student(student)
                    print("Student added successfully.")

                case 2:
                    roll_no = int(input("Enter Roll No: "))
                    student = manager.get_student(roll_no)
                    if student:
                        print(student.__dict__)
                    else:
                        print("Student not found.")

                case 3:
                    roll_no = int(input("Enter Roll No: "))
                    print("Leave field empty to skip update")

                    name = input("New Name: ").strip() or None
                    age_input = input("New Age: ").strip()
                    age = int(age_input) if age_input else None
                    course = input("New Course: ").strip() or None
                    marks_input = input("New Marks: ").strip()
                    marks = int(marks_input) if marks_input else None

                    manager.update_student(roll_no, name, age, course, marks)
                    print("Student updated successfully.")

                case 4:
                    roll_no = int(input("Enter Roll No: "))
                    manager.remove_student(roll_no)
                    print("Student removed successfully.")

                case 5:
                    students = manager.student_list()
                    if not students:
                        print("No students available.")
                    for student in students:
                        print(student.__dict__)

                case 0:
                    print("Exiting... Goodbye!")
                    break

                case _:
                    print("Invalid choice.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()