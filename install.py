"""
This script installs the necessary dependencies for the University Record Management System.
"""

import subprocess
import sys
import os

# Ensure the script runs from the project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

def install_dependencies():
    """Installs required Python dependencies from requirements.txt."""
    print("📦 Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    print("✅ Dependencies installed successfully!")

if __name__ == "__main__":
    install_dependencies()
