from database import get_db_connection

def get_students_in_major(major_name):
    """Retrieve all students enrolled in the same major."""
    query = """
    SELECT name FROM students WHERE program = %s;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, (major_name,))
        result = cursor.fetchall()
    conn.close()
    return result

def get_professors_in_department(department_name):
    """Retrieve all professors in the same department."""
    query = """
    SELECT name FROM lecturers WHERE department = %s;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, (department_name,))
        result = cursor.fetchall()
    conn.close()
    return result

def get_students_in_course(course_name):
    """
    Retrieve all students enrolled in a specific course.
    
    Args:
        course_name (str): Name of the course.
    
    Returns:
        list: A list of student names enrolled in the course.
    """
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

def get_courses_by_lecturer_in_department(department_name):
    """
    List all courses taught by lecturers in a specific department.
    
    Args:
        department_name (str): The department name.
    
    Returns:
        list: A list of tuples (course_name, lecturer_name).
    """
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
    """
    List all students with an average grade above 70%.
    
    Returns:
        list: A list of tuples (student_name, current_grades).
    """
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

def get_staff_in_department(department_name):
    """
    Find all staff members employed in a specific department.
    
    Args:
        department_name (str): The department name.
    
    Returns:
        list: A list of tuples (staff_name, job_title).
    """
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

def get_all_departments():
    """Retrieve a list of all departments."""
    query = "SELECT department_name FROM departments;"
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    conn.close()
    
    # Ensure department names are returned in correct format
    return [row[0] for row in result]  # This removes spaces between characters

def get_courses_by_department(department_name):
    """Retrieve all courses for a specific department."""
    query = """
    SELECT name
    FROM courses
    WHERE department = %s;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, (department_name,))
        result = cursor.fetchall()
    conn.close()
    return result

