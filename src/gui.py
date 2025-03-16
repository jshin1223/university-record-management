# gui.py
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import sys
import os

# Importing queries from queries.py NB these both the queries created by Shin and the ones I proposed.
from queries import (
    # Original shin queries
    get_students_in_major,
    get_courses_by_department,
    get_students_in_course,
    get_top_students,
    get_all_departments,
    get_professors_in_department,
    get_courses_by_lecturer_in_department,
    get_staff_in_department,
    # NEW proposed queries
    get_students_in_course_by_lecturer,
    get_final_year_students_above_70,
    get_students_no_courses,
    get_advisor_contact_for_student,
    get_lecturers_by_research_area,
    get_lecturers_supervising_most_projects,
    get_recent_publications,
    get_students_advised_by
)

class UniversityGUI(tk.Tk):
    """
    A Tkinter-based GUI for the University Record Management System.
    This version includes buttons for all the queries in queries.py.
    """
    def __init__(self):
        super().__init__()
        self.title("University Record Management System")
        self.geometry("1100x600")  # A bit bigger to accommodate more buttons

        # Set up main frames: a side frame for the menu, a main frame for results
        self.menu_frame = tk.Frame(self, bg="lightgray")
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.content_frame = tk.Frame(self)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Title label at the top of content frame
        title_label = tk.Label(self.content_frame, text="University Record Management System", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Result area: use a Treeview for tabular data
        self.tree = ttk.Treeview(self.content_frame, columns=["Column1", "Column2", "Column3"], show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # We'll dynamically set headings when we display results
        for i in range(1, 4):
            self.tree.heading(f"Column{i}", text=f"Column {i}")

        # --- Original Buttons ---
        btn1 = tk.Button(self.menu_frame, text="Students in Major", command=self.show_students_in_major)
        btn2 = tk.Button(self.menu_frame, text="Courses by Dept", command=self.show_courses_by_dept)
        btn3 = tk.Button(self.menu_frame, text="Students in Course", command=self.show_students_in_course)
        btn4 = tk.Button(self.menu_frame, text="Top Students >70%", command=self.show_top_students)
        btn5 = tk.Button(self.menu_frame, text="All Departments", command=self.show_all_departments)
        btn6 = tk.Button(self.menu_frame, text="Professors in Dept", command=self.show_professors_in_dept)
        btn7 = tk.Button(self.menu_frame, text="Courses by Lecturers", command=self.show_courses_by_lecturer_dept)
        btn8 = tk.Button(self.menu_frame, text="Staff in Dept", command=self.show_staff_in_dept)

        # --- NEW Buttons for Additional Queries ---
        # 1) Students in Course Taught by a Particular Lecturer
        btn_new1 = tk.Button(self.menu_frame, text="Students in Course & Lecturer", command=self.show_students_course_lecturer)

        # 2) Final-Year Students >70%
        btn_new2 = tk.Button(self.menu_frame, text="Final-Year >70%", command=self.show_final_year_students_above_70)

        # 3) Students with No Courses
        btn_new3 = tk.Button(self.menu_frame, text="Students w/ No Courses", command=self.show_students_no_courses)

        # 4) Advisor's Contact
        btn_new4 = tk.Button(self.menu_frame, text="Advisor Contact", command=self.show_advisor_contact)

        # 5) Lecturers by Research Area
        btn_new5 = tk.Button(self.menu_frame, text="Lecturers by Research", command=self.show_lecturers_by_research_area)

        # 6) Lecturers Who Supervised Most Projects
        btn_new6 = tk.Button(self.menu_frame, text="Top Supervisors", command=self.show_top_supervisors)

        # 7) Recent Publications by Year
        btn_new7 = tk.Button(self.menu_frame, text="Publications by Year", command=self.show_recent_publications)

        # 8) Students Advised by Lecturer
        btn_new8 = tk.Button(self.menu_frame, text="Students Advised by...", command=self.show_students_advised_by)

        # Exit button
        btn_exit = tk.Button(self.menu_frame, text="Exit", command=self.exit_app, bg="red", fg="white")

        # Pack the buttons in the menu frame
        for widget in [
            btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8,
            btn_new1, btn_new2, btn_new3, btn_new4, btn_new5, btn_new6, btn_new7, btn_new8,
            btn_exit
        ]:
            widget.pack(padx=10, pady=5, fill=tk.X)

    def clear_tree(self):
        """Clears any existing data in the tree."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Reset column headings
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

    def display_data_in_tree(self, data, col_labels=None):
        """
        Display a list of tuples in the tree.
        data: list of tuples or single values
        col_labels: optional list of column headings
        """
        self.clear_tree()

        if not data:
            messagebox.showinfo("No Results", "No data found.")
            return

        # Determine the max number of columns based on the data
        max_cols = max(len(row) for row in data)
        # Reconfigure tree columns dynamically
        columns = [f"Column{i}" for i in range(1, max_cols + 1)]
        self.tree["columns"] = columns

        # Set headings based on provided col_labels or fallback
        if col_labels and len(col_labels) == max_cols:
            for i, col_name in enumerate(col_labels, start=1):
                self.tree.heading(f"Column{i}", text=col_name)
        else:
            for i in range(max_cols):
                self.tree.heading(f"Column{i+1}", text=f"Column {i+1}")

        # Insert rows
        for row in data:
            # Ensure row is a tuple, or wrap single item
            if not isinstance(row, (tuple, list)):
                row = (row,)
            self.tree.insert("", tk.END, values=row)

    # --- Original Query Handlers (unchanged) ---
    def show_students_in_major(self):
        major = simpledialog.askstring("Students in Major", "Enter major name:")
        if major:
            data = get_students_in_major(major)
            self.display_data_in_tree(data, col_labels=["Student Name"])

    def show_courses_by_dept(self):
        dept = simpledialog.askstring("Courses by Dept", "Enter department name:")
        if dept:
            data = get_courses_by_department(dept)
            self.display_data_in_tree(data, col_labels=["Course Name"])

    def show_students_in_course(self):
        course_name = simpledialog.askstring("Students in Course", "Enter course name:")
        if course_name:
            data = get_students_in_course(course_name)
            self.display_data_in_tree(data, col_labels=["Student Name"])

    def show_top_students(self):
        data = get_top_students()  # e.g. [("John Doe", 85.5), ("Emily Johnson", 91.2)]
        self.display_data_in_tree(data, col_labels=["Student Name", "Current Grades"])

    def show_all_departments(self):
        data = get_all_departments()
        self.display_data_in_tree(data, col_labels=["Department"])

    def show_professors_in_dept(self):
        dept = simpledialog.askstring("Professors in Dept", "Enter department name:")
        if dept:
            data = get_professors_in_department(dept)
            self.display_data_in_tree(data, col_labels=["Lecturer Name"])

    def show_courses_by_lecturer_dept(self):
        dept = simpledialog.askstring("Courses by Lecturers", "Enter department name:")
        if dept:
            data = get_courses_by_lecturer_in_department(dept)
            # e.g. [("Algorithms", "Dr. Smith"), ("Cybersecurity", "Dr. Kevin")]
            self.display_data_in_tree(data, col_labels=["Course Name", "Lecturer Name"])

    def show_staff_in_dept(self):
        dept = simpledialog.askstring("Staff in Dept", "Enter department name:")
        if dept:
            data = get_staff_in_department(dept)
            self.display_data_in_tree(data, col_labels=["Staff Name", "Job Title"])

    # --- NEW Query Handlers (corresponding to newly added queries) ---

    def show_students_course_lecturer(self):
        """
        Finds all students in a given course taught by a particular lecturer.
        Corresponds to get_students_in_course_by_lecturer in queries.py.
        """
        course = simpledialog.askstring("Course Name", "Enter the course name:")
        lecturer = simpledialog.askstring("Lecturer Name", "Enter the lecturer's name:")
        if course and lecturer:
            data = get_students_in_course_by_lecturer(course, lecturer)
            self.display_data_in_tree(data, col_labels=["Student Name"])

    def show_final_year_students_above_70(self):
        """
        Lists final-year students who have an average grade above 70%.
        Calls get_final_year_students_above_70 from queries.py.
        """
        data = get_final_year_students_above_70()
        # e.g. each row might be (Name, CurrentGrade, YearOfStudy)
        self.display_data_in_tree(data, col_labels=["Name", "Grade", "Year"])

    def show_students_no_courses(self):
        """
        Identifies students who haven't registered for any courses.
        Calls get_students_no_courses from queries.py.
        """
        data = get_students_no_courses()
        self.display_data_in_tree(data, col_labels=["Student Name"])

    def show_advisor_contact(self):
        """
        Retrieves the advisor's contact info for a given student.
        Calls get_advisor_contact_for_student from queries.py.
        """
        student_input = simpledialog.askstring("Student Name", "Enter student's name:")
        if student_input:
            data = get_advisor_contact_for_student(student_input)
            # data might come back as (advisor_name, email, phone)
            self.display_data_in_tree(data, col_labels=["Advisor Name", "Email", "Phone"])

    def show_lecturers_by_research_area(self):
        """
        Searches lecturers by a given research keyword.
        Calls get_lecturers_by_research_area from queries.py.
        """
        keyword = simpledialog.askstring("Research Keyword", "Enter a keyword (e.g., AI):")
        if keyword:
            data = get_lecturers_by_research_area(keyword)
            # e.g. each row might be (lecturer_id, name, expertise)
            self.display_data_in_tree(data, col_labels=["Lecturer ID", "Lecturer Name", "Expertise"])

    def show_top_supervisors(self):
        """
        Identifies lecturers who supervised the most research projects.
        Calls get_lecturers_supervising_most_projects.
        """
        # We could optionally ask how many top supervisors to show, e.g. 5 or 10
        limit = simpledialog.askinteger("Number of Supervisors", "How many top supervisors?", initialvalue=5)
        if limit:
            data = get_lecturers_supervising_most_projects(limit)
            # e.g. each row might be (lecturer_name, project_count)
            self.display_data_in_tree(data, col_labels=["Lecturer", "Project Count"])

    def show_recent_publications(self):
        """
        Generates a report on publications in a given year.
        Calls get_recent_publications from queries.py.
        """
        year_str = simpledialog.askstring("Publication Year", "Enter year (e.g., 2023):")
        if year_str:
            data = get_recent_publications(year_str)
            # e.g. each row might be (lecturer_name, publications)
            self.display_data_in_tree(data, col_labels=["Lecturer Name", "Publications"])

    def show_students_advised_by(self):
        """
        Retrieves names of students advised by a specific lecturer.
        Calls get_students_advised_by from queries.py.
        """
        lecturer_name = simpledialog.askstring("Lecturer Name", "Enter lecturer's name:")
        if lecturer_name:
            data = get_students_advised_by(lecturer_name)
            # e.g. each row is (student_name,)
            self.display_data_in_tree(data, col_labels=["Student Name"])

    def exit_app(self):
        """Exit the application."""
        self.destroy()

def main():
    app = UniversityGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
