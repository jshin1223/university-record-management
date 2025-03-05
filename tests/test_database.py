"""
test_database.py

This module contains basic unit tests to verify database connectivity and table existence.
"""

import unittest
import sys
import os

# Add src/ to the Python path dynamically
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from database import get_db_connection  # Import the database connection function

class TestDatabaseConnection(unittest.TestCase):
    """Test cases for verifying database connection and tables."""

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

    def test_tables_exist(self):
        """Check if the key tables exist in the database."""
        tables = ["students", "courses", "lecturers", "enrollments", "departments"]
        for table in tables:
            with self.subTest(table=table):
                self.cursor.execute(f"SHOW TABLES LIKE '{table}';")
                result = self.cursor.fetchone()
                self.assertIsNotNone(result, f"Table '{table}' does not exist!")

if __name__ == '__main__':
    unittest.main()
