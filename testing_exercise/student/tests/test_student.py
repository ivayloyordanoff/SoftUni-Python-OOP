import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("First student")
        self.student_with_course = Student("Second student", {"math": ["some note"]})

    def test_correct_initialization(self):
        self.assertEqual(self.student.name, "First student")
        self.assertEqual(self.student.courses, {})
        self.assertEqual(self.student_with_course.courses, {"math": ["some note"]})

    def test_enroll_existing_course(self):
        result = self.student_with_course.enroll("math", ["second note"])
        self.assertEqual(self.student_with_course.courses["math"][1], "second note")
        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_enroll_non_existing_course_without_third_param(self):
        result = self.student.enroll("math", ["math notes"])
        self.assertEqual(self.student.courses["math"][0], "math notes")
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_non_existing_course_with_third_param(self):
        result = self.student.enroll("math", ["math notes"], "Y")
        self.assertEqual(self.student.courses["math"][0], "math notes")
        self.assertEqual(result, "Course and course notes have been added.")

    def test_add_new_course_without_adding_the_notes(self):
        result = self.student.enroll("math", ["math notes"], "N")
        self.assertEqual(len(self.student.courses["math"]), 0)
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_on_existing_course(self):
        result = self.student_with_course.add_notes("math", "new note")
        self.assertEqual(self.student_with_course.courses["math"][-1], "new note")
        self.assertEqual(result, "Notes have been updated")

    def test_add_notes_to_non_existing_course(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes("math", "some note")
        self.assertEqual(str(context.exception), "Cannot add notes. Course not found.")

    def test_leave_existing_course(self):
        result = self.student_with_course.leave_course("math")
        self.assertEqual(self.student_with_course.courses, {})
        self.assertEqual(result, "Course has been removed")

    def test_leave_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course("math")
        self.assertEqual(str(context.exception), "Cannot remove course. Course not found.")


if __name__ == "__main__":
    unittest.main()
