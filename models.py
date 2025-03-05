from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Text, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.sql import text
from config import DB_CONFIG
import pymysql

# Ensure database creation before defining tables
DB_NAME = DB_CONFIG["database"]
CONNECTION_URL = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}"

# Connect to MySQL without a database and create `university_db` if it does not exist
engine = create_engine(CONNECTION_URL)
with engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))

# Now connect to the actual database
DATABASE_URL = f"{CONNECTION_URL}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# Define ORM base class
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Many-to-Many relationship table between Students and Courses
enrollments = Table(
    "enrollments",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.student_id"), primary_key=True),
    Column("course_id", String(20), ForeignKey("courses.course_code"), primary_key=True)
)

# Many-to-Many relationship table between Lecturers and Courses
lecturer_courses = Table(
    "lecturer_courses",
    Base.metadata,
    Column("lecturer_id", Integer, ForeignKey("lecturers.lecturer_id"), primary_key=True),
    Column("course_id", String(20), ForeignKey("courses.course_code"), primary_key=True)
)

# Students Table
class Student(Base):
    __tablename__ = "students"
    student_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    dob = Column(String(10))
    contact_info = Column(String(255))
    program = Column(String(100))
    year_of_study = Column(Integer)
    current_grades = Column(Float)
    graduation_status = Column(String(50))
    disciplinary_records = Column(Text)
    advisor_id = Column(Integer, ForeignKey("lecturers.lecturer_id"))

    advisor = relationship("Lecturer", back_populates="students_advised")
    courses = relationship("Course", secondary=enrollments, back_populates="students_enrolled")

# Lecturers Table
class Lecturer(Base):
    __tablename__ = "lecturers"
    lecturer_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    department = Column(String(100))
    academic_qualifications = Column(String(255))
    expertise = Column(String(255))
    course_load = Column(Integer)
    research_interests = Column(Text)
    publications = Column(Text)

    students_advised = relationship("Student", back_populates="advisor")
    courses_taught = relationship("Course", secondary=lecturer_courses, back_populates="lecturers")

# Non-Academic Staff Table
class NonAcademicStaff(Base):
    __tablename__ = "non_academic_staff"
    staff_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    job_title = Column(String(100))
    department = Column(String(100))
    employment_type = Column(String(50))
    contract_details = Column(Text)
    salary_information = Column(Float)
    emergency_contact = Column(String(255))

# Courses Table
class Course(Base):
    __tablename__ = "courses"
    course_code = Column(String(20), primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    department = Column(String(100))
    level = Column(Integer)
    credits = Column(Integer)
    prerequisites = Column(Text)
    schedule = Column(String(100))
    materials = Column(Text)

    students_enrolled = relationship("Student", secondary=enrollments, back_populates="courses")
    lecturers = relationship("Lecturer", secondary=lecturer_courses, back_populates="courses_taught")

# Departments Table
class Department(Base):
    __tablename__ = "departments"
    department_name = Column(String(100), primary_key=True)
    faculty = Column(String(100))
    research_areas = Column(Text)
    courses_offered = Column(Integer)
    staff_members = Column(Integer)

# Programs Table
class Program(Base):
    __tablename__ = "programs"
    name = Column(String(100), primary_key=True)
    degree_awarded = Column(String(100))
    duration = Column(Integer)
    course_requirements = Column(Text)
    enrolment_details = Column(Text)

# Research Projects Table
class ResearchProject(Base):
    __tablename__ = "research_projects"
    project_title = Column(String(255), primary_key=True)
    principal_investigator = Column(Integer, ForeignKey("lecturers.lecturer_id"))
    funding_sources = Column(String(255))
    team_members = Column(Text)
    publications = Column(Text)
    outcomes = Column(Text)

    investigator = relationship("Lecturer")




# Create all tables
Base.metadata.create_all(engine)
print("✅ Database and tables created successfully.")
