import unittest
from student import Student
from instructor import Instructor
from course import Course
class TestUniversitySystem(unittest.TestCase):
    def setUp(self):
        self.student = Student("Alice", 1)
        self.instructor = Instructor("Dr. Smith", 101)
        self.course = Course("Python Programming", "CS101")
        self.instructor.add_course(self.course)
    def test_enrollment(self):
        self.student.enroll(self.course)
        self.assertIn("CS101", self.student.enrolled_courses)
    def test_grade_assignment(self):
        self.student.enroll(self.course)
        self.instructor.assign_grade(self.student, self.course, "A")
        self.assertEqual(self.student.enrolled_courses["CS101"], "A")
if __name__ == "__main__":
    unittest.main()