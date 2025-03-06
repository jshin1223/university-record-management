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

## Project Description
The **University Record Management System** is a Python-based command-line application designed to manage university records, including:

- **Student Records**
- **Lecturer Records**
- **Course Records**
- **Department Records**
- **Research Projects**
- **Non-Academic Staff**

The system enables users to retrieve university records through a user-friendly menu-based interface.

## Installation
### Prerequisites
Ensure you have the following installed on your system:
1. **Python 3.8 or higher** – Download and install from the [official Python website](https://www.python.org/downloads/).
2. **MySQL Server** – Install from the [official MySQL website](https://dev.mysql.com/downloads/installer/).
3. **MySQL Workbench** – Optional but recommended for executing SQL scripts and managing the database.

### Installing Dependencies
Once Python is installed, install the required dependencies using:
```sh
pip install -r requirements.txt
```

## Execution and Usage
### Clone the Repository
```sh
git clone <repository_url>
cd <repository_directory>
```

### Set Up and Run the Application
To set up the database and launch the system, run:
```sh
python start.py
```
This command:
1. **Creates the database schema**.
2. **Populates the database with data**.
3. **Launches the application**.

### Menu Options
When the application starts, you will see the following menu:
```
************************************
  🎓 University Record Management System
************************************
1. 🔍 Find students in a course
2. 📚 List courses taught by lecturers in a department
3. 🏆 List students with an average grade above 70%
4. 👨‍🏫 Find staff members in a department
5. 🚪 Exit
************************************
Enter your choice:
```
Choose an option by entering the corresponding number.

## Running Unit Tests
To run all unit tests, execute:
```sh
python test.py
```
This will run all tests in the `tests/` directory.

## Executing SQL File in MySQL Workbench
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

## Technologies Used
The project was built using:
- **Python 3.8 or higher**
- **MySQL** (Relational Database Management System)
- **PyMySQL** (Python MySQL connector)
- **SQLAlchemy** (ORM for database models)

## Current Features
The University Record Management System supports:
- **Student Records:** Retrieve student details and enrollment information.
- **Lecturer Records:** View lecturer details and assigned courses.
- **Course Records:** List courses offered by departments.
- **Enrollment Management:** Ensure students are only enrolled in courses within their department.
- **Department Records:** Retrieve details about university departments.
- **Research Projects:** View research projects supervised by lecturers.
- **Non-Academic Staff Management:** Retrieve non-academic staff details.

## Contributors
- **Matthew Stevenson**
- **Hugo Janse van Renburg**
- **Auwal Muhammad Musa**
- **Sung Shin**

## License
This project is licensed under the MIT License.

**Copyright (c) 2025 Matthew Stevenson, Hugo Janse van Renburg, Auwal Muhammad Musa, Sung Shin**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.