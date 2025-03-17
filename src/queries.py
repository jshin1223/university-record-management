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
    """Retrieve all professors in a specific department with 'Dr.' prefix."""
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT CONCAT('Dr. ', name) AS professor_name, academic_qualifications, expertise
    FROM lecturers
    WHERE department = %s;
    """
    
    cursor.execute(query, (department_name,))
    results = cursor.fetchall()
    
    conn.close()
    return results

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

def get_courses_taught_by_lecturers(department_name):
    """Retrieve courses taught by lecturers in a department with 'Dr.' prefix."""
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT CONCAT('Dr. ', l.name) AS lecturer_name, GROUP_CONCAT(c.name SEPARATOR ', ') AS courses
    FROM lecturers l
    JOIN lecturer_courses lc ON l.lecturer_id = lc.lecturer_id
    JOIN courses c ON lc.course_id = c.course_code
    WHERE l.department = %s
    GROUP BY l.lecturer_id, l.name;
    """
    
    cursor.execute(query, (department_name,))
    results = cursor.fetchall()
    
    conn.close()
    return results

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
    query = "SELECT TRIM(department_name) FROM departments;"  # ✅ Ensure full names are retrieved
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    conn.close()
    
    return [row[0] for row in result]  # ✅ Ensures proper formatting


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

def get_research_projects_by_department(department_name):
    """Retrieve all research projects in a specific department with properly formatted names."""
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT rp.project_title, 
           CONCAT('Dr. ', l.name) AS principal_investigator, 
           rp.funding_sources, 
           CONCAT('Dr. ', l.name, ' & Students: ', s1.name, ', ', s2.name) AS team_members, 
           rp.publications
    FROM research_projects rp
    JOIN lecturers l ON rp.principal_investigator = l.lecturer_id
    LEFT JOIN students s1 ON SUBSTRING_INDEX(SUBSTRING_INDEX(rp.team_members, ', ', -2), ', ', 1) = CONCAT('Student ', s1.student_id)
    LEFT JOIN students s2 ON SUBSTRING_INDEX(rp.team_members, ', ', -1) = CONCAT('Student ', s2.student_id)
    WHERE l.department = %s;
    """
    
    cursor.execute(query, (department_name,))
    results = cursor.fetchall()
    
    conn.close()
    return results

def get_bachelors_degrees():
    """Retrieve all bachelor's degree programmes (BSc, BEng, BBA, BA)."""
    query = """
    SELECT name, degree_awarded, duration, course_requirements, enrolment_details
    FROM programs
    WHERE degree_awarded IN ('BSc', 'BEng', 'BBA', 'BA');
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    conn.close()
    return result

def get_masters_degrees():
    """Retrieve all master's degree programmes (MSc)."""
    query = """
    SELECT name, degree_awarded, duration, course_requirements, enrolment_details
    FROM programs
    WHERE degree_awarded = 'MSc';
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    conn.close()
    return result