import sys
from queries import (
    get_students_in_major,
    get_courses_by_department,
    get_professors_in_department,
    get_students_in_course,
    get_courses_by_lecturer_in_department,
    get_top_students,
    get_staff_in_department,
    get_all_departments,
)
from collections import defaultdict

def display_menu():
    """Displays the main menu."""
    print("\n" + "*" * 45)
    print("  🎓 University Record Management System")
    print("*" * 45)
    print("1. 🏫  List all students in a major")
    print("2. 📜  List all courses by department")
    print("3. 🔎  Find students in a course")
    print("4. 🥇  List students with an average grade above 70%")
    print("5. 🏛️  List all departments")
    print("6. 🧑‍🏫  List all professors in a department")
    print("7. 📖  List courses taught by lecturers in a department")
    print("8. 🏢  Find staff members in a department")
    print("9. 🚪  Exit")
    print("*" * 45)

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
            print_results(f"Professors in {department_name.upper()}", professors)

        elif choice == "7":
            department_name = input("\n🔹 Enter department name: ").strip()
            courses = get_courses_by_lecturer_in_department(department_name)
            print_results_grouped(f"Courses in {department_name.upper()}", courses)

        elif choice == "8":
            department_name = input("\n🔹 Enter department name: ").strip()
            staff = get_staff_in_department(department_name)
            print_results(f"Staff in {department_name.upper()}", staff)

        elif choice == "9":
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

def print_results_grouped (title, data):
    """Formats and displays query results grouped by lecturer."""
    print("\n" + "*" * 40)
    print(f"📌 {title}:")
    print("*" * 40)

    if data:
        lecturer_courses = defaultdict(list)

        # Group courses under each lecturer
        for course, lecturer in data:
            lecturer_courses[lecturer].append(course)

        # Print lecturer and their courses
        for lecturer, courses in lecturer_courses.items():
            print(f"\n👨‍🏫 Lecturer: {lecturer}")
            for course in courses:
                print(f"   - {course}")
    else:
        print("❌ No results found.")

    print("\n" + "*" * 40)

if __name__ == "__main__":
    main()