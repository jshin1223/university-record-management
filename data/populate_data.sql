USE university_db;

-- 🚨 Disable foreign key checks before truncating tables to prevent constraint issues
SET FOREIGN_KEY_CHECKS = 0;

-- 🔄 Reset tables before inserting new data (clear old records)
TRUNCATE TABLE enrollments;
TRUNCATE TABLE lecturer_courses;
TRUNCATE TABLE students;
TRUNCATE TABLE courses;
TRUNCATE TABLE lecturers;
TRUNCATE TABLE departments;
TRUNCATE TABLE programs;
TRUNCATE TABLE research_projects;
TRUNCATE TABLE non_academic_staff;

-- ✅ Reset AUTO_INCREMENT counters for primary keys **AFTER** truncation
ALTER TABLE enrollments AUTO_INCREMENT = 1;
ALTER TABLE lecturer_courses AUTO_INCREMENT = 1;
ALTER TABLE students AUTO_INCREMENT = 1;
ALTER TABLE courses AUTO_INCREMENT = 1;
ALTER TABLE lecturers AUTO_INCREMENT = 1;
ALTER TABLE departments AUTO_INCREMENT = 1;
ALTER TABLE programs AUTO_INCREMENT = 1;
ALTER TABLE research_projects AUTO_INCREMENT = 1;
ALTER TABLE non_academic_staff AUTO_INCREMENT = 1;

-- ✅ Re-enable foreign key checks
SET FOREIGN_KEY_CHECKS = 1;

-- ✅ Insert new data as usual
-- (Continue with your INSERT statements for departments, lecturers, students, etc.)

-- Insert Departments
INSERT INTO departments (department_name, faculty, research_areas, courses_offered, staff_members) VALUES
('Computer Science', 'Engineering', 'AI, Data Science, Cybersecurity', 20, 50),
('Mathematics', 'Science', 'Statistics, Algebra, Geometry', 15, 40),
('Physics', 'Science', 'Quantum Mechanics, Astrophysics', 10, 35),
('Biology', 'Life Sciences', 'Genetics, Microbiology, Neuroscience', 12, 30),
('Chemistry', 'Science', 'Organic, Inorganic, Analytical Chemistry', 8, 25),
('Business', 'Management', 'Finance, Marketing, Strategy', 18, 45),
('Psychology', 'Social Sciences', 'Cognitive Science, Behavioral Analysis', 14, 28),
('Mechanical Engineering', 'Engineering', 'Robotics, Thermodynamics, Design', 16, 50),
('Electrical Engineering', 'Engineering', 'Circuits, Renewable Energy, Signal Processing', 22, 55),
('History', 'Humanities', 'Medieval Studies, Modern History', 10, 20);

-- Insert Lecturers
INSERT INTO lecturers (lecturer_id, name, department, academic_qualifications, expertise, course_load, research_interests, publications)
VALUES
-- 🖥️ Computer Science (5)
(1, 'Alice Johnson', 'Computer Science', 'PhD AI', 'Machine Learning', 3, 'Neural Networks, AI Ethics', 'AI Journal 2024'),
(2, 'Kevin Brown', 'Computer Science', 'PhD Cybersecurity', 'Ethical Hacking', 3, 'Cyber Threats and Protection', 'CyberSec Journal 2024'),
(3, 'Umar Khan', 'Computer Science', 'PhD Artificial Intelligence', 'Deep Learning', 3, 'AI Applications in Healthcare', 'Deep Learning Review 2024'),
(4, 'Ethan Morgan', 'Computer Science', 'PhD Software Engineering', 'Cloud Computing', 3, 'DevOps, Distributed Systems', 'Cloud Research 2023'),
(5, 'Sophia Davis', 'Computer Science', 'PhD Computational Theory', 'Algorithms', 3, 'Graph Theory, Cryptography', 'Theory Review 2023'),

