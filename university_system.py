import pickle
import json
import sqlite3
from student import Student
from instructor import Instructor
from course import Course

class UniversitySystem:

    conn = sqlite3.connect("university_data.db")
    cursor = conn.cursor()

    @classmethod
    def create_tables(cls):
        cls.cursor.execute("""CREATE TABLE IF NOT EXISTS students(
                       name TEXT NOT NULL,
                       id TEXT NOT NULL,
                       enrolled_courses TEXT)""")
        cls.cursor.execute("""CREATE TABLE IF NOT EXISTS instructors(
                       name TEXT NOT NULL,
                       id TEXT NOT NULL,
                       courses BLOB) """)
        cls.cursor.execute("""CREATE TABLE IF NOT EXISTS courses( 
                       name TEXT NOT NULL,
                       code TEXT UNIQUE NOT NULL,
                       students BLOB) """)
        cls.conn.commit() #Save changes
    
    @classmethod
    def add_student(cls,student):
        cls.cursor.execute("SELECT id FROM students WHERE id = ?", (student.id,))
        if cls.cursor.fetchone():
            print(f"Student with ID {student.id} already exists!")
            return
        enrolled_courses = json.dumps(student.enrolled_courses) if student.enrolled_courses else json.dumps({})
        cls.cursor.execute("INSERT INTO students(name,id,enrolled_courses) VALUES (?,?,?)",(student.name,student.id,enrolled_courses))
        print(f"Name: {student.name} ID: {student.id} Added")
        cls.conn.commit()
        print(f"Student {student.name} added")

    @classmethod
    def get_student(cls,id):
        cls.cursor.execute("SELECT * FROM students WHERE id = ?",(id,))
        info = cls.cursor.fetchone()
        if not info:
            print(f"No student found with ID: {id}")
            return None
        name = info[0]
        enrolled_courses = json.loads(info[2]) if info[2] else {}
        student = Student(name,info[1])
        student.enrolled_courses = enrolled_courses
        return student
    
    @classmethod
    def remove_student(cls,student):
        cls.cursor.execute("SELECT enrolled_courses FROM students WHERE id = ?", (student.id,))
        enrolled_courses = cls.cursor.fetchone()
        enrolled_courses = json.loads(enrolled_courses[0])
        enrolled_courses = [cls.get_course(a) for a in enrolled_courses.keys()]
        for course in enrolled_courses:
            course.remove_student(student)
            cls.update_course_students(course)
        cls.cursor.execute("DELETE FROM students WHERE id = ?",(student.id,))
        print(f"Student with ID: {student.id} removed")
        cls.conn.commit()

    @classmethod
    def update_enrolled_courses(cls,student):
        """add student object"""
        enrolled_courses = json.dumps(student.enrolled_courses)
        cls.cursor.execute("UPDATE students SET enrolled_courses = ? WHERE id = ?",(enrolled_courses,student.id))
    
    @classmethod
    def add_course(cls,course):
        cls.cursor.execute("SELECT code FROM courses WHERE code = ?", (course.code,))
        if cls.cursor.fetchone():
            print(f"Course with Code {course.code} already exists!")
            return
        students = pickle.dumps(course.students)
        cls.cursor.execute("INSERT INTO courses(name,code,students) VALUES (?,?,?)",(course.name,course.code,students))
        cls.conn.commit()
        print(f"Course {course.name} added")

    @classmethod
    def get_course(cls,code):
        cls.cursor.execute("SELECT name,code,students FROM courses WHERE code = ?",(code,))
        info = cls.cursor.fetchone()
        if not info:
            print(f"No course found with Code: {code}")
            return None
        name, code, students = info
        students = pickle.loads(students) if students else []
        course = Course(name, code)
        course.students = students
        return course
    
    @classmethod
    def remove_course(cls,course):
        cls.cursor.execute("DELETE FROM courses WHERE code = ?",(course.code,))
        print(f"Course with Code: {course.code} removed")
        cls.conn.commit()

    @classmethod
    def update_course_students(cls,course):
        """course object, updates the course.students in database"""
        students = pickle.dumps(course.students)
        cls.cursor.execute("UPDATE courses SET students = ? WHERE code = ?",(students,course.code))
        cls.conn.commit()

    @classmethod
    def add_instructor(cls,instructor):
        cls.cursor.execute("SELECT id FROM instructors WHERE id = ?", (instructor.id,))
        if cls.cursor.fetchone():
            print(f"instructor with ID {instructor.id} already exists!")
            return
        courses = pickle.dumps(instructor.courses) if instructor.courses else pickle.dumps([])
        cls.cursor.execute("INSERT INTO instructors(name,id,courses) VALUES (?,?,?)",(instructor.name,instructor.id,courses))
        print(f"Name: {instructor.name} ID: {instructor.id} Added")
        cls.conn.commit()
        print(f"instructor {instructor.name} added")

    @classmethod
    def get_instructor(cls,id):
        cls.cursor.execute("SELECT * FROM instructors WHERE id = ?",(id,))
        info = cls.cursor.fetchone()
        if not info:
            print(f"No instructor found with ID: {id}")
            return None
        name = info[0]
        courses = pickle.loads(info[2]) if info[2] else []
        instructor = instructor(name,info[1])
        instructor.courses = courses
        return instructor
    
    @classmethod
    def remove_instructor(cls,instructor):
        cls.cursor.execute("SELECT id FROM instructors WHERE id = ?",(instructor.id,))
        info = cls.cursor.fetchone()
        if not info:
            print(f"No instructor found with ID: {instructor.id}")
            return None
        cls.cursor.execute("DELETE FROM instructors WHERE id = ?",(instructor.id,))
        print(f"instructor with ID: {instructor.id} removed")
        cls.conn.commit()

    @classmethod
    def update_instructor_courses(cls,instructor):
        """add instructor object"""
        cls.cursor.execute("SELECT id FROM instructors WHERE id = ?",(instructor.id,))
        info = cls.cursor.fetchone()
        if not info:
            print(f"No instructor found with ID: {instructor.id}")
            return None
        courses = pickle.dumps(instructor.courses)
        cls.cursor.execute("UPDATE instructors SET courses = ? WHERE id = ?",(courses,instructor.id))
        cls.conn.commit()

    @classmethod
    def close_connection(cls):
        cls.conn.close()