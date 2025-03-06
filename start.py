"""
This script automates the database setup and execution of the University Record Management System.
"""

import subprocess
import sys
import os

# Ensure the script runs from the project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

def setup_database():
    """Runs all setup steps for the database."""
    print("🛠️ Setting up the database...")

    # Step 1: Run models.py to create tables
    subprocess.run([sys.executable, os.path.join(SRC_DIR, "models.py")], check=True)

    # Step 2: Populate data from populate_data.sql
    subprocess.run([sys.executable, os.path.join(SRC_DIR, "populate_data.py")], check=True)

    print("✅ Setup complete! The database is ready.")

def run_application():
    """Start the application."""
    print("🚀 Launching University Record Management System...")
    subprocess.run([sys.executable, os.path.join(SRC_DIR, "ui.py")], check=True)

if __name__ == "__main__":
    setup_database()
    run_application()
