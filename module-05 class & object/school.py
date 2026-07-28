class Student:

    def __init__(self, name, current_class, id):
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self):
        return f"Student with name: {self.name}, class: {self.current_class}, id: {self.id}"


class Teacher:

    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f"Teacher: {self.name}, subject: {self.subject}"


class School:

    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def __repr__(self):
        # Build the formatted string output using line breaks (\n)
        output = [
            f"Welcome to {self.name}",
            "--------------OUR Teachers------------",
        ]
        for teacher in self.teachers:
            output.append(str(teacher))

        output.append("--------------OUR Students------------")
        for student in self.students:
            output.append(str(student))

        # Join everything into a single multi-line string
        return "\n".join(output)

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 100
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return "not enough fee"
        else:
            id = len(self.students) + 1
            student = Student(name, "A", id)
            self.students.append(student)
            return f"{name} is enrolled with id: {id}, extra money {fee - 6500}"


# ================= Execution =================
electron = School("Electron School")

electron.enroll("ali", 6000)  # Fee is less than 6500, will not be enrolled
electron.enroll("rani", 8000)  # Enrolled successfully

electron.add_teacher("tom", "Algorithm")
electron.add_teacher("ajar", "Database")

# Print the school repr data
print(electron)
