import sys
from queries import (
    get_students_in_course,
    get_courses_by_department,
    get_top_students,
    get_staff_by_department,
)

def display_menu():
    """Displays the main menu."""
    print("\n" + "*" * 36)
    print("  🎓 University Record Management System")
    print("*" * 36)
    print("1. 🔍 Find students in a course")
    print("2. 📚 List courses taught by lecturers in a department")
    print("3. 🏆 List students with an average grade above 70%")
    print("4. 👨‍🏫 Find staff members in a department")
    print("5. 🚪 Exit")
    print("*" * 36)

def main():
    """Main function to handle user input and execute queries."""
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            course_name = input("\n🔹 Enter course name: ").strip()
            students = get_students_in_course(course_name)
            print_results(f"Students enrolled in {course_name}", students)
        
        elif choice == "2":
            department_name = input("\n🔹 Enter department name: ").strip()
            courses = get_courses_by_department(department_name)
            print_results(f"Courses in {department_name.upper()}", courses)
        
        elif choice == "3":
            students = get_top_students()
            print_results("Students with an average grade above 70%", students)
        
        elif choice == "4":
            department_name = input("\n🔹 Enter department name: ").strip()
            staff = get_staff_by_department(department_name)
            print_results(f"Staff in {department_name.upper()}", staff)
        
        elif choice == "5":
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
    """Formats and displays query results."""
    print("\n" + "*" * 40)
    print(f"📌 {title}:")
    print("*" * 40)
    if data:
        for item in data:
            print("✔️", item)
    else:
        print("❌ No results found.")
    print("*" * 40)

if __name__ == "__main__":
    main()