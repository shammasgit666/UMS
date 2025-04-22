class Course:
    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.students = []
    
    def add_student(self,student):
        self.students.append(student)

    def remove_student(self,student):
        if student.id in [student.id for student in self.students]:
            self.students = [s for s in self.students if s.id != student.id]
        else:
            print(f"Student {student.id} not found in course {self.code}.")

    def __repr__(self):
        return f"Course(name='{self.name}', code='{self.code}', students={[student.id for student in self.students]})"