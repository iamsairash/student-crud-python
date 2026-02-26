from db.connection import get_connection, get_cursor

def enroll_student(student_id, course_id):
    conn = get_connection()
    cur = get_cursor(conn)

    try:
        cur.execute("INSERT INTO student_courses (student_id, course_id) VALUES (%s, %s) RETURNING *;",
                (student_id, course_id))
        enrollment = cur.fetchone()
        conn.commit()
        print(f"Enrolled student {student_id} in course {course_id}")
        return dict(enrollment)
    except Exception as e:
        conn.rollback()
        print(f"ERROR: {e}")
    finally:
        cur.close()
        conn.close()

        