from db.connection import get_connection, get_cursor

# create student


def create_student(name, email, age):
    conn = get_connection()
    cur = get_cursor(conn)

    try:
        cur.execute(
            "INSERT INTO students (name, email, age) VALUES (%s, %s, %s) RETURNING *;",
            (name, email, age),
        )
        student = cur.fetchone()
        conn.commit()
        print(f"Created student: {dict(student)}")
        return dict(student)
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()


# read


def get_all_students():
    conn = get_connection()
    cur = get_cursor(conn)

    cur.execute("SELECT * FROM students ORDER BY id;")
    students = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(s) for s in students]


def get_student_by_id(student_id):
    conn = get_connection()
    cur = get_cursor(conn)

    cur.execute("SELECT * FROM students WHERE id = %s;", (student_id,))
    student = cur.fetchone()
    cur.close()
    conn.close()
    return dict(student) if student else None


# update
def update_student(student_id, name=None, email=None, age=None):
    conn = get_connection()
    cur = get_cursor(conn)

    try:
        fields = []
        values = []
        if name:
            fields.append("name = %s")
            values.append(name)
        if email:
            fields.append("email = %s")
            values.append(email)
        if age:
            fields.append("age = %s")
            values.append(age)

        if not fields:
            print("Nothing to update.")
            return

        values.append(student_id)
        query = f"UPDATE students SET {', '.join(fields)} WHERE id = %s RETURNING *;"
        cur.execute(query, values)

        updated = cur.fetchone()
        conn.commit()
        print(f"Updated: {dict(updated)}")
        return dict(updated)
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()


# delete
def delete_student(student_id):
    conn = get_connection()
    cur = get_cursor(conn)

    try:
        cur.execute("DELETE FROM students WHERE id = %s RETURNING name;", (student_id,))
        deleted = cur.fetchone()
        conn.commit()
        if deleted:
            print(f"Deleted student: {deleted['name']}")
        else:
            print("Student not found")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
