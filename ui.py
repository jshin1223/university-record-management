import queries

def main():
    """
    University Record Management System Command Line Interface (CLI).
    Provides users with a menu to query university records.
    """
    while True:
        print("\n************************************")
        print("  🎓 University Record Management System")
        print("************************************")
        print("1. 🔍 Find students in a course")
        print("2. 📚 List courses taught by lecturers in a department")
        print("3. 🏆 List students with an average grade above 70%")
        print("4. 👨‍🏫 Find staff members in a department")
        print("5. 🚪 Exit")
        print("************************************")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            course_name = input("\n🔹 Enter course name: ")
            students = queries.get_students_in_course(course_name)
            print("\n****************************************")
            print(f"📌 Students enrolled in {course_name.upper()}:")
            print("****************************************")
            if students:
                for student in students:
                    print(f"✔ {student[0]}")
            else:
                print("❌ No students found for this course.")
            print("****************************************")

        elif choice == "2":
            department_name = input("\n🔹 Enter department name: ")
            courses = queries.get_courses_by_department(department_name)
            print("\n****************************************")
            print(f"📌 Courses in {department_name.upper()}:")
            print("****************************************")
            if courses:
                for course, lecturer in courses:
                    print(f"📖 {course} - 👨‍🏫 Lecturer: {lecturer}")
            else:
                print("❌ No courses found for this department.")
            print("****************************************")

        elif choice == "3":
            students = queries.get_top_students()
            print("\n****************************************")
            print("📌 Students with an average grade above 70%:")
            print("****************************************")
            if students:
                for student, grade in students:
                    print(f"🎓 {student} - {grade}%")
            else:
                print("❌ No students found with grades above 70%.")
            print("****************************************")

        elif choice == "4":
            department_name = input("\n🔹 Enter department name: ")
            staff = queries.get_staff_by_department(department_name)
            print("\n****************************************")
            print(f"📌 Staff members in {department_name.upper()}:")
            print("****************************************")
            if staff:
                for name, job in staff:
                    print(f"👔 {name} - {job}")
            else:
                print("❌ No staff found for this department.")
            print("****************************************")

        elif choice == "5":
            print("\n🚪 Exiting program. Goodbye! 👋")
            break

        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
