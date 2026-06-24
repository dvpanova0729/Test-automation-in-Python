from decouple import config
import requests


class YouGileAPI:

    def __init__(self, url):
        self.url = url
        self.auth_token = None
        self.project_id = None

    def get_key(self):
        user = config('USERNAME')
        password = config('PASSWORD')
        creds = {
            'login': user,
            'password': password
        }
        response = requests.post(self.url + 'auth/companies', json=creds)
        data = response.json()
        company_id = data['content'][0]['id']
        key_creds = {
            'login': user,
            'password': password,
            'companyId': company_id
        }
        key = requests.post(self.url + 'auth/keys', json=key_creds)
        self.auth_token = key.json()['key']
        self.auth_token = self.auth_token
        return self.auth_token

    def get_project_list(self):
        headers = {
            "Authorization": f"Bearer {self.auth_token}"
        }
        response = requests.get(self.url + 'projects', headers=headers)
        project_list = response.json()
        return project_list['content']

    def create_project(self, title):
        headers = {
            "Authorization": f"Bearer {self.auth_token}"
        }
        project_data = {
            "title": title
        }
        response = requests.post(
            self.url + 'projects', json=project_data, headers=headers
        )
        project_id = response.json()['id']
        self.project_id = project_id
        return self.project_id

    def create_project_unauthorized(self):
        project_data = {
            "title": "Unauthorized Project"
        }
        response = requests.post(self.url + 'projects', json=project_data)
        return response

    def edit_project(self):
        headers = {
            "Authorization": f"Bearer {self.auth_token}"
        }
        edited_data = {
            "deleted": True
        }
        response = requests.put(
            self.url + f"projects/{self.project_id}",
            json=edited_data, headers=headers
        )
        response.raise_for_status()
        return response.json()

    def edit_test_project(self, nonexistent_id):
        headers = {
            "Authorization": f"Bearer {self.auth_token}"
        }
        edited_data = {
            "deleted": True
        }
        response = requests.put(
            self.url + f"projects/{nonexistent_id}",
            json=edited_data, headers=headers
        )
        return response

    def get_project_by_id(self):
        headers = {
            "Authorization": f"Bearer {self.auth_token}"
        }
        response = requests.get(
            self.url + f"projects/{self.project_id}", headers=headers
        )
        response.raise_for_status()
        return response.json()

    def get_project_by_incorrect_id(self, incorrect_id):
        headers = {
            "Authorization": f"Bearer {self.auth_token}"
        }
        response = requests.get(
            self.url + f"projects/{incorrect_id}", headers=headers
        )

        return response
