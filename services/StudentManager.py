from models.student import Student
from repository.studentRepository import StudentRepository
from utils import validators 


class StudentManager:
    def __init__(self):
        self.repository = StudentRepository()
        self.student = self._load_students()

    def _load_students(self): 
        student_dicts = self.repository.load_students()
        return [Student.from_dict(data) for data in student_dicts]

    def _save_students(self):
        student_dicts = [student.to_dict() for student in self.student]
        self.repository.save_students(student_dicts)

    def add_student(self, student: Student):
        if self.get_student(student.roll_no):
            raise ValueError("Student with this ID already exists")
        
        validators.validate_marks(student.marks)
        self.student.append(student)
        self._save_students()

    def get_student(self, roll_no):
        for student in self.student:
            if student.roll_no == roll_no:
                return student
        return None

    def remove_student(self, roll_no):
        student = self.get_student(roll_no)
        if not student:
            raise ValueError("Student not found")

        self.student.remove(student)
        self._save_students()

    def update_student(self, roll_no, name=None, age=None, course=None, marks=None):
        student = self.get_student(roll_no)
        if not student:
            raise ValueError("Student not found")

        if name is not None:
            student.name = name
        if age is not None:
            student.age = age
        if course is not None:
            student.course = course
        if marks is not None:
            validators.validate_marks(marks)
            student.marks = marks

        self._save_students()

    def student_list(self):
        return self.student