-- 🧮 Mathematics (5)
(6, 'Bob Smith', 'Mathematics', 'PhD Statistics', 'Probability Theory', 2, 'Bayesian Models, Applied Math', 'Math Review 2023'),
(7, 'Lisa Adams', 'Mathematics', 'PhD Applied Mathematics', 'Mathematical Modelling', 2, 'Statistical Analysis', 'Applied Math Review 2023'),
(8, 'Victoria Evans', 'Mathematics', 'PhD Probability Theory', 'Stochastic Processes', 2, 'Risk Analysis', 'Probability Journal 2023'),
(9, 'Daniel Carter', 'Mathematics', 'PhD Algebra', 'Linear Algebra', 2, 'Abstract Algebra, Number Theory', 'Algebra Review 2024'),
(10, 'Emily Roberts', 'Mathematics', 'PhD Computational Mathematics', 'Numerical Methods', 2, 'Simulation Techniques', 'Computational Math 2023'),

-- 🔬 Physics (5)
(11, 'Chris Evans', 'Physics', 'PhD Quantum Mechanics', 'Quantum Computing', 3, 'Quantum Cryptography', 'Quantum Journal 2023'),
(12, 'Michael Johnson', 'Physics', 'PhD Astrophysics', 'Black Holes', 3, 'Exoplanet Research', 'AstroPhysics Journal 2024'),
(13, 'William Taylor', 'Physics', 'PhD Nuclear Physics', 'Fusion Energy', 3, 'Nuclear Fusion Technologies', 'Nuclear Science 2023'),
(14, 'Olivia Carter', 'Physics', 'PhD Thermodynamics', 'Statistical Mechanics', 3, 'Heat Transfer, Kinetics', 'Physics Review 2023'),
(15, 'Nathan Scott', 'Physics', 'PhD Optics', 'Lasers and Photonics', 3, 'Quantum Optics', 'Photonics Journal 2024'),

-- 🧬 Biology (5)
(16, 'Diana Ford', 'Biology', 'PhD Genetics', 'DNA Sequencing', 2, 'Genome Research', 'BioTech 2022'),
(17, 'Nancy Lee', 'Biology', 'PhD Microbiology', 'Bacterial Resistance', 2, 'Pathogen Study', 'Microbiology Journal 2023'),
(18, 'Xavier King', 'Biology', 'PhD Biotechnology', 'Genetic Engineering', 2, 'CRISPR Research', 'Biotech Journal 2024'),
(19, 'Rachel Adams', 'Biology', 'PhD Ecology', 'Environmental Science', 2, 'Climate Change', 'Ecology Journal 2024'),
(20, 'Thomas Green', 'Biology', 'PhD Neuroscience', 'Neurobiology', 2, 'Brain Function Studies', 'Neuroscience Journal 2023'),

-- 🧪 Chemistry (5)
(21, 'Edward Harris', 'Chemistry', 'PhD Chemistry', 'Organic Chemistry', 2, 'Molecular Synthesis', 'ChemSci 2024'),
(22, 'Olivia Wright', 'Chemistry', 'PhD Analytical Chemistry', 'Spectroscopy', 3, 'Chemical Sensors', 'Analytical Chem 2024'),
(23, 'Yvonne Carter', 'Chemistry', 'PhD Organic Synthesis', 'Catalysis', 3, 'Green Chemistry', 'Chemistry World 2023'),
(24, 'Samuel Lewis', 'Chemistry', 'PhD Inorganic Chemistry', 'Material Science', 3, 'Nanotechnology', 'Materials Journal 2023'),
(25, 'Hannah Wilson', 'Chemistry', 'PhD Biochemistry', 'Enzymology', 3, 'Metabolic Pathways', 'BioChem Review 2024'),

-- 💼 Business (5)
(26, 'Fiona Green', 'Business', 'PhD Finance', 'Investment Strategies', 3, 'Stock Market Analysis', 'Finance Today 2023'),
(27, 'Peter Clarke', 'Business', 'PhD Marketing', 'Consumer Behavior', 2, 'Brand Management', 'Marketing Journal 2022'),
(28, 'Zachary Miller', 'Business', 'PhD Strategic Management', 'Corporate Strategy', 2, 'Business Leadership', 'Management Journal 2023'),
(29, 'Lucy Anderson', 'Business', 'PhD Human Resources', 'Workplace Psychology', 2, 'Organizational Behavior', 'HR Journal 2023'),
(30, 'Nicholas Brown', 'Business', 'PhD Entrepreneurship', 'Startups and Innovation', 2, 'Venture Capital', 'Entrepreneurship Journal 2024'),

-- 🧠 Psychology (5)
(31, 'George White', 'Psychology', 'PhD Cognitive Science', 'Human Behavior', 3, 'Cognitive Neuroscience', 'PsychSci 2024'),
(32, 'Quentin Harris', 'Psychology', 'PhD Behavioral Science', 'Mental Health Research', 3, 'Cognitive Therapy', 'Behavioral Science 2024'),
(33, 'Adam Thompson', 'Psychology', 'PhD Neuroscience', 'Brain Imaging', 3, 'Neural Networks in Psychology', 'Neuroscience Today 2024'),
(34, 'Emma Turner', 'Psychology', 'PhD Social Psychology', 'Group Dynamics', 3, 'Social Influence', 'Psychology Journal 2023'),
(35, 'Jack Robinson', 'Psychology', 'PhD Developmental Psychology', 'Child Development', 3, 'Education and Learning', 'Child Psychology 2023'),

-- ⚙️ Mechanical Engineering (5)
(36, 'Helen King', 'Mechanical Engineering', 'PhD Robotics', 'AI in Robotics', 2, 'Industrial Automation', 'Robotics Review 2023'),
(37, 'Rachel Scott', 'Mechanical Engineering', 'PhD Automotive Engineering', 'Electric Vehicles', 2, 'Battery Tech Innovations', 'Automotive Journal 2023'),
(38, 'Bella Richardson', 'Mechanical Engineering', 'PhD Thermodynamics', 'Energy Efficiency', 2, 'Sustainable Energy Solutions', 'Engineering Review 2023'),
(39, 'Benjamin Scott', 'Mechanical Engineering', 'PhD Aerospace Engineering', 'Aerodynamics', 2, 'Aircraft Design', 'Aerospace Journal 2024'),
(40, 'Sophia Lewis', 'Mechanical Engineering', 'PhD Mechatronics', 'Sensors & Automation', 2, 'Smart Manufacturing', 'Mechatronics Journal 2024'),

-- ⚡ Electrical Engineering (5)
(41, 'Isaac Lee', 'Electrical Engineering', 'PhD Energy Systems', 'Renewable Energy', 3, 'Solar and Wind Power', 'Energy Journal 2022'),
(42, 'Samuel White', 'Electrical Engineering', 'PhD Digital Systems', 'Embedded Systems', 3, 'Internet of Things', 'IoT Journal 2023'),
(43, 'Charles Roberts', 'Electrical Engineering', 'PhD Control Systems', 'Automation', 3, 'Smart Grid Development', 'Energy Systems Journal 2022'),
(44, 'Derek Anderson', 'Electrical Engineering', 'PhD Signal Processing', 'Wireless Communications', 3, '5G Technology', 'Signal Processing Journal 2023'),
(45, 'Melissa Young', 'Electrical Engineering', 'PhD Electronics', 'Semiconductors', 3, 'Microchip Research', 'Electronics Journal 2024');

-- Insert Courses for all departments
INSERT INTO courses (course_code, name, description, department, level, credits, prerequisites, schedule, materials)
VALUES
('CS101', 'Introduction to AI', 'Basics of AI concepts and applications', 'Computer Science', 1, 3, NULL, 'Mon/Wed 10-11 AM', 'Lecture Notes'),
('CS102', 'Data Structures', 'Fundamentals of data structures', 'Computer Science', 1, 3, NULL, 'Tue/Thu 11-12 PM', 'Textbook'),
('CS103', 'Algorithms', 'Analysis and design of algorithms', 'Computer Science', 2, 3, 'CS102', 'Mon/Wed 2-3 PM', 'Lecture Notes'),
('CS104', 'Machine Learning', 'Supervised and unsupervised learning', 'Computer Science', 3, 3, 'CS101', 'Tue/Thu 3-4 PM', 'Research Papers'),
('CS105', 'Cybersecurity Fundamentals', 'Introduction to security threats', 'Computer Science', 2, 3, NULL, 'Fri 10-12 PM', 'Textbook'),
('MATH201', 'Linear Algebra', 'Vector spaces and transformations', 'Mathematics', 1, 3, NULL, 'Mon/Wed 9-10 AM', 'Textbook'),
('MATH202', 'Calculus I', 'Differential and integral calculus', 'Mathematics', 1, 3, NULL, 'Tue/Thu 10-11 AM', 'Textbook'),
('MATH203', 'Probability and Statistics', 'Basic probability theory and statistics', 'Mathematics', 2, 3, 'MATH202', 'Wed/Fri 1-2 PM', 'Lecture Notes'),
('MATH204', 'Discrete Mathematics', 'Fundamentals of discrete mathematics', 'Mathematics', 2, 3, NULL, 'Mon/Wed 2-3 PM', 'Textbook'),
('MATH205', 'Numerical Methods', 'Computational techniques for mathematical problems', 'Mathematics', 3, 3, 'MATH201', 'Tue/Thu 3-4 PM', 'Research Papers'),
('PHY301', 'Classical Mechanics', 'Newtonian physics principles', 'Physics', 1, 3, NULL, 'Mon/Wed 10-11 AM', 'Lecture Notes'),
('PHY302', 'Electromagnetism', 'Maxwell equations and applications', 'Physics', 2, 3, 'PHY301', 'Tue/Thu 11-12 PM', 'Textbook'),
('PHY303', 'Quantum Mechanics', 'Introduction to quantum physics', 'Physics', 3, 3, 'PHY302', 'Wed/Fri 2-3 PM', 'Research Papers'),
('PHY304', 'Astrophysics', 'Study of celestial bodies', 'Physics', 3, 3, NULL, 'Mon/Wed 3-4 PM', 'Lecture Notes'),
('PHY305', 'Thermodynamics', 'Laws of thermodynamics', 'Physics', 2, 3, 'PHY301', 'Tue/Thu 9-10 AM', 'Textbook'),
('BUS101', 'Principles of Marketing', 'Fundamentals of marketing strategies', 'Business', 1, 3, NULL, 'Mon/Wed 10-11 AM', 'Textbook'),
('BUS102', 'Financial Accounting', 'Accounting principles and practices', 'Business', 1, 3, NULL, 'Tue/Thu 2-3 PM', 'Lecture Notes'),
('BUS103', 'Business Strategy', 'Strategic planning for organizations', 'Business', 2, 3, 'BUS101', 'Mon/Wed 3-4 PM', 'Case Studies'),
('BUS104', 'Entrepreneurship', 'Basics of starting a business', 'Business', 3, 3, NULL, 'Tue/Thu 9-10 AM', 'Research Papers'),
('BUS105', 'Investment Analysis', 'Risk assessment in investments', 'Business', 3, 3, 'BUS102', 'Wed/Fri 1-2 PM', 'Textbook'),
('BIO101', 'Genetics', 'Fundamentals of genetic engineering', 'Biology', 1, 3, NULL, 'Mon/Wed 10-11 AM', 'Textbook'),
('BIO102', 'Microbiology', 'Study of microorganisms', 'Biology', 2, 3, 'BIO101', 'Tue/Thu 11-12 PM', 'Research Papers'),
('BIO103', 'Neuroscience', 'Study of the nervous system', 'Biology', 3, 3, 'BIO102', 'Wed/Fri 1-2 PM', 'Lecture Notes'),
('BIO104', 'Molecular Biology', 'Molecular mechanisms of cells', 'Biology', 3, 3, 'BIO101', 'Mon/Wed 2-3 PM', 'Textbook'),
('BIO105', 'Biotechnology', 'Applications of biology in industry', 'Biology', 3, 3, 'BIO103', 'Tue/Thu 3-4 PM', 'Research Papers'),
('MECH201', 'Thermodynamics', 'Principles of heat and work', 'Mechanical Engineering', 2, 3, NULL, 'Mon/Wed 10-11 AM', 'Textbook'),
('MECH202', 'Robotics', 'Introduction to robotic systems', 'Mechanical Engineering', 3, 3, 'MECH201', 'Tue/Thu 11-12 PM', 'Research Papers'),
('MECH203', 'Mechanical Design', 'Design principles for mechanical systems', 'Mechanical Engineering', 3, 3, 'MECH201', 'Wed/Fri 1-2 PM', 'Lecture Notes'),
('MECH204', 'Fluid Mechanics', 'Study of fluid dynamics', 'Mechanical Engineering', 3, 3, 'MECH202', 'Mon/Wed 2-3 PM', 'Textbook'),
('MECH205', 'Control Systems', 'Automation and control theory', 'Mechanical Engineering', 3, 3, 'MECH203', 'Tue/Thu 3-4 PM', 'Research Papers'),
('ELEC301', 'Power Systems', 'Electrical power generation and distribution', 'Electrical Engineering', 3, 3, NULL, 'Mon/Wed 10-11 AM', 'Textbook'),
('ELEC302', 'Digital Circuits', 'Design of digital electronic circuits', 'Electrical Engineering', 2, 3, NULL, 'Tue/Thu 11-12 PM', 'Lecture Notes'),
('ELEC303', 'Embedded Systems', 'Microcontroller programming and interfacing', 'Electrical Engineering', 3, 3, 'ELEC302', 'Wed/Fri 1-2 PM', 'Research Papers'),
('ELEC304', 'Signal Processing', 'Analysis of signals and systems', 'Electrical Engineering', 3, 3, 'ELEC303', 'Mon/Wed 2-3 PM', 'Textbook'),
('ELEC305', 'Renewable Energy Systems', 'Integration of renewable energy sources', 'Electrical Engineering', 3, 3, 'ELEC301', 'Tue/Thu 3-4 PM', 'Research Papers'),
('HIST201', 'World History', 'Study of global civilizations and their impact.', 'History', 1, 3, NULL, 'Tue/Thu 10-11 AM', 'Lecture Notes'),
('HIST202', 'Ancient Civilizations', 'Exploring ancient societies like Egypt, Rome, and Greece.', 'History', 2, 3, NULL, 'Mon/Wed 2-3 PM', 'Textbook'),
('HIST203', 'Renaissance & Reformation', 'European cultural and religious changes.', 'History', 2, 3, NULL, 'Fri 11-12 PM', 'Research Papers'),
('HIST204', 'Modern European History', 'Political and social changes in 19th-20th centuries.', 'History', 3, 3, 'HIST201', 'Wed/Fri 1-2 PM', 'Textbook'),
('HIST205', 'History of Science & Technology', 'How scientific discoveries shaped society.', 'History', 3, 3, NULL, 'Mon/Wed 4-5 PM', 'Lecture Notes'),
('CHEM201', 'Physical Chemistry', 'Study of thermodynamics and quantum mechanics.', 'Chemistry', 2, 3, 'CHEM101', 'Tue/Thu 10-11 AM', 'Textbook'),
('CHEM202', 'Inorganic Chemistry', 'Study of non-organic elements and compounds.', 'Chemistry', 2, 3, NULL, 'Mon/Wed 2-3 PM', 'Lecture Notes'),
('CHEM203', 'Organic Chemistry II', 'Advanced study of organic compounds.', 'Chemistry', 3, 3, 'CHEM101', 'Fri 11-12 PM', 'Research Papers'),
('CHEM204', 'Chemical Engineering Principles', 'Application of chemistry in industrial processes.', 'Chemistry', 3, 3, 'CHEM201', 'Wed/Fri 1-2 PM', 'Textbook'),
('CHEM205', 'Pharmaceutical Chemistry', 'Study of drug design and synthesis.', 'Chemistry', 3, 3, 'CHEM203', 'Mon/Wed 4-5 PM', 'Lecture Notes'),
('PSY201', 'Cognitive Psychology', 'Study of perception, memory, and problem-solving.', 'Psychology', 2, 3, 'PSY101', 'Tue/Thu 10-11 AM', 'Textbook'),
('PSY202', 'Clinical Psychology', 'Application of psychology in therapy and diagnosis.', 'Psychology', 3, 3, 'PSY101', 'Mon/Wed 2-3 PM', 'Lecture Notes'),
('PSY203', 'Social Psychology', 'How individuals behave in social situations.', 'Psychology', 2, 3, NULL, 'Fri 11-12 PM', 'Research Papers'),
('PSY204', 'Neuroscience & Behavior', 'How brain structure influences emotions and behavior.', 'Psychology', 3, 3, NULL, 'Wed/Fri 1-2 PM', 'Textbook'),
('PSY205', 'Developmental Psychology', 'Psychological growth from childhood to adulthood.', 'Psychology', 3, 3, NULL, 'Mon/Wed 4-5 PM', 'Lecture Notes');


INSERT INTO students (student_id, name, dob, contact_info, program, year_of_study, current_grades, graduation_status, disciplinary_records, advisor_id)
VALUES
-- 🖥️ Computer Science Students (Advisors: 1-5)
(1, 'John Doe', '2001-05-15', 'john.doe@liverpool.ac.uk', 'Computer Science', 4, 85.5, 'In Progress', NULL, 1),
(2, 'Ethan Walker', '2001-05-02', 'ethan.walker@liverpool.ac.uk', 'Computer Science', 3, 82.4, 'In Progress', NULL, 2),
(3, 'Lucas Green', '2000-05-08', 'lucas.green@liverpool.ac.uk', 'Computer Science', 4, 79.8, 'In Progress', NULL, 3),

-- 🧮 Mathematics Students (Advisors: 6-10)
(4, 'Jane Smith', '2002-08-22', 'jane.smith@liverpool.ac.uk', 'Mathematics', 3, 72.0, 'In Progress', NULL, 6),
(5, 'Sophia Evans', '2000-08-19', 'sophia.evans@liverpool.ac.uk', 'Mathematics', 4, 78.8, 'In Progress', NULL, 7),
(6, 'Mia Cooper', '2002-07-21', 'mia.cooper@liverpool.ac.uk', 'Mathematics', 3, 74.3, 'In Progress', NULL, 8),

