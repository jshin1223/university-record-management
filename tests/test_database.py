"""
test_database.py

This module contains unit tests for testing database connectivity and queries.
"""

import unittest
from database import get_db_connection

class TestDatabase(unittest.TestCase):
    """Test cases for database connectivity and queries."""

    def setUp(self):
        """Set up the database connection before each test."""
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    def tearDown(self):
        """Close the database connection after each test."""
        self.cursor.close()
        self.conn.close()

    def test_database_connection(self):
        """Test if the database connection is established successfully."""
        self.assertIsNotNone(self.conn, "Database connection failed!")

    def test_students_table_exists(self):
        """Check if the students table exists in the database."""
        self.cursor.execute("SHOW TABLES LIKE 'students';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Table 'students' does not exist!")

    def test_courses_table_exists(self):
        """Check if the courses table exists in the database."""
        self.cursor.execute("SHOW TABLES LIKE 'courses';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Table 'courses' does not exist!")

    def test_lecturers_table_exists(self):
        """Check if the lecturers table exists in the database."""
        self.cursor.execute("SHOW TABLES LIKE 'lecturers';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Table 'lecturers' does not exist!")

    def test_enrollments_table_exists(self):
        """Check if the enrollments table exists in the database."""
        self.cursor.execute("SHOW TABLES LIKE 'enrollments';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Table 'enrollments' does not exist!")

    def test_insert_student(self):
        """Test inserting a new student into the database."""
        self.cursor.execute("INSERT INTO students (student_id, name, program, year_of_study, current_grades) VALUES (999, 'Test Student', 'Computer Science', 1, 85.5);")
        self.conn.commit()
        self.cursor.execute("SELECT * FROM students WHERE student_id = 999;")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Failed to insert student into the database!")

    def test_query_students(self):
        """Test querying all students in the database."""
        self.cursor.execute("SELECT COUNT(*) FROM students;")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Query for students returned no result!")

if __name__ == '__main__':
    unittest.main()
