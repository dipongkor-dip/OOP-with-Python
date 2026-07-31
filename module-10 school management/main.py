from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School("Northern School", "Dhaka")

# adding Classroom
eight = ClassRoom("eight")
nine = ClassRoom("nine")
ten = ClassRoom("ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# adding students
sunny = Student("Sunny", eight)
asa = Student("asa", nine)
hay = Student("ahy", nine)
kan = Student("kan", ten)
fun = Student("fun", eight)
alo = Student("Alo", ten)
asi = Student("Asi", ten)

school.student_admission(sunny)
school.student_admission(asa)
school.student_admission(hay)
school.student_admission(kan)
school.student_admission(fun)
school.student_admission(alo)
school.student_admission(asi)


abu = Teacher("Abu Khan")
lil = Teacher("Lil Khan")
ali = Teacher("Ali Khan")

# adding subject
biology = Subject("Biology", abu)
physics = Subject("Physics", lil)
math = Subject("Math", ali)
chemistry = Subject("Chemistry", lil)

eight.add_subject(biology)
eight.add_subject(physics)
eight.add_subject(math)
eight.add_subject(chemistry)

nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(math)

ten.add_subject(chemistry)
ten.add_subject(physics)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)
