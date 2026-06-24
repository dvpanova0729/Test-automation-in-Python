from sqlalchemy import create_engine, text


class MyDatabase:
    __scripts = {
        "select": text("SELECT * FROM student"),
        "get_max_id": text("SELECT MAX(\"user_id\") FROM student"),
        "insert_new": text(
            "INSERT INTO student("
            "\"user_id\", "
            "\"level\", "
            "\"education_form\", "
            "\"subject_id\") "
            "VALUES ("
            ":new_student_id, "
            ":level, "
            ":education_form, "
            ":subject_id)"
        ),
        "delete_by_id": text(
            "DELETE FROM student WHERE user_id = :id_to_delete"
        ),
        "update_student": text(
            "UPDATE student SET level = :new_level,"
            "education_form = :new_education_form "
            "WHERE user_id = :new_student_id"
        )}

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)
        self.id = None

    def get_list_of_students(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def get_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.scalar()
        conn.close()
        return max_id

    def add_new_student(
        self,
        new_student_id,
        level,
        education_form,
        subject_id
    ):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["insert_new"],
            {
                "new_student_id": new_student_id,
                "level": level,
                "education_form": education_form,
                "subject_id": subject_id
            }
            )
        conn.commit()
        conn.close()
        return new_student_id

    def delete(self, id):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["delete_by_id"],
            {"id_to_delete": id}
        )
        conn.commit()
        conn.close()

    def update_student(self, new_student_id, new_level, new_education_form):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["update_student"],
            {
                "new_student_id": new_student_id,
                "new_level": new_level,
                "new_education_form": new_education_form
            }
        )
        conn.commit()
        conn.close()