-- 🔬 Physics Students (Advisors: 11-15)
(7, 'Michael Brown', '2000-11-10', 'michael.brown@liverpool.ac.uk', 'Physics', 2, 78.3, 'In Progress', NULL, 11),
(8, 'William King', '2002-10-28', 'william.king@liverpool.ac.uk', 'Physics', 2, 80.1, 'In Progress', NULL, 12),
(9, 'Mason Wright', '2001-09-17', 'mason.wright@liverpool.ac.uk', 'Physics', 2, 81.9, 'In Progress', NULL, 13),

-- 🧬 Biology Students (Advisors: 16-20)
(10, 'Emily Johnson', '2003-02-18', 'emily.johnson@liverpool.ac.uk', 'Biology', 1, 91.2, 'In Progress', NULL, 16),
(11, 'Chloe Scott', '2003-03-07', 'chloe.scott@liverpool.ac.uk', 'Biology', 1, 92.7, 'In Progress', NULL, 17),
(12, 'Lily Young', '2003-01-12', 'lily.young@liverpool.ac.uk', 'Biology', 1, 94.2, 'In Progress', NULL, 18),

-- 🧪 Chemistry Students (Advisors: 21-25)
(13, 'David Wilson', '2001-07-30', 'david.wilson@liverpool.ac.uk', 'Chemistry', 3, 68.5, 'In Progress', NULL, 21),
(14, 'Matthew Adams', '2001-06-14', 'matthew.adams@liverpool.ac.uk', 'Chemistry', 3, 70.9, 'In Progress', NULL, 22),
(15, 'Noah Perez', '2000-12-24', 'noah.perez@liverpool.ac.uk', 'Chemistry', 3, 68.7, 'In Progress', NULL, 23),

-- 💼 Business Students (Advisors: 26-30)
(16, 'Sarah Martinez', '2002-04-25', 'sarah.martinez@liverpool.ac.uk', 'Business', 2, 76.1, 'In Progress', NULL, 26),
(17, 'Ava Baker', '2002-01-22', 'ava.baker@liverpool.ac.uk', 'Business', 2, 75.3, 'In Progress', NULL, 27),
(18, 'Ella Murphy', '2002-03-29', 'ella.murphy@liverpool.ac.uk', 'Business', 2, 76.4, 'In Progress', NULL, 28),

-- 🧠 Psychology Students (Advisors: 31-35)
(19, 'Daniel Lee', '2000-09-14', 'daniel.lee@liverpool.ac.uk', 'Psychology', 4, 89.9, 'In Progress', NULL, 31),
(20, 'Liam Carter', '2000-07-16', 'liam.carter@liverpool.ac.uk', 'Psychology', 4, 88.4, 'In Progress', NULL, 32),
(21, 'Jacob Bennett', '2001-08-10', 'jacob.bennett@liverpool.ac.uk', 'Psychology', 4, 89.1, 'In Progress', NULL, 33),

-- ⚙️ Mechanical Engineering Students (Advisors: 36-40)
(22, 'Laura White', '2003-06-22', 'laura.white@liverpool.ac.uk', 'Mechanical Engineering', 1, 79.3, 'In Progress', NULL, 36),
(23, 'Charlotte Mitchell', '2003-09-05', 'charlotte.mitchell@liverpool.ac.uk', 'Mechanical Engineering', 1, 81.5, 'In Progress', NULL, 37),
(24, 'Zoe Reed', '2003-06-27', 'zoe.reed@liverpool.ac.uk', 'Mechanical Engineering', 1, 83.7, 'In Progress', NULL, 38),

-- ⚡ Electrical Engineering Students (Advisors: 41-45)
(25, 'James Harris', '2001-03-11', 'james.harris@liverpool.ac.uk', 'Electrical Engineering', 3, 84.2, 'In Progress', NULL, 41),
(26, 'Benjamin Roberts', '2001-11-30', 'benjamin.roberts@liverpool.ac.uk', 'Electrical Engineering', 3, 85.9, 'In Progress', NULL, 42),
(27, 'Logan Foster', '2000-10-30', 'logan.foster@liverpool.ac.uk', 'Electrical Engineering', 3, 86.3, 'In Progress', NULL, 43);

-- Insert Programs
INSERT INTO programs (name, degree_awarded, duration, course_requirements, enrolment_details)
VALUES
('Computer Science', 'BSc', 4, 'Core AI, Data Science, Software Engineering', 'Full-time'),
('Mechanical Engineering', 'BEng', 4, 'Thermodynamics, Robotics, Design', 'Full-time'),
('Electrical Engineering', 'BEng', 4, 'Circuits, Renewable Energy, Signal Processing', 'Full-time'),
('Mathematics', 'BSc', 3, 'Statistics, Algebra, Geometry', 'Full-time'),
('Physics', 'BSc', 3, 'Quantum Mechanics, Astrophysics', 'Full-time'),
('Biology', 'BSc', 3, 'Genetics, Microbiology, Neuroscience', 'Full-time'),
('Chemistry', 'BSc', 3, 'Organic, Inorganic, Analytical Chemistry', 'Full-time'),
('Business Administration', 'BBA', 3, 'Finance, Marketing, Strategy', 'Full-time'),
('Psychology', 'BSc', 3, 'Cognitive Science, Behavioral Analysis', 'Full-time'),
('History', 'BA', 3, 'Medieval Studies, Modern History', 'Full-time'),
('Artificial Intelligence', 'MSc', 2, 'Machine Learning, Deep Learning', 'Full-time'),
('Cybersecurity', 'MSc', 2, 'Network Security, Ethical Hacking', 'Full-time'),
('Data Science', 'MSc', 2, 'Big Data, Analytics, AI', 'Full-time'),
('Finance and Accounting', 'MSc', 2, 'Financial Modelling, Risk Management', 'Full-time'),
('Marketing Management', 'MSc', 2, 'Digital Marketing, Branding', 'Full-time'),
('Environmental Science', 'MSc', 2, 'Climate Change, Renewable Energy', 'Full-time'),
('Medical Research', 'MSc', 2, 'Clinical Studies, Biomedical Research', 'Full-time');

-- Insert enrollments ensuring students only take courses from their major
INSERT INTO enrollments (student_id, course_id)
SELECT s.student_id, c.course_code
FROM students s
JOIN courses c ON s.program = c.department
ORDER BY RAND()
LIMIT 100;

-- Insert lecturer-course assignments ensuring lecturers only teach their department's courses
INSERT INTO lecturer_courses (lecturer_id, course_id)
SELECT l.lecturer_id, c.course_code
FROM lecturers l
JOIN courses c ON l.department = c.department
ORDER BY RAND()
LIMIT 60;

-- Insert Research Projects dynamically based on lecturers and students
INSERT INTO research_projects (project_title, principal_investigator, funding_sources, team_members, publications, outcomes)
SELECT 
    CONCAT(l.expertise, ' Research #', ROW_NUMBER() OVER (PARTITION BY l.lecturer_id ORDER BY RAND())), 
    l.lecturer_id,                     
    'University Research Grant',        
    CONCAT(l.name, ', Student ', s1.student_id, ', Student ', s2.student_id), 
    CONCAT(l.expertise, ' Journal'), 
    CONCAT('Innovative research in ', l.expertise)  
FROM lecturers l
JOIN students s1 ON s1.program = l.department  
JOIN students s2 ON s2.program = l.department AND s1.student_id <> s2.student_id  
ORDER BY RAND()
LIMIT 100;  -- Adjust the number of projects as needed

-- Insert Non-Academic Staff
INSERT INTO non_academic_staff (staff_id, name, job_title, department, employment_type, contract_details, salary_information, emergency_contact)
VALUES
(1, 'Mike Johnson', 'Administrator', 'Computer Science', 'Full-time', '5-year contract', 50000, 'mike.johnson@liverpool.ac.uk'),
(2, 'Sarah Adams', 'HR Manager', 'Business', 'Full-time', 'Permanent', 55000, 'sarah.adams@liverpool.ac.uk'),
(3, 'James Carter', 'IT Support Technician', 'Computer Science', 'Full-time', '3-year contract', 48000, 'james.carter@liverpool.ac.uk'),
(4, 'Laura Green', 'Librarian', 'Library Services', 'Full-time', 'Permanent', 42000, 'laura.green@liverpool.ac.uk'),
(5, 'Tom Wright', 'Financial Officer', 'Finance Department', 'Full-time', '5-year contract', 60000, 'tom.wright@liverpool.ac.uk'),
(6, 'Emma White', 'Student Affairs Officer', 'Student Services', 'Full-time', 'Permanent', 47000, 'emma.white@liverpool.ac.uk'),
(7, 'Daniel Lee', 'Facilities Manager', 'Operations', 'Full-time', '10-year contract', 58000, 'daniel.lee@liverpool.ac.uk'),
(8, 'Sophie Harris', 'Marketing Coordinator', 'Marketing', 'Full-time', '3-year contract', 52000, 'sophie.harris@liverpool.ac.uk'),
(9, 'David Brown', 'Research Coordinator', 'Research Office', 'Full-time', '4-year contract', 51000, 'david.brown@liverpool.ac.uk'),
(11, 'Emma Thompson', 'Research Coordinator', 'Computer Science', 'Full-time', 'Permanent', 56000, 'emma.thompson@liverpool.ac.uk'),
(12, 'Mark Harrison', 'Technical Lab Assistant', 'Mechanical Engineering', 'Full-time', '3-year contract', 49000, 'mark.harrison@liverpool.ac.uk'),
(13, 'Rachel Adams', 'Student Support Officer', 'Business', 'Full-time', 'Permanent', 52000, 'rachel.adams@liverpool.ac.uk'),
(14, 'Steven Wilson', 'Academic Advisor', 'History', 'Full-time', '5-year contract', 53000, 'steven.wilson@liverpool.ac.uk'),
(15, 'Lisa Carter', 'Librarian', 'Psychology', 'Full-time', 'Permanent', 47000, 'lisa.carter@liverpool.ac.uk'),
(16, 'Brian Parker', 'Administrative Officer', 'Mathematics', 'Full-time', '5-year contract', 51000, 'brian.parker@liverpool.ac.uk'),
(17, 'Sophia Turner', 'Financial Manager', 'Chemistry', 'Full-time', 'Permanent', 60000, 'sophia.turner@liverpool.ac.uk'),
(18, 'Michael Scott', 'Research Assistant', 'Physics', 'Full-time', '4-year contract', 48000, 'michael.scott@liverpool.ac.uk'),
(19, 'Nancy White', 'Student Affairs Officer', 'Biology', 'Full-time', '3-year contract', 53000, 'nancy.white@liverpool.ac.uk'),
(20, 'Tom Green', 'HR Specialist', 'Electrical Engineering', 'Full-time', 'Permanent', 55000, 'tom.green@liverpool.ac.uk');


-- Commit the changes
COMMIT;
