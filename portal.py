from university_system import UniversitySystem
from admin import Admin
from student import Student

UniversitySystem.create_tables()

class GPA_Calculator:
     
    @classmethod
    def auto_GPA_calculate(cls,student):
        gpa_scale = {
        "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "F": 0.0
    }
        if not student.enrolled_courses:
             return 0.0
        
        sum = 0.0
        for grade in student.enrolled_courses.values():
            if grade:
                sum += gpa_scale[grade]
        GPA = sum / len(student.enrolled_courses)
        student.update_GPA(GPA)
        return GPA
        
    @classmethod
    def view_GPA(cls,student):
        print(f"{student.name}'s GPA: {student.GPA}")

    @classmethod
    def get_GPA(cls,student):
        return student.GPA
    
    @classmethod
    def calculate_GPA():
        print("GPA Calculator")
        gpa_scale = {
        "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "F": 0.0
    }
        match input("Enter grades separated by space: ").split():
            case [*grades]:
                sum = 0.0
                for grade in grades:
                    if grade in gpa_scale:
                        sum += gpa_scale[grade]
                    else:
                        print(f"Invalid grade: {grade}")
                GPA = sum / len(grades)
                print(f"GPA: {GPA}")
            case _:
                print("Invalid input")

class Portal:

    @classmethod
    def admin(cls):
        while True:
            # try:
                x = input("Admin:\n1. Student\n2. Course\n0. Back ")
                match x:
                    case '1':
                        while True:
                            # try:
                                x = input("1. Add Student\n2. Remove Student\n3. View Student information\n0.Back ")
                                match x:
                                    case '1':
                                        Admin.add_student(input("Name: "),input("ID: "))
                                    case '2':
                                        Admin.remove_student(input("ID: "))
                                    case '3':
                                        Admin.view_student(input("ID: "))
                                    case '0':
                                        break
                                    case _:
                                        print(f"Invalid: {x}\n")
                    case '2':
                        while True:
                                x = input("1. Add Course\n2. Remove Course\n3. View Course\n0. Back ")
                                match x:
                                    case '1':
                                        Admin.add_course(input("Name: "),input("Code: "))
                                    case '2':
                                        Admin.remove_course(input("Code: "))
                                    case '3':
                                        Admin.view_course(input("Code: "))
                                    case '0':
                                        break
                                    case _:
                                        print(f"Invalid {x}\n")
                    case '0':
                        break
                    case _:
                        print(f"Invalid {x}\n")

    @classmethod
    def student(cls,id):
        student = UniversitySystem.get_student(id)
        if not student:
            return
        print("Logged in as",student.name)
        while True:
                x = input("1. View Information\n2. Enroll\n3. GPA Calculator\n0. Back ")
                match x:
                    case '1':
                        Admin.view_student(student.id)
                    case '2':
                        course = UniversitySystem.get_course(input("Code: "))
                        if not course:
                             continue
                        student.enroll(course)
                        UniversitySystem.update_enrolled_courses(student)
                        UniversitySystem.update_course_students(course)
                    case '3':
                        cls.GPA_calculator(student)
                    case '0':
                        break
                    case _:
                        print(f"Invalid {x}\n")

    @classmethod
    def instructor(cls, id):
        instructor = UniversitySystem.get_instructor(id)
        if not instructor:
            return
        print("Logged in as",instructor.name)
        while True:
                x = input("\n1. View Information\n2. Assign Course\n3. Assign Grades\n0. Back ")
                match x:
                    case '1':
                        Admin.view_instructor(instructor.id)
                    case '2':
                        course = UniversitySystem.get_course(input("Code: "))
                        if not course:
                             continue
                        instructor.add_course(course)
                        UniversitySystem.update_instructor_courses(instructor)
                        print(f"Course {course.name} assigned to {instructor.name}")
                    case '3':
                        student = UniversitySystem.get_student(input("Student ID: "))
                        if not student:
                            continue
                        course = UniversitySystem.get_course(input("Course Code: "))
                        if not course:
                            continue
                        instructor.assign_grade(student,course,input("Grades: "))
                        UniversitySystem.update_enrolled_courses(student)
                        GPA_Calculator.auto_GPA_calculate(student)
                    case '0':
                        break
                    case _:
                        print(f"Invalid {x}\n")
            # except Exception as a:
                # print(a)

    @classmethod
    def GPA_calculator(cls,student):
        print("GPA Calculator")
        while True:
            # try:
                match input("1. Calculate GPA\n2. View GPA\n0. Back "):
                    case '1':
                        GPA_Calculator.calculate_GPA()
                    case '2':
                        print(f"{student.name}'s GPA: {GPA_Calculator.view_GPA(student)}")
                    case '0':
                        break
                    case _:
                        print(f"Invalid {x}\n")
            # except Exception as a:
                # print(a)

while True:
    # try:
        x = input("Login as: \n1. Admin\n2. Student\n3. Instructor\n0. Exit ")
        match x:
            case '1':
                Portal.admin()
            case '2':
                id = input("Logging in as Studet: \nID: ")
                Portal.student(id)
            case '3':
                Portal.instructor(input("Logging in as Instructor: \nID: "))
            case '0':
                break
            case _:
                print(f"Invalid {x}\n")
    # except Exception as a:
        # print(a)

UniversitySystem.close_connection()
