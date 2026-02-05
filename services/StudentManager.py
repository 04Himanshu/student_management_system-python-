from models.student import Student
from utils import validators


class StudentManager:
    def __init__(self):
        self._students = []   # protected by convention

    def add_student(self, student: Student):
        if self.get_student(student.roll_no):
            raise ValueError("Student with this ID already exists")
        self._students.append(student)

    def get_student(self, roll_no):
        for student in self._students:
            if student.roll_no == roll_no:
                return student
        return None

    def remove_student(self, roll_no):
        student = self.get_student(roll_no)
        if not student:
            raise ValueError("Student not found")
        self._students.remove(student)

    def update_student(self, roll_no, name=None, age=None, course=None, marks=None):
        student = self.get_student(roll_no)
        if not student:
            raise ValueError("Student not found")

        if name is not None:
            student.name = name
        if age is not None:
            validators.validate_age(age)
            student.age = age
        if course is not None:
            student.course = course
        if marks is not None:
            validators.validate_marks(marks)
            student.marks = marks

    def student_list(self):
        return self._students
