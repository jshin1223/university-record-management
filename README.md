# 🎓 University Record Management System

## 📚 Table of Contents
- [Project Description](#project-description)
- [Installation & Execution](#installation--execution)
- [Technologies Used](#technologies-used)
- [Current Features](#current-features)
- [Contributors](#contributors)
- [License](#license)

---

## 📌 Project Description
The **University Record Management System** is a Python-based command-line application designed to manage university records, including:

- **Student Records**
- **Lecturer Records**
- **Course Records**
- **Department Records**
- **Research Projects**
- **Non-Academic Staff**

The system enables users to retrieve university records through a user-friendly menu-based interface.

---

## ⚙️ Installation & Execution

### 📝 **Prerequisites**
Ensure you have the following installed:
1. **Python 3.8 or higher** – Download from the [official Python website](https://www.python.org/downloads/).
2. **MySQL Server** – Install from the [official MySQL website](https://dev.mysql.com/downloads/installer/).

---

### 🚀 **One-Step Installation & Execution**
The setup script **automates** everything:  
💚 Installs dependencies  
💚 Creates the database and tables  
💚 Populates the database with data  
💚 Launches the application  

#### **Step 1: Clone the Repository**
```sh
git clone <repository_url>
cd <repository_directory>
```

#### **Step 2: Run the Setup Script**
```sh
python setup.py
```

That's it! 🎉 The system will start running automatically.

---

### 🎮 **How to Use the Application**
After running `python setup.py`, the following menu will appear:

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
Simply enter the corresponding number to retrieve the desired information.

---

## 🛠️ Technologies Used
The project was built using:
- **Python 3.8+**
- **MySQL** (Relational Database Management System)
- **PyMySQL** (Python MySQL Connector)
- **SQLAlchemy** (ORM for database models)

---

## 🌟 Current Features
👉 **Student Records:** Retrieve student details and enrollment information  
👉 **Lecturer Records:** View lecturer details and assigned courses  
👉 **Course Records:** List courses offered by departments  
👉 **Enrollment Management:** Ensure students are only enrolled in courses within their department  
👉 **Department Records:** Retrieve details about university departments  
👉 **Research Projects:** View research projects supervised by lecturers  
👉 **Non-Academic Staff Management:** Retrieve non-academic staff details  

---

## 👥 Contributors
- **Matthew Stevenson**
- **Hugo Janse van Renburg**
- **Auwal Muhammad Musa**
- **Sung Shin**

---

## 📚 License
This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025
Matthew Stevenson, Hugo Janse van Renburg, Auwal Muhammad Musa, Sung Shin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

