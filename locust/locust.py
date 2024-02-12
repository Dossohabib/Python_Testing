from locust import HttpUser, between, task

class UserBehavior(HttpUser):
    wait_time = between(5, 15)

    @task
    def index_page(self):
        self.client.get("/")

    @task
    def show_summary(self):
        self.client.post("/showSummary", data={'email': 'john@simplylift.co'})

    @task
    def book_competition(self):
        self.client.get("/book/Spring%20Festival/Simply%20Lift")

    @task
    def purchase_places(self):
        self.client.post("/purchasePlaces", data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '5'})
