from person import Person

class Instructor(Person):
    
    def __init__(self,name,id):
        super().__init__(name,id)
        self.courses = []
    
    def assign_grade(self,student,course,grade):
        if course in self.courses and course.code in student.enrolled_courses:
            student.enrolled_courses[course.code] = grade
            print(f"{self.name} assigned grade {grade} to {student.name} for {course.name}")
        else:
            print("Error: Instructor not assigned to course or student not enrolled")
    
    def add_course(self,course):
        self.courses.append(course)