from person import Person
from course import Course
from student import Student
from university_system import UniversitySystem

class Admin(Person):
    
    def __init__(self,name,id):
        super().__init__(name,id)
    
    @classmethod
    def add_student(cls,name,id):
        print("Adding Student: ")
        student = Student(name,id)
        UniversitySystem.add_student(student)

    @classmethod
    def remove_student(cls,id):
        print("Removing Student:")
        student = UniversitySystem.get_student(id)
        UniversitySystem.remove_student(student)

    @classmethod
    def view_student(cls,id):
        student = UniversitySystem.get_student(id)
        if not student:
            return 
        print(f"Name: {student.name}\nID: {student.id}")
        courses_codes = [str(a) for a in list(student.enrolled_courses.keys())]
        print("Enrolled Courses:","  ".join([UniversitySystem.get_course(code).name for code in courses_codes]))
    
    @classmethod
    def add_course(cls,name,code):
        print("Adding Course")
        course = Course(name,code)
        UniversitySystem.add_course(course)

    @classmethod
    def remove_course(cls,code):
        print("Removing Course")
        course = UniversitySystem.get_course(code)
        UniversitySystem.remove_course(course)
    
    @classmethod
    def view_course(cls,code):
        course = UniversitySystem.get_course(code)
        if not course:
            return 
        print(f"Name: {course.name}\nCode: {course.code}")
        print("Students Enrolled:","  ".join([student.name for student in course.students]))
    
    @classmethod
    def add_instructor(cls,name,id):
        print("Adding instructor: ")
        instructor = instructor(name,id)
        UniversitySystem.add_instructor(instructor)

    @classmethod
    def remove_instructor(cls,id):
        print("Removing instructor:")
        instructor = UniversitySystem.get_instructor(id)
        UniversitySystem.remove_instructor(instructor)

    @classmethod
    def view_instructor(cls,id):
        instructor = UniversitySystem.get_instructor(id)
        if not instructor:
            return 
        print(f"Name: {instructor.name}\nID: {instructor.id}")
        courses_codes = [str(a) for a in list(instructor.courses)]
        print("Assigned Courses:","  ".join([UniversitySystem.get_course(code).name for code in courses_codes]))