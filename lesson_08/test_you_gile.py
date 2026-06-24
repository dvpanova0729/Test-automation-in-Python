from YouGileAPI import YouGileAPI

api = YouGileAPI("https://ru.yougile.com/api-v2/")


# ----Создание проекта----
def test_create_project_successful():
    api.get_key()
    base_list = api.get_project_list()
    api.create_project("My new project")
    new_list = api.get_project_list()

    assert len(new_list) - len(base_list) == 1


def test_create_project_unauthorized():
    response = api.create_project_unauthorized()

    assert response.status_code == 401


# ----Изменение проекта----
def test_edit_project():
    api.get_key()
    base_list = api.get_project_list()
    api.edit_project()
    new_list = api.get_project_list()

    assert len(base_list) - len(new_list) == 1


def test_edit_nonexistent_project():
    api.get_key()
    response = api.edit_test_project("00000000-0000-0000-0000-000000000000")

    assert response.status_code == 404


# ----Получение проекта по id----
def test_get_project_by_id_successful():
    api.get_key()
    created_project_id = api.create_project("Create new project")
    get_progect_id = api.get_project_by_id()['id']

    assert created_project_id == get_progect_id


def test_get_project_by_incorect_id():
    response = api.get_project_by_incorrect_id("incorrect-id")

    assert response.status_code in [400, 404]
