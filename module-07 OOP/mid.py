class StudentDatabase:
    student_list = []

    @classmethod  # class method for task 1
    def add_student(self, student_data):
        self.student_list.append(student_data)


class Student:
    def __init__(self, student_id, name, department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = True

        StudentDatabase.add_student(self)

    def get_stu_id(self):
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled == False:
            self.__is_enrolled = True
            print(f"{self.__name} has been enrolled.")
        else:
            print(f"{self.__name} is already enrolled.")

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"{self.__name} has dropped out.")
        else:
            print(f"{self.__name} is not enrolled.")

    def view_student_info(self):
        print(
            f"ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__is_enrolled}"
        )


Student(101, "Sunny", "Physics")
Student(102, "Alo", "Biology")
Student(103, "dip", "Chemistry")
# s = Student(103, "dip", "Chemistry")
# s.view_student_info()

# Menu System

while True:

    print("============= Students Database ==============")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        print("\n--- ALL STUDENTS ---")
        if not StudentDatabase.student_list:
            print("No students found in database.")
        else:
            for student in StudentDatabase.student_list:
                student.view_student_info()

    elif choice == "2":
        print("\n--- ENROLL STUDENT ---")
        s_id = int(input("Enter Student ID to enroll: "))

        flag = False

        for s in StudentDatabase.student_list:
            if s.get_stu_id() == s_id:
                flag = True
                s.enroll_student()
                s.view_student_info()
                break

        if not flag:
            print(f"Error: Invalid Student ID ({s_id}). Not found.")

    elif choice == "3":
        print("\n--- DROP STUDENT ---")
        s_id = int(input("Enter Student ID to drop: "))

        flag = False

        for s in StudentDatabase.student_list:
            if s.get_stu_id() == s_id:
                flag = True
                s.drop_student()
                s.view_student_info()
                break

        if not flag:
            print(f"Error: Invalid Student ID ({s_id}). Not found.")

    elif choice == "4":
        print("\nExiting system.")
        break

    else:
        print("Invalid option! Please enter a number between 1 and 4.")

    print("\n")
