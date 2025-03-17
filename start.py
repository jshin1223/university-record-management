"""
This script automates the database setup and execution of the University Record Management System.
It also allows the user to choose between running the application in CLI or GUI mode.
"""

import subprocess
import sys
import pymysql
from sqlalchemy import create_engine, inspect
from src.config import DB_CONFIG
import os

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
    required_tables = [
        "students", "lecturers", "courses", "departments", 
        "research_projects", "non_academic_staff", "enrollments", "lecturer_courses"
    ]

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

def choose_interface():
    """Prompt user to choose between CLI or GUI before running the application."""

    # **Check if CLI or GUI script exists before running**
    cli_path = "src/ui.py"
    gui_path = "src/gui.py"

    print("\n" + "=" * 50)
    print("🎓  WELCOME TO THE UNIVERSITY RECORD MANAGEMENT SYSTEM")
    print("=" * 50 + "\n")

    while True:
        print("\033[1;34m🔹 Select how you want to run the program:\033[0m")  # Blue Header
        print("\033[1;33m[1]\033[0m  Command Line Interface (CLI)")  # Bold Yellow
        print("\033[1;33m[2]\033[0m  Graphical User Interface (GUI)")  # Bold Yellow
        print("\033[1;33m[0]\033[0m  Exit\n")  # Bold Yellow

        choice = input("\033[1;34m👉 Enter your choice (1, 2, or 0 to exit): \033[0m").strip()

        if choice == "1":
            if not os.path.exists(cli_path):
                print("\n❌ ERROR: CLI script (ui.py) is missing! Please ensure it exists in the 'src/' folder.")
                continue
            print("\n✅ Running in Command Line Interface mode...\n")
            subprocess.run([sys.executable, cli_path], check=True)  # Runs CLI version
            break
        elif choice == "2":
            if not os.path.exists(gui_path):
                print("\n❌ ERROR: GUI script (gui.py) is missing! Please ensure it exists in the 'src/' folder.")
                continue
            print("\n✅ Launching Graphical User Interface mode...\n")
            subprocess.run([sys.executable, gui_path], check=True)  # Runs GUI version
            break
        elif choice == "0":
            print("\n👋 Exiting the program. Goodbye!")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please enter \033[1;33m1\033[0m for CLI, \033[1;33m2\033[0m for GUI, or \033[1;33m0\033[0m to exit.\n")

if __name__ == "__main__":
    setup_database()
    choose_interface()
