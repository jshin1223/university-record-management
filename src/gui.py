# gui.py
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import sys
import os

# If gui.py and queries.py are in the same folder, you can do a direct import like this:
from queries import (
    get_students_in_major,
    get_courses_by_department,
    get_students_in_course,
    get_top_students,
    get_all_departments,
    get_professors_in_department,
    get_courses_by_lecturer_in_department,
    get_staff_in_department
)

class UniversityGUI(tk.Tk):
    """
    A Tkinter-based GUI for the University Record Management System.
    """
    def __init__(self):
        super().__init__()
        self.title("University Record Management System")
        self.geometry("920x480")  # Adjust window size as needed

        # Set up main frames: a side frame for the menu, a main frame for results
        self.menu_frame = tk.Frame(self, bg="lightgray")
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.content_frame = tk.Frame(self)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Title label at the top of content frame
        title_label = tk.Label(self.content_frame, text="University Records", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Result area: use a Treeview for tabular data
        self.tree = ttk.Treeview(self.content_frame, columns=["Column1", "Column2", "Column3"], show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # We'll dynamically set headings when we display results
        for i in range(1, 4):
            self.tree.heading(f"Column{i}", text=f"Column {i}")

        # Add buttons for each of the queries on the left menu
        btn1 = tk.Button(self.menu_frame, text="Students in Major", command=self.show_students_in_major)
        btn2 = tk.Button(self.menu_frame, text="Courses by Dept", command=self.show_courses_by_dept)
        btn3 = tk.Button(self.menu_frame, text="Students in Course", command=self.show_students_in_course)
        btn4 = tk.Button(self.menu_frame, text="Top Students >70%", command=self.show_top_students)
        btn5 = tk.Button(self.menu_frame, text="All Departments", command=self.show_all_departments)
        btn6 = tk.Button(self.menu_frame, text="Professors in Dept", command=self.show_professors_in_dept)
        btn7 = tk.Button(self.menu_frame, text="Courses by Lecturers", command=self.show_courses_by_lecturer_dept)
        btn8 = tk.Button(self.menu_frame, text="Staff in Dept", command=self.show_staff_in_dept)
        btn_exit = tk.Button(self.menu_frame, text="Exit", command=self.exit_app, bg="red", fg="white")

        # Pack the buttons in the menu frame
        for widget in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn_exit]:
            widget.pack(padx=10, pady=5, fill=tk.X)

    def clear_tree(self):
        """Clears any existing data in the tree."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Reset column headings to initial state
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

        # Set headings based on provided col_labels or fallback to generic
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
        data = get_all_departments()  # e.g. [("Computer Science",), ("Mathematics",)]
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

    def exit_app(self):
        """Exit the application."""
        self.destroy()

def main():
    app = UniversityGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
