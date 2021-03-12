import random

from locust import HttpUser, task, between

from locust_project.utils import get_links
from locust_project.settings import Settings


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    def __init__(self, *args, **kwargs):
        super(QuickstartUser, self).__init__(*args, **kwargs)
        self.settings = Settings()
        self.links = set()
        self.user = random.choice(self.settings.list_usernames)

    def on_start(self):
        if self.settings.login_enable:
            self.login()
        response = self.client.get("/")
        if response.status_code == 200:
            self.links.update(get_links(response.content))

    def on_stop(self):
        if self.settings.login_enable:
            self.logout()

    def login(self):
        auth = {
            self.settings.username_parameter_name: self.user,
            self.settings.password_parameter_name: self.settings.user_password_default
        }
        self.client.post(self.settings.login_url, auth)

    def logout(self):
        auth = {
            self.settings.username_parameter_name: self.user,
            self.settings.password_parameter_name: self.settings.user_password_default
        }
        self.client.post(self.settings.logout_url, auth)

    @task
    def index(self):
        self.client.get("/")

    @task
    def random_link(self):
        try:
            link = random.choice(tuple(self.links))
            response = self.client.get(link)
            if response.status_code == 200:
                self.links.update(get_links(response.content))
        except IndexError:
            pass
