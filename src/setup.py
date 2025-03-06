"""
setup.py

This script automates the installation, database setup, and execution of the University Record Management System.
"""

import subprocess
import sys

def setup_database():
    """Runs all setup steps for the database."""
    print("🛠️ Setting up the database...")

    # Step 1: Run models.py to create tables
    subprocess.run([sys.executable, "src/models.py"], check=True)

    # Step 2: Populate data from populate_data.sql
    subprocess.run([sys.executable, "src/populate_data.py"], check=True)

    print("✅ Setup complete! The database is ready.")

def run_application():
    """Start the application."""
    print("🚀 Launching University Record Management System...")
    subprocess.run([sys.executable, "src/ui.py"], check=True)

if __name__ == "__main__":
    setup_database()
    run_application()
