# 🎓 University Record Management System

## 🌍 Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Execution and Usage](#execution-and-usage)
- [Running Unit Tests](#running-unit-tests)
- [Executing SQL File in MySQL Workbench](#executing-sql-file-in-mysql-workbench)
- [Technologies Used](#technologies-used)
- [Current Features](#current-features)
- [Contributors](#contributors)
- [License](#license)

<a id="project-description"></a>
## 📚 Project Description
The **University Record Management System** is a Python-based application designed to manage university records, including:

- **Student Records**
- **Lecturer Records**
- **Course Records**
- **Department Records**
- **Research Projects**
- **Non-Academic Staff**

The system enables users to retrieve university records through a user-friendly **Command-Line Interface (CLI)** or an interactive **Graphical User Interface (GUI)**.

<a id="installation"></a>
## ⚙️ Installation
### Prerequisites
Ensure you have the following installed on your system:
1. **Python 3.8 or higher** – Download and install from the [official Python website](https://www.python.org/downloads/).
2. **MySQL Server** – Install from the [official MySQL website](https://dev.mysql.com/downloads/installer/).
3. **MySQL Workbench** – Optional but recommended for executing SQL scripts and managing the database.

### 📌 Steps to Install

1. **Clone the Repository**
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Run the Installation Script**
   ```sh
   python install.py
   ```
   This will install all required dependencies.

<a id="execution-and-usage"></a>
## 🚀 Execution and Usage

### Set Up and Run the Application
To set up the database and launch the system, run:
```sh
python start.py
```
This command:
1. **Creates the database schema**.
2. **Populates the database with data**.
3. **Prompts the user to select CLI or GUI mode**.
4. **Launches the application**.

### Choose CLI or GUI Mode
When running `start.py`, you will see:
```
==================================================
🎓  WELCOME TO THE UNIVERSITY RECORD MANAGEMENT SYSTEM
==================================================

🔹 Select how you want to run the program:
[1]  Command Line Interface (CLI)
[2]  Graphical User Interface (GUI)
[0]  Exit

👉 Enter your choice (1, 2, or 0 to exit): 
```
- **Enter `1`** to run in **Command Line Interface (CLI)**.
- **Enter `2`** to run in **Graphical User Interface (GUI)**.
- **Enter `0`** to exit.

---

### **📜 Menu Options (CLI Mode)**
When running in **CLI Mode**, the menu displays:
```
************************************
  🎓 University Record Management System
************************************
1. 🏫  List all students in a major
2. 📜  List all courses by department
3. 🔎  Find students in a course
4. 🥇  List students with an average grade above 70%
5. 🏛️  List all departments
6. 🧑‍🏫  List all professors in a department
7. 📖  List courses taught by lecturers in a department
8. 🏢  Find staff members in a department
9. 🏆  List all research projects in a department
10. 🎓  List all Bachelor's degree programs
11. 🎓  List all Master's degree programs
12. 🚪  Exit
************************************
Enter your choice:
```
Choose an option by entering the corresponding number.

---

### **🖥️ GUI Mode**
If **GUI mode** is selected, a **graphical interface** appears with:
- **Sidebar Menu** for selecting queries.
- **Beautifully formatted results** with larger fonts.
- **Scrollable results** for better visibility.
- **Interactive pop-ups** with larger fonts for prompts.

<a id="running-unit-tests"></a>
## 🧪 Running Unit Tests
To run all unit tests, execute:
```sh
python test.py
```
This will run all tests in the `tests/` directory.

<a id="executing-sql-file-in-mysql-workbench"></a>
## 💾 Executing SQL File in MySQL Workbench
To insert initial data into MySQL, follow these steps:
1. Open **MySQL Workbench** and connect to your MySQL Server.
2. Select the database `university_db` (or create it if it does not exist).
3. Click **File > Open SQL Script** and select `data/populate_data.sql`.
4. Click **Execute** to run the script.
5. Verify the data using:
   ```sql
   SELECT * FROM students;
   SELECT * FROM courses;
   ```

<a id="technologies-used"></a>
## 🛠 Technologies Used
The project was built using:
- **Python 3.8 or higher**
- **MySQL** (Relational Database Management System)
- **PyMySQL** (Python MySQL connector)
- **SQLAlchemy** (ORM for database models)
- **Tkinter** (for GUI development)

<a id="current-features"></a>
## 🎯 Current Features
The University Record Management System supports:
- **Student Records:** Retrieve student details and enrollment information.
- **Lecturer Records:** View lecturer details and assigned courses.
- **Course Records:** List courses offered by departments.
- **Enrollment Management:** Ensure students are only enrolled in courses within their department.
- **Department Records:** Retrieve details about university departments.
- **Research Projects:** View research projects supervised by lecturers.
- **Non-Academic Staff Management:** Retrieve non-academic staff details.
- **Graphical User Interface (GUI):** Run the system with an interactive GUI.

<a id="contributors"></a>
## 👥 Contributors
- **Matthew Stevenson**
- **Hugo Janse van Renburg**
- **Auwal Muhammad Musa**
- **Sung Shin**

<a id="license"></a>
## 📜 License
This project is licensed under the MIT License.

**Copyright (c) 2025 Matthew Stevenson, Hugo Janse van Renburg, Auwal Muhammad Musa, Sung Shin**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
