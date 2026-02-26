from db.connection import get_connection, get_cursor

def create_course(course_name, description, credits):
    conn = get_connection()
    cur = get_cursor(conn)
    
    try:
        cur.execute(
            "INSERT INTO courses (course_name, description, credits) VALUES (%s, %s, %s) RETURNING *;",
            (course_name, description, credits)
        )
        course = cur.fetchone()
        conn.commit()
        
        print(f"Created course: {dict(course)}")
        return dict(course)
    except Exception as e:
        conn.rollback()
        print(f"ERROR: {e}")
    finally:
        cur.close()
        conn.close()

def get_all_courses():
    conn = get_connection()
    cur = get_cursor(conn)
    
    cur.execute("SELECT * FROM courses ORDER BY id;")
    courses = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(c) for c in courses]

def get_course_by_id(course_id):
    conn = get_connection()
    cur = get_cursor(conn)
    
    cur.execute("SELECT * FROM courses WHERE id = %s;",(course_id,))
    course = cur.fetchone()
    cur.close()
    conn.close()
    return dict(course) if course else None

def update_course(course_id, course_name= None, description=None, credits=None):
    conn = get_connection()
    cur = get_cursor(conn)
    
    try:
        fields = []
        values = []
        if course_name:
            fields.append("course_name = %s")
            values.append(course_name)
        if description:
            fields.append("description = %s")
            values.append(description)
        if credits:
            fields.append("credits = %s")
            values.append(credits)
        
        if not fields:
            print("Nothing to update.")
            return
        
        values.append(course_id)
        query = f"UPDATE course SET {', '.join(values)} WHERE id = %s RETURNING *;"
        cur.execute(query, values)
        updated = cur.fetchone()
        print(f"Updated: {dict(updated)}")
        return dict(updated)
    except Exception as e:
        conn.rollback()
        print(f"ERROR: {e}")
    finally:
        cur.close()
        conn.close()

def delete_course(course_id):
    conn = get_connection()
    cur = get_cursor(conn)
    
    try:
        cur.execute("DELETE FROM courses WHERE id = %s RETURNING course_name;",(course_id,))
        deleted = cur.fetchone()
        conn.commit()
        if deleted:
            print(f"Deleted course: {deleted["course_name"]}")
        else:
            print("course not found.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
        