import unittest
import sys
import os

# Add src/ to the Python path dynamically
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from queries import (
    get_students_in_major,
    get_professors_in_department,
    get_students_in_course,
    get_courses_taught_by_lecturers,
    get_top_students,
    get_staff_in_department,
    get_all_departments,
    get_courses_by_department,
    get_research_projects_by_department,
    get_bachelors_degrees,
    get_masters_degrees
)
from database import get_db_connection

class TestDatabaseQueries(unittest.TestCase):
    """Unit tests for database query functions in queries.py."""

    def setUp(self):
        """Set up database connection before each test."""
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()
    
    def tearDown(self):
        """Close database connection after each test."""
        self.cursor.close()
        self.conn.close()

    def test_get_students_in_major(self):
        result = get_students_in_major("Computer Science")
        self.assertIsInstance(result, (list, tuple))

    def test_get_professors_in_department(self):
        result = get_professors_in_department("Engineering")
        self.assertIsInstance(result, (list, tuple))

    def test_get_students_in_course(self):
        result = get_students_in_course("Introduction to AI")
        self.assertIsInstance(result, (list, tuple))

    def test_get_courses_taught_by_lecturers(self):
        result = get_courses_taught_by_lecturers("Computer Science")
        self.assertIsInstance(result, (list, tuple))

    def test_get_top_students(self):
        result = get_top_students()
        self.assertIsInstance(result, (list, tuple))

    def test_get_staff_in_department(self):
        result = get_staff_in_department("Administration")
        self.assertIsInstance(result, (list, tuple))

    def test_get_all_departments(self):
        result = get_all_departments()
        self.assertIsInstance(result, (list, tuple))

    def test_get_courses_by_department(self):
        result = get_courses_by_department("Mathematics")
        self.assertIsInstance(result, (list, tuple))

    def test_get_research_projects_by_department(self):
        result = get_research_projects_by_department("Physics")
        self.assertIsInstance(result, (list, tuple))

    def test_get_bachelors_degrees(self):
        result = get_bachelors_degrees()
        self.assertIsInstance(result, (list, tuple))

    def test_get_masters_degrees(self):
        result = get_masters_degrees()
        self.assertIsInstance(result, (list, tuple))

    # New Advanced Tests
    def test_insert_student(self):
        """Test inserting a new student."""
        self.cursor.execute("""
            INSERT INTO students (name, dob, contact_info, program, year_of_study, current_grades, graduation_status)
            VALUES ('Test Student', '2000-01-01', 'test@student.com', 'Computer Science', 2, 75.0, 'In Progress');
        """)
        self.conn.commit()
        self.cursor.execute("SELECT name FROM students WHERE name = 'Test Student'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    def test_update_student_grade(self):
        """Test updating a student's grade."""
        self.cursor.execute("""
            INSERT INTO students (name, dob, contact_info, program, year_of_study, current_grades, graduation_status)
            VALUES ('Test Student', '2000-01-01', 'test@student.com', 'Computer Science', 2, 75.0, 'In Progress')
            ON DUPLICATE KEY UPDATE current_grades = 75.0;
        """)
        self.conn.commit()
        
        self.cursor.execute("UPDATE students SET current_grades = 90.0 WHERE name = 'Test Student'")
        self.conn.commit()
        self.cursor.execute("SELECT current_grades FROM students WHERE name = 'Test Student'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 90.0)

    def test_delete_student(self):
        """Test deleting a student."""
        self.cursor.execute("DELETE FROM students WHERE name = 'Test Student'")
        self.conn.commit()
        self.cursor.execute("SELECT name FROM students WHERE name = 'Test Student'")
        result = self.cursor.fetchone()
        self.assertIsNone(result)

    def test_invalid_course_lookup(self):
        """Test querying a non-existent course."""
        result = get_students_in_course("Non-Existent Course")
        self.assertIn(result, ([], ()))  # Accepts both empty list and empty tuple

if __name__ == "__main__":
    unittest.main()
