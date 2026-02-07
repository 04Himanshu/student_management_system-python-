import json
import os

class StudentRepository:
    def __init__(self, file_path="Student_management\\data\\students.json"):
        self.file_path = file_path

    def load_students(self) -> list:
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    def save_students(self, students: list) -> None:
        with open(self.file_path, "w") as file:
            json.dump(students, file, indent=4)