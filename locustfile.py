from locust import HttpUser, task, between

class PetstoreUser(HttpUser):
    wait_time = between(1, 3)  # wait between 1 to 3 seconds between tasks

    @task(1)
    def get_pet_by_id(self):
        self.client.get("/pet/1")

    @task(1)
    def find_pets_by_status(self):
        self.client.get("/pet/findByStatus", params={"status": "available"})

