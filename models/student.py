class Student:
    def __init__(self,roll_no,name,age,marks,course):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks
        self.course = course
    
    def __str__(self):
        return(
            f"Roll_No: {self.roll_no} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Marks: {self.marks} | "
            f"Course: {self.course} | "
        )
    
    def to_dict(self) -> dict:
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "marks": self.marks,
            "course": self.course
        }

    @staticmethod
    def from_dict(data: dict):
        return Student(
            int(data["roll_no"]),
            data["name"],
            int(data["age"]),
            int(data["marks"]),
            data["course"]
        )