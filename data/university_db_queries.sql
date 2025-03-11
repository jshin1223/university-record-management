SELECT * FROM enrollments;
SELECT * FROM lecturer_courses;
SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM lecturers;
SELECT * FROM departments;
SELECT * FROM programs;
SELECT * FROM research_projects;
SELECT * FROM non_academic_staff;

SELECT COUNT(*) FROM enrollments;
SELECT COUNT(*) FROM lecturer_courses;
SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM courses;
SELECT COUNT(*) FROM lecturers;
SELECT COUNT(*) FROM departments;
SELECT COUNT(*) FROM programs;
SELECT COUNT(*) FROM research_projects;
SELECT COUNT(*) FROM non_academic_staff;


SELECT student_id FROM students;
SELECT course_code FROM courses;
SELECT student_id FROM students ORDER BY student_id;

SHOW TABLES LIKE 'programs';
