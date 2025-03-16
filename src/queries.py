from database import get_db_connection

def get_students_in_major(major_name):
    """
    This will retrieve all students enrolled in the same major (program).
    Corresponds to an example query: 
      - 'List students by major.'
    """
    query = """
    SELECT name 
    FROM students 
    WHERE program = %s;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, (major_name,))
        result = cursor.fetchall()
    conn.close()
    return result

def get_professors_in_department(department_name):
    """
    Retrieve all lecturers/professors in a given department.
    Example query:
      - 'List all professors in a department.'
    """
    query = """
    SELECT name 
    FROM lecturers 
    WHERE department = %s;
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
    Satisfies suggested query:
      - 'Find all students enrolled in a specific course taught by a particular lecturer.'
      (We only handle "specific course" here. If you want to filter by lecturer too,
       see get_students_in_course_by_lecturer().)
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

def get_students_in_course_by_lecturer(course_name, lecturer_name):
    """
    Find all students enrolled in a specific course that is taught by a particular lecturer.
    Satisfies the *exact* assignment query:
      - 'Find all students enrolled in a specific course taught by a particular lecturer.'
    """
    query = """
    SELECT s.name
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN courses c ON e.course_id = c.course_code
    JOIN lecturer_courses lc ON lc.course_id = c.course_code
    JOIN lecturers l ON lc.lecturer_id = l.lecturer_id
    WHERE c.name = %s
      AND l.name = %s;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, (course_name, lecturer_name))
        result = cursor.fetchall()
    conn.close()
    return result

def get_final_year_students_above_70():
    """
    List all students with an average grade above 70% who are in their 'final year' of studies.
    The 'final year' logic depends on your data. If you store a 'year_of_study' 
    and a separate 'programs.duration', you can join them. For example:
    
    SELECT s.name, s.current_grades
    FROM students s
    JOIN programs p ON s.program = p.name
    WHERE s.current_grades > 70
      AND s.year_of_study = p.duration;

    If your schema doesn't tie year_of_study to program duration, you can 
    do something simpler, like "year_of_study = 4" (assuming 4th year is final).
    Adjust the query to match your real data.
    """
    query = """
    SELECT s.name, s.current_grades, s.year_of_study
    FROM students s
    JOIN programs p ON s.program = p.name
    WHERE s.current_grades > 70
      AND s.year_of_study = p.duration;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    conn.close()
    return result

def get_students_no_courses():
    """
    Identify students who haven't registered for ANY courses in the current semester.
    If your 'enrollments' table doesn't store a semester, you might just find students with 
    no enrollments at all. For example:
    
    SELECT s.name
    FROM students s
    WHERE s.student_id NOT IN (
        SELECT e.student_id FROM enrollments e
    );

    If you do track 'semester' in enrollments, filter by 'WHERE e.semester = 'Spring2025'', etc.
    """
    query = """
    SELECT s.name
    FROM students s
    WHERE s.student_id NOT IN (
        SELECT e.student_id FROM enrollments e
    );
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    conn.close()
    return result

def get_advisor_contact_for_student(student_id_or_name):
    """
    Retrieve the contact information for the faculty advisor of a specific student.
    This assumes 'lecturers' table has columns like 'email' or 'phone' for contact info.
    If not, adapt accordingly.
    
    We'll match by student's name or ID. We'll assume 'students' has a unique name or
    you might do 'WHERE s.student_id = %s' if the user passes an ID.
    """
    query = """
    SELECT l.name AS advisor_name,
           l.email AS advisor_email,
           l.phone AS advisor_phone
    FROM lecturers l
    JOIN students s ON s.advisor_id = l.lecturer_id
    WHERE s.name = %s
    LIMIT 1;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, (student_id_or_name,))
        result = cursor.fetchall()
    conn.close()
    return result

def get_lecturers_by_research_area(keyword):
    """
    Search for lecturers with expertise in a particular research area.
    e.g. 'keyword' = 'machine learning'
    We'll do a case-insensitive search with LIKE.
    """
    query = """
    SELECT lecturer_id, name, expertise 
    FROM lecturers
    WHERE LOWER(expertise) LIKE LOWER(%s);
    """
    pattern = f"%{keyword}%"
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, (pattern,))
        result = cursor.fetchall()
    conn.close()
    return result

def get_lecturers_supervising_most_projects(limit=5):
    """
    Identify lecturers who have supervised the most student research projects.
    This assumes 'research_projects' table has 'principal_investigator' referencing 
    the lecturer who supervises it. We'll group and order by the count of projects.
    """
    query = """
    SELECT l.name AS lecturer_name,
           COUNT(r.project_title) AS project_count
    FROM lecturers l
    JOIN research_projects r ON r.principal_investigator = l.lecturer_id
    GROUP BY l.lecturer_id
    ORDER BY project_count DESC
    LIMIT %s;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, (limit,))
        result = cursor.fetchall()
    conn.close()
    return result

def get_recent_publications(year_str):
    """
    Generate a report on the publications of lecturers in the *past year*.
    
    If your 'lecturers' table includes a 'publications' column that references
    a text or string like 'AI Journal 2023', we can do something naive like:
      WHERE publications LIKE '%2023%'
    or we can parse it differently. We'll let the user pass the year: '2023' or '2024'.
    
    If your data has multiple lines, you might need a more robust approach.
    """
    pattern = f"%{year_str}%"
    query = """
    SELECT name, publications 
    FROM lecturers
    WHERE publications LIKE %s;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, (pattern,))
        result = cursor.fetchall()
    conn.close()
    return result

def get_students_advised_by(lecturer_name):
    """
    Retrieve the names of students advised by a specific lecturer.
    This uses 'advisor_id' in students referencing 'lecturers.lecturer_id'.
    """
    query = """
    SELECT s.name
    FROM students s
    JOIN lecturers l ON s.advisor_id = l.lecturer_id
    WHERE l.name = %s;
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, (lecturer_name,))
        result = cursor.fetchall()
    conn.close()
    return result

def get_staff_in_department(department_name):
    """
    Find all staff members employed in a specific department.
    We already had this, which matches one assignment suggestion:
      - 'Find all staff members employed in a specific department.'
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
    """
    Retrieve a list of all departments. 
    Already existed—useful for populating a combo box or just listing them.
    """
    query = "SELECT department_name FROM departments;"
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    conn.close()
    # Return a flat list
    return [row[0] for row in result]

def get_courses_by_department(department_name):
    """
    Retrieve all courses for a specific department.
    """
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

def get_courses_by_lecturer_in_department(department_name):
    """
    List all courses taught by lecturers in a specific department.
    Already existed for your assignment.
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
    This function corresponds to a query in gui.py.
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
