import sqlite3
import os

# Database ka naam
DB_NAME = "attendance.db"

# Database ka pura path - ye file backend folder ke andar banegi
DB_PATH = os.path.join(os.path.dirname(__file__), DB_NAME)

def get_db_connection():
    """Database se connection banane ke liye function"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Data ko dictionary ki tarah access kar sakte hain
    return conn

def init_db():
    """Database aur faculty table banane ke liye function"""
    conn = get_db_connection()
    
    # faculty table banao agar pehle se nahi hai to
    conn.execute("""
        CREATE TABLE IF NOT EXISTS faculty (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            department TEXT NOT NULL
        );
    """)
    
    conn.commit()  # Changes ko save karo
    conn.close()   # Connection band karo
    print(f"Database \'{DB_NAME}\' initialized successfully!")
    print("Table \'faculty\' is ready with columns: id, name, email, department")

# Jab is file ko directly run karenge tabhi database banega
if __name__ == "__main__":
    init_db()