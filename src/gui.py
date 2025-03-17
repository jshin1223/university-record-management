import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

# Importing queries from queries.py
from queries import (
    get_students_in_major,
    get_courses_by_department,
    get_students_in_course,
    get_top_students,
    get_all_departments,
    get_professors_in_department,
    get_courses_taught_by_lecturers,
    get_staff_in_department,
    get_research_projects_by_department,
    get_bachelors_degrees,
    get_masters_degrees
)


class CustomDialog(simpledialog.Dialog):
    """Custom Dialog with Larger Font & Styling"""
    def __init__(self, parent, title, prompt_text):
        self.prompt_text = prompt_text
        super().__init__(parent, title)

    def body(self, master):
        """Customize the pop-up layout."""
        self.configure(bg="#E8E8E8")  # Light grey background
        tk.Label(master, text=self.prompt_text, font=("Helvetica", 14, "bold"), bg="#E8E8E8").pack(pady=10)
        self.entry = tk.Entry(master, font=("Helvetica", 14), width=30)
        self.entry.pack(pady=5)
        return self.entry  # Focus on the entry field automatically

    def apply(self):
        """Return user input."""
        self.result = self.entry.get()


class UniversityGUI(tk.Tk):
    """A Tkinter-based GUI for the University Record Management System."""

    def __init__(self):
        super().__init__()
        self.title("University Record Management System")
        self.geometry("1100x600")
        self.configure(bg="#F5F5F5")  # Light gray background

        # Set up main frames: menu & content
        self.menu_frame = tk.Frame(self, bg="#004080", width=300)  # Dark blue sidebar
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.content_frame = tk.Frame(self, bg="white")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Title label
        title_label = tk.Label(
            self.content_frame, text="University Record Management System",
            font=("Helvetica", 18, "bold"), fg="#004080", bg="white"
        )
        title_label.pack(pady=10)

        # 🌟 Custom Styling for Bigger Fonts
        style = ttk.Style()
        style.configure("Treeview", font=("Helvetica", 14))  # ✅ Bigger text inside results
        style.configure("Treeview.Heading", font=("Helvetica", 16, "bold"))  # ✅ Bigger headers
        style.configure("Treeview", rowheight=30)  # ✅ Increase row height for better spacing

        # **Scrollable Result Area**
        self.tree_frame = tk.Frame(self.content_frame)
        self.tree_frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.tree_frame, show="headings")

        # ✅ Add a Scrollbar to the Treeview
        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Always visible on the right

        # ✅ Ensure buttons are created
        self.create_buttons()

    def create_buttons(self):
        """Create and place all buttons in the sidebar menu."""
        button_data = [
            ("🏫 Students in Major", self.show_students_in_major),
            ("📜 Courses by Dept", self.show_courses_by_dept),
            ("🔎 Find Students in Course", self.show_students_in_course),
            ("🥇 Top Students >70%", self.show_top_students),
            ("🏛️ All Departments", self.show_all_departments),
            ("🧑‍🏫 Professors in Dept", self.show_professors_in_dept),
            ("📖 Courses by Lecturers", self.show_courses_by_lecturer_dept),
            ("🏢 Staff in Dept", self.show_staff_in_dept),
            ("🏆 Research Projects", self.show_research_projects),
            ("🎓 Bachelor's Degrees", self.show_bachelors_degrees),
            ("🎓 Master's Degrees", self.show_masters_degrees),
            ("🚪 Exit", self.exit_app)
        ]

        for text, command in button_data:
            btn = tk.Button(
                self.menu_frame,
                text=text,
                command=command,  # ✅ Ensure the correct method is being called
                font=("Helvetica", 12, "bold"),
                bg="#3498db",  # Blue color
                fg="white",
                padx=10, pady=5
            )
            btn.pack(pady=5, fill=tk.X)

    def clear_tree(self):
        """Clears the tree view before inserting new data."""
        for item in self.tree.get_children():
            self.tree.delete(item)

    def display_data(self, data, col_labels):
        """Displays data in the tree view with descriptive column names."""
        self.clear_tree()

        if not data:
            messagebox.showinfo("No Results", "No data found.")
            return

        # Set column headers dynamically
        self.tree["columns"] = [f"Col{i}" for i in range(1, len(col_labels) + 1)]
        for i, label in enumerate(col_labels, start=1):
            self.tree.heading(f"Col{i}", text=label)
            self.tree.column(f"Col{i}", anchor="center", stretch=True)

        # Insert data rows
        for row in data:
            self.tree.insert("", tk.END, values=row)

    # ----- Query Handlers -----
    def get_input(self, title, prompt):
        """Use a **custom pop-up with larger fonts** for input."""
        dialog = CustomDialog(self, title, prompt)
        return dialog.result

    def show_students_in_major(self):
        major = self.get_input("Major", "Enter major name:")
        if major:
            data = get_students_in_major(major)
            self.display_data(data, col_labels=["Student Name"])

    def show_courses_by_dept(self):
        dept = self.get_input("Department", "Enter department name:")
        if dept:
            data = get_courses_by_department(dept)
            self.display_data(data, col_labels=["Course Name"])

    def show_students_in_course(self):
        course = self.get_input("Course", "Enter course name:")
        if course:
            data = get_students_in_course(course)
            self.display_data(data, col_labels=["Student Name"])

    def show_top_students(self):
        data = get_top_students()
        self.display_data(data, col_labels=["Student Name", "Grade (%)"])

    def show_all_departments(self):
        """Fetch and display all department names properly."""
        data = get_all_departments()
        formatted_data = [(dept,) for dept in data] if data else []
        self.display_data(formatted_data, col_labels=["Department Name"])

    def show_professors_in_dept(self):
        dept = self.get_input("Department", "Enter department name:")
        if dept:
            data = get_professors_in_department(dept)
            self.display_data(data, col_labels=["Professor Name", "Qualification", "Expertise"])

    def show_courses_by_lecturer_dept(self):
        dept = self.get_input("Department", "Enter department name:")
        if dept:
            data = get_courses_taught_by_lecturers(dept)
            self.display_data(data, col_labels=["Lecturer", "Courses"])

    def show_staff_in_dept(self):
        dept = self.get_input("Department", "Enter department name:")
        if dept:
            data = get_staff_in_department(dept)
            self.display_data(data, col_labels=["Staff Name", "Job Title"])

    def show_research_projects(self):
        dept = self.get_input("Department", "Enter department name:")
        if dept:
            data = get_research_projects_by_department(dept)
            self.display_data(data, col_labels=["Project Title", "Principal Investigator", "Funding", "Team Members", "Publications"])

    def show_bachelors_degrees(self):
        data = get_bachelors_degrees()
        self.display_data(data, col_labels=["Program Name", "Degree", "Duration", "Course Requirements", "Enrollment Details"])

    def show_masters_degrees(self):
        data = get_masters_degrees()
        self.display_data(data, col_labels=["Program Name", "Degree", "Duration", "Course Requirements", "Enrollment Details"])

    def exit_app(self):
        """Exit the application."""
        self.destroy()


# Run the application
if __name__ == "__main__":
    app = UniversityGUI()
    app.mainloop()
