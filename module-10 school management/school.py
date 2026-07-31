class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}  # {"bengali": teacher_object}
        self.classrooms = {}  # {"eight": classroom_object}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        classname = student.classroom.name
        print("classname", classname, student.name)
        self.classrooms[classname].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks <= 100:
            return "A+"
        elif marks > 70 and marks <= 60:
            return "A"
        elif marks > 60 and marks < 70:
            return "A-"
        elif marks > 50 and marks <= 60:
            return "B"
        elif marks > 40 and marks <= 50:
            return "C"
        elif marks >= 33 and marks <= 40:
            return "D"
        else:
            return "F"

    @staticmethod
    def grade_to_value(grade):
        grades = {
            "A+": 5.00,
            "A- ": 4.00,
            "A-": 3.50,
            "B": 3.00,
            "C": 2.00,
            "D": 1.00,
            "F": 0.00,
        }
        return grades[grade]

    @staticmethod
    def value_to_grade(value):
        if value >= 4.5 and value <= 5.00:
            return "A+"
        elif value >= 3.5 and value < 4.50:
            return "A"
        elif value >= 3.0 and value < 3.5:
            return "A-"
        elif value >= 2.5 and value < 3.0:
            return "B"
        elif value >= 2.0 and value < 2.5:
            return "C"
        elif value >= 1.0 and value < 2.0:
            return "D"
        else:
            return "F"

    def __repr__(self):
        # for k, v in self.classrooms.items():
        #     print(k)
        for key in self.classrooms.keys():
            print(key)

        print("All Students")

        result = ""
        for k, v in self.classrooms.items():
            result += f"---------{k.upper()} classroom students\n"
            for stu in v.students:
                result += f"{stu.name}\n"

        print(result)

        subject = ""
        for k, v in self.classrooms.items():
            subject += f"---------{k.upper()} classroom subjects\n"
            for sub in v.subjects:
                subject += f"{sub.name}\n"

        print(subject)

        print("Students Results")
        for key, value in self.classrooms.items():
            for stu in value.students:
                for k, v in stu.marks.items():
                    print(stu.name, k, v, stu.subject_grade[k])

                print(stu.calculate_final_grade())

        return ""
