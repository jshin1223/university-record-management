import sys
from queries import (
    get_students_in_major,
    get_courses_by_department,
    get_professors_in_department,
    get_students_in_course,
    get_courses_taught_by_lecturers,
    get_top_students,
    get_staff_in_department,
    get_all_departments,
    get_research_projects_by_department,
    get_bachelors_degrees, 
    get_masters_degrees
)
from collections import defaultdict

def display_menu():
    """Displays the main menu."""
    print("\n" + "*" * 50)
    print("  🎓 University Record Management System")
    print("*" * 50)
    print("1. 🏫  List all students in a major")
    print("2. 📜  List all courses by department")
    print("3. 🔎  Find students in a course")
    print("4. 🥇  List students with an average grade above 70%")
    print("5. 🏛️  List all departments")
    print("6. 🧑‍🏫  List all professors in a department")
    print("7. 📖  List courses taught by lecturers in a department")
    print("8. 🏢  Find staff members in a department")
    print("9. 🏆  List all research projects in a department")
    print("10. 🎓  List all Bachelor's Degrees")
    print("11. 🎓  List all Master's Degrees")
    print("12. 🚪  Exit")
    print("*" * 50)

def main():
    """Main function to handle user input and execute queries."""
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            major_name = input("\n🔹 Enter major name: ").strip()
            students = get_students_in_major(major_name)
            print_results(f"Students enrolled in {major_name}", students)

        elif choice == "2":
            department_name = input("\n🔹 Enter department name: ").strip()
            courses = get_courses_by_department(department_name)
            print_results(f"Courses in {department_name.upper()}", courses)

        elif choice == "3":
            course_name = input("\n🔹 Enter course name: ").strip()
            students = get_students_in_course(course_name)
            print_results(f"Students enrolled in {course_name}", students)

        elif choice == "4":
            students = get_top_students()
            print_results("Students with an average grade above 70%", students)

        elif choice == "5":
            departments = get_all_departments()
            print_results("List of Departments", departments)

        elif choice == "6":
            department_name = input("\n🔹 Enter department name: ").strip()
            professors = get_professors_in_department(department_name)
            print_lecturer_results(f"Professors in {department_name.upper()}", professors)

        elif choice == "7":
            department_name = input("\n🔹 Enter department name: ").strip()
            courses = get_courses_taught_by_lecturers(department_name)
            print_lecturer_results(f"Courses in {department_name.upper()}", courses)

        elif choice == "8":
            department_name = input("\n🔹 Enter department name: ").strip()
            staff = get_staff_in_department(department_name)
            print_results(f"Staff in {department_name.upper()}", staff)

        elif choice == "9":  # ✅ NEW FUNCTION FOR RESEARCH PROJECTS
            department_name = input("\n🔹 Enter department name: ").strip()
            projects = get_research_projects_by_department(department_name)
            print_research_results(f"Research Projects in {department_name.upper()}", projects)

        elif choice == "10":
            bachelors_degrees = get_bachelors_degrees()
            print_degree_results("Bachelor's Degree Programs", bachelors_degrees)

        elif choice == "11":
            masters_degrees = get_masters_degrees()
            print_degree_results("Master's Degree Programs", masters_degrees)

        elif choice == "10":
            print("\n🚪 Exiting... Goodbye! 👋\n")
            sys.exit(0)

        else:
            print("\n❌ Invalid choice! Please select a valid option.")

        # Prompt user if they want to continue or exit
        while True:
            continue_choice = input("\n🔄 Would you like to perform another operation? (y/n): ").strip().lower()
            if continue_choice == "y":
                break  # Show menu again
            elif continue_choice == "n":
                print("\n🚪 Exiting... Goodbye! 👋\n")
                sys.exit(0)
            else:
                print("❌ Invalid input! Please enter 'y' to continue or 'n' to exit.")

def print_results(title, data):
    """Formats and displays query results with structured output."""
    print("\n" + "*" * 40)
    print(f"📌 {title}:")
    print("*" * 40)

    if data:
        for item in data:
            if isinstance(item, tuple):
                if all(isinstance(x, str) and len(x) == 1 for x in item):  
                    # If the tuple contains single-character elements (fix for department names)
                    print(f"✔️ {''.join(item)}")  
                elif len(item) == 2:  
                    # If the tuple contains two values (Name and Detail)
                    name, detail = item
                    print(f"✔️ {name}: {detail}")  
                else:
                    print(f"✔️ {' '.join(map(str, item))}")  
            else:
                print(f"✔️ {item}")  # If item is a single string
    else:
        print("❌ No results found.")

    print("*" * 40)

def print_research_results(title, data):
    """Formats and displays query results with structured output."""
    print("\n" + "*" * 50)
    print(f"📌 {title}:")
    print("*" * 50)

    if data:
        for item in data:
            if isinstance(item, tuple) and len(item) == 5:  # Research projects format
                project_title, principal_investigator, funding_sources, team_members, publications = item
                print(f"✔️ Project Title: {project_title}")
                print(f"   Principal Investigator: {principal_investigator}")
                print(f"   Funding Sources: {funding_sources}")
                print(f"   Team Members: {team_members}")  # Prof. + Students correctly formatted
                print(f"   Publications: {publications}\n")
            else:
                print(f"✔️ {' '.join(map(str, item))}")  # Default handling for other queries
        
    else:
        print("❌ No results found.")

    print("*" * 50)

def print_lecturer_results(title, data):
    """Formats and displays query results with structured output."""
    print("\n" + "*" * 50)
    print(f"📌 {title}:")
    print("*" * 50)

    if data:
        for item in data:
            if isinstance(item, tuple) and len(item) == 3:  # Professors List
                professor_name, qualifications, expertise = item
                print(f"✔️ {professor_name}")
                print(f"   Academic Qualifications: {qualifications}")
                print(f"   Expertise: {expertise}\n")

            elif isinstance(item, tuple) and len(item) == 2:  # Courses Taught by Lecturers
                lecturer_name, courses = item
                print(f"👨‍🏫 {lecturer_name}")
                print(f"   Courses: {courses}\n")

            else:
                print(f"✔️ {' '.join(map(str, item))}")  # Default handling for other queries
        
    else:
        print("❌ No results found.")

    print("*" * 50)

def print_degree_results(title, data):
    """Formats and displays query results with structured output."""
    print("\n" + "*" * 50)
    print(f"📌 {title}:")
    print("*" * 50)

    if data:
        for item in data:
            if isinstance(item, tuple) and len(item) == 5:
                name, degree, duration, requirements, enrolment = item
                print(f"✔️ Major: {degree}, {name}")
                print(f"   Duration: {duration} ({enrolment})")
                print(f"   Course Requirements: {requirements}")
                print()
            else:
                print(f"✔️ {' '.join(map(str, item))}")  
    else:
        print("❌ No results found.")

    print("*" * 50)

if __name__ == "__main__":
    main()