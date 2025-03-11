"""
This script automates the database setup and execution of the University Record Management System.
"""

import subprocess
import sys
import pymysql
from sqlalchemy import create_engine, inspect
from src.config import DB_CONFIG

# Database connection credentials
DB_HOST = DB_CONFIG['host']
DB_USER = DB_CONFIG['user']
DB_PASSWORD = DB_CONFIG['password']
DB_NAME = DB_CONFIG['database']
DB_PORT = DB_CONFIG['port']

def database_exists():
    """Check if the MySQL database exists before running setup."""
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)
        cursor = conn.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{DB_NAME}'")
        database_found = cursor.fetchone()
        conn.close()
        return bool(database_found)
    except pymysql.MySQLError as e:
        print(f"⚠️ Database connection error: {e}")
        return False

def tables_exist():
    """Check if required tables exist in the database."""
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(DATABASE_URL)
    inspector = inspect(engine)
    required_tables = ["students", "lecturers", "courses", "departments", "research_projects", "non_academic_staff", "enrollments", "lecturer_courses"]

    existing_tables = inspector.get_table_names()
    return all(table in existing_tables for table in required_tables)

def setup_database():
    """Ensures database setup and resets data every time."""
    if not database_exists():
        print("🛠️ Database not found. Creating database and tables...")
        subprocess.run([sys.executable, "src/models.py"], check=True)
        print("✅ Database setup complete!")

    if not tables_exist():
        print("🛠️ Tables missing. Creating tables...")
        subprocess.run([sys.executable, "src/models.py"], check=True)
        print("✅ Tables setup complete!")

    print("🔄 Resetting database data...")
    subprocess.run([sys.executable, "src/populate_data.py"], check=True)
    print("✅ Database reset and repopulated successfully!")

def run_application():
    """Start the application."""
    print("🚀 Launching University Record Management System...")
    subprocess.run([sys.executable, "src/ui.py"], check=True)

if __name__ == "__main__":
    setup_database()
    run_application()
