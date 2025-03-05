from database import get_db_connection

def get_students_in_course(course_name):
    """Find all students enrolled in a specific course."""
    query = """
    SELECT s.name
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN courses c ON e.course_id = c.course_code
    WHERE c.name = %s;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, (course_name,))
        result = cursor.fetchall()
    conn.close()
    return result

def get_courses_by_department(department_name):
    """List all courses taught by lecturers in a specific department."""
    query = """
    SELECT c.name, l.name AS lecturer
    FROM courses c
    JOIN lecturer_courses lc ON c.course_code = lc.course_id
    JOIN lecturers l ON lc.lecturer_id = l.lecturer_id
    WHERE c.department = %s;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, (department_name,))
        result = cursor.fetchall()
    conn.close()
    return result

def get_top_students():
    """List all students with an average grade above 70%."""
    query = """
    SELECT name, current_grades
    FROM students
    WHERE current_grades > 70;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    conn.close()
    return result

def get_staff_by_department(department_name):
    """Find all staff members employed in a specific department."""
    query = """
    SELECT name, job_title
    FROM non_academic_staff
    WHERE department = %s;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, (department_name,))
        result = cursor.fetchall()
    conn.close()
    return result

