from locust import HttpLocust
from locust import TaskSet
from locust import task


class MainTaskSet(TaskSet):
    @task(1)
    def api_all_pair_status(self):
        self.client.get("/api/all_status/")


class MyLocust(HttpLocust):
    task_set = MainTaskSet
    min_wait = 5000
    max_wait = 15000
