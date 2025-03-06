"""
populate_data.py

This script executes the populate_data.sql file to insert data into the MySQL database.
"""

import sys
import os

# Ensure the `src` directory is included in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import get_db_connection  

def execute_sql_file(filename):
    """Read and execute the SQL file for data population."""
    conn = get_db_connection()
    if conn is None:
        print("❌ Database connection failed.")
        return

    try:
        with conn.cursor() as cursor:
            with open(filename, 'r', encoding='utf-8') as file:
                sql_statements = file.read()
                for statement in sql_statements.split(';'):  # Execute each statement separately
                    statement = statement.strip()
                    if statement:
                        cursor.execute(statement)
        conn.commit()
        print("✅ Data successfully populated from populate_data.sql")
    except Exception as e:
        print(f"⚠️ Error while populating data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    execute_sql_file("data/populate_data.sql")
