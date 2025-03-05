import pymysql
from config import DB_CONFIG

def get_db_connection():
    """Connect to the MySQL database."""
    try:
        conn = pymysql.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"],
            port=DB_CONFIG["port"],
            ssl_disabled=True
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"❌ Database connection error: {e}")
        return None
