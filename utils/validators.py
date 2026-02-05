def validate_age(age):
    if age <= 0:
        raise ValueError("Age must be positive")

def validate_marks(marks):
    if not (0 <= marks <= 100):
        raise ValueError("Marks must be between 0 and 100")
