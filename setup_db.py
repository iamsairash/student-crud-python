from db.connection import get_connection, get_cursor

def create_tables():
    conn = get_connection()
    cur = get_cursor(conn)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(150) UNIQUE NOT NULL,
            age INT CHECK (age > 0 AND age < 120),
            enrollment_date DATE DEFAULT CURRENT_DATE
        );
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id SERIAL PRIMARY KEY,
            course_name VARCHAR(150) NOT NULL,
            description TEXT,
            credits INT CHECK (credits > 0)
        );
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student_courses (
            id SERIAL PRIMARY KEY,
            student_id INT REFERENCES students(id) ON DELETE CASCADE,
            course_id INT REFERENCES courses(id) ON DELETE CASCADE,
            enrolled_on DATE DEFAULT CURRENT_DATE,
            UNIQUE(student_id, course_id) 
        );
    """)
    
    conn.commit()
    cur.close()
    conn.close()
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()