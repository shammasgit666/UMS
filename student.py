from person import Person

class Student(Person):
    def __init__(self,name,id):
        super().__init__(name,id)
        self.GPA = 0.0
        self.enrolled_courses = {}
    
    def enroll(self,course):
        if course.code not in self.enrolled_courses:
            self.enrolled_courses[course.code] = None
            course.add_student(self)
            print(f"{self.name} enrolled in {course.name}")
        else:
            print(f"{self.name} is already enrolled in {course.name}")

    def view_grades(self):
        return self.enrolled_courses
    
    def update_GPA(self,GPA):
        self.GPA = GPA

    def __repr__(self):
        return f"Student(name='{self.name}', id='{self.id}', enrolled_courses={self.enrolled_courses})"