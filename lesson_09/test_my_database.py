from MyDatabase import MyDatabase


db = MyDatabase(
    "postgresql://postgres:Igubif52@127.0.0.1:5432/DB_for_autotest"
)


# Тест на добавление студента
def test_add_student():
    db_result_before = db.get_list_of_students()
    max_id_result = db.get_max_id()
    new_student_id = max_id_result + 1
    added_student = db.add_new_student(new_student_id, "Beginner", "group", 2)
    db_result_after = db.get_list_of_students()

    db.delete(added_student)

    assert len(db_result_after) - 1 == len(db_result_before)


# Тест на изменение данных о студенте
def test_update_student():
    max_id_result = db.get_max_id()
    new_student_id = max_id_result + 1
    db.add_new_student(new_student_id, "Beginner", "group", 2)

    db.update_student(new_student_id, "Advanced", "personal")

    all_students = db.get_list_of_students()
    updated_student = None
    for student in all_students:
        if student["user_id"] == new_student_id:
            updated_student = student
            break

    db.delete(new_student_id)

    assert updated_student["level"] == "Advanced"
    assert updated_student["education_form"] == "personal"


# Тест на удаление студента
def test_delete_student():
    max_id_result = db.get_max_id()
    new_student_id = max_id_result + 1
    db.add_new_student(new_student_id, "Beginner", "group", 2)
    db_result_before = db.get_list_of_students()

    db.delete(new_student_id)

    db_result_after = db.get_list_of_students()

    assert len(db_result_before) - 1 == len(db_result_after)
