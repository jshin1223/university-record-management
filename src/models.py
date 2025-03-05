"""
This module defines the SQLAlchemy ORM models for the University Record Management System.
It sets up the database connection, creates the required tables, and defines relationships
between entities such as students, lecturers, courses, departments, programs, and research projects.
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Text, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.sql import text
from config import DB_CONFIG
# import pymysql

# Database configuration
DB_NAME = DB_CONFIG["database"]
CONNECTION_URL = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}"

# Ensure database exists before defining tables
engine = create_engine(CONNECTION_URL)
with engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))

# Connect to the actual database
DATABASE_URL = f"{CONNECTION_URL}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# Define ORM base class
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define many-to-many relationship between Students and Courses
enrollments = Table(
    "enrollments",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.student_id"), primary_key=True),
    Column("course_id", String(20), ForeignKey("courses.course_code"), primary_key=True)
)

# Define many-to-many relationship between Lecturers and Courses
lecturer_courses = Table(
    "lecturer_courses",
    Base.metadata,
    Column("lecturer_id", Integer, ForeignKey("lecturers.lecturer_id"), primary_key=True),
    Column("course_id", String(20), ForeignKey("courses.course_code"), primary_key=True)
)

# Students Table
class Student(Base):
    """
    Represents a student in the university.
    """
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)  # Unique student ID
    name = Column(String(100), nullable=False)  # Student name
    dob = Column(String(10))  # Date of birth
    contact_info = Column(String(255))  # Email or phone contact details
    program = Column(String(100))  # Program of study
    year_of_study = Column(Integer)  # Current academic year
    current_grades = Column(Float)  # Current average grade
    graduation_status = Column(String(50))  # Graduation progress (e.g., "In Progress")
    disciplinary_records = Column(Text)  # Disciplinary actions (if any)
    advisor_id = Column(Integer, ForeignKey("lecturers.lecturer_id"))  # Faculty advisor

    # Relationships
    advisor = relationship("Lecturer", back_populates="students_advised")
    courses = relationship("Course", secondary=enrollments, back_populates="students_enrolled")

# Lecturers Table
class Lecturer(Base):
    """
    Represents a lecturer in the university.
    """
    __tablename__ = "lecturers"

    lecturer_id = Column(Integer, primary_key=True)  # Unique lecturer ID
    name = Column(String(100), nullable=False)  # Lecturer name
    department = Column(String(100))  # Department affiliation
    academic_qualifications = Column(String(255))  # Academic degrees
    expertise = Column(String(255))  # Areas of expertise
    course_load = Column(Integer)  # Number of courses taught
    research_interests = Column(Text)  # Research topics
    publications = Column(Text)  # Publications

    # Relationships
    students_advised = relationship("Student", back_populates="advisor")
    courses_taught = relationship("Course", secondary=lecturer_courses, back_populates="lecturers")

# Non-Academic Staff Table
class NonAcademicStaff(Base):
    """
    Represents non-academic staff members.
    """
    __tablename__ = "non_academic_staff"

    staff_id = Column(Integer, primary_key=True)  # Unique staff ID
    name = Column(String(100), nullable=False)  # Staff name
    job_title = Column(String(100))  # Position title
    department = Column(String(100))  # Assigned department
    employment_type = Column(String(50))  # Full-time, part-time, etc.
    contract_details = Column(Text)  # Employment contract information
    salary_information = Column(Float)  # Salary details
    emergency_contact = Column(String(255))  # Emergency contact info

# Courses Table
class Course(Base):
    """
    Represents a university course.
    """
    __tablename__ = "courses"

    course_code = Column(String(20), primary_key=True)  # Unique course code
    name = Column(String(100), nullable=False)  # Course name
    description = Column(Text)  # Course description
    department = Column(String(100))  # Department offering the course
    level = Column(Integer)  # Course level (e.g., undergraduate, postgraduate)
    credits = Column(Integer)  # Credit hours
    prerequisites = Column(Text)  # Prerequisites for the course
    schedule = Column(String(100))  # Scheduled days and times
    materials = Column(Text)  # Required learning materials

    # Relationships
    students_enrolled = relationship("Student", secondary=enrollments, back_populates="courses")
    lecturers = relationship("Lecturer", secondary=lecturer_courses, back_populates="courses_taught")

# Departments Table
class Department(Base):
    """
    Represents a university department.
    """
    __tablename__ = "departments"

    department_name = Column(String(100), primary_key=True)  # Unique department name
    faculty = Column(String(100))  # Faculty overseeing the department
    research_areas = Column(Text)  # Key research areas
    courses_offered = Column(Integer)  # Number of courses available
    staff_members = Column(Integer)  # Number of staff members in the department

# Programs Table
class Program(Base):
    """
    Represents a degree program at the university.
    """
    __tablename__ = "programs"

    name = Column(String(100), primary_key=True)  # Program name
    degree_awarded = Column(String(100))  # Type of degree awarded (e.g., BSc, MSc)
    duration = Column(Integer)  # Program duration in years
    course_requirements = Column(Text)  # Required courses
    enrolment_details = Column(Text)  # Details about enrolment

# Research Projects Table
class ResearchProject(Base):
    """
    Represents research projects supervised by university lecturers.
    """
    __tablename__ = "research_projects"

    project_title = Column(String(255), primary_key=True)  # Unique project title
    principal_investigator = Column(Integer, ForeignKey("lecturers.lecturer_id"))  # Lead investigator (lecturer)
    funding_sources = Column(String(255))  # Funding details
    team_members = Column(Text)  # List of team members
    publications = Column(Text)  # Publications resulting from the project
    outcomes = Column(Text)  # Key findings

    # Relationships
    investigator = relationship("Lecturer")

# Create all tables in the database
Base.metadata.create_all(engine)
print("✅ Database and tables created successfully.")
