import unittest

from project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.my_student = Student("Silvia")
        self.my_student_with_course = Student("Silvia", {"OOP": [6.00]})

    def test_initialize_student(self):
        self.assertEqual("Silvia", self.my_student.name)
        self.assertEqual({}, self.my_student.courses)
        self.assertEqual({"OOP": [6.00]}, self.my_student_with_course.courses)

    def test_enroll_with_already_existing_course_update_notes(self):
        result = self.my_student_with_course.enroll("OOP", [6.00])

        self.assertEqual([6.00, 6.00], self.my_student_with_course.courses["OOP"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_new_course_with_notes(self):
        result = self.my_student.enroll("OOP", [6.00])

        self.assertEqual([6.00], self.my_student.courses["OOP"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(1, len(self.my_student.courses))

    def test_enroll_new_course_with_notes_with_param_Y(self):
        result2 = self.my_student.enroll("Advanced", [6.00, 5.90], "Y")

        self.assertEqual([6.00, 5.90], self.my_student.courses["Advanced"])
        self.assertEqual("Course and course notes have been added.", result2)
        self.assertEqual(1, len(self.my_student.courses))

    def test_enroll_new_course_with_no_notes(self):
        result = self.my_student.enroll("OOP", [6.00], "no")

        self.assertEqual([], self.my_student.courses["OOP"])
        self.assertEqual("Course has been added.", result)
        self.assertEqual(1, len(self.my_student.courses))

    def test_add_notes_to_already_existing_course(self):
        result = self.my_student_with_course.add_notes("OOP", 5.80)

        self.assertIn(5.80, self.my_student_with_course.courses["OOP"])
        self.assertEqual([6.00, 5.80], self.my_student_with_course.courses["OOP"])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_non_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.my_student.add_notes("OOP", 5.80)

        self.assertNotIn("OOP", self.my_student.courses)
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        result = self.my_student_with_course.leave_course("OOP")

        self.assertEqual({}, self.my_student_with_course.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_non_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.my_student_with_course.leave_course("Advanced")

        self.assertEqual({"OOP": [6.00]}, self.my_student_with_course.courses)
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()
