from models.students import create_student, delete_student, update_student, get_all_students, get_student_by_id
from models.course import create_course, update_course, get_all_courses, get_course_by_id,delete_course
from models.student_course import enroll_student

if __name__ == "__main__":
    print("=== STUDENTS ===")
    # sairash = create_student("Sairash", "sairash@gmail.com", 24)
    # pushpa = create_student("Pushpa", "pushpa@gmail.com", 23)
    # rishi = create_student("Rishi Raj", "rishiraj@gmail.com", 18)

    python = create_course("Python 101", "This is python course.", 50)
    math = create_course("Mathematics", "This is math course", 45)

    print(get_all_courses())
    
    