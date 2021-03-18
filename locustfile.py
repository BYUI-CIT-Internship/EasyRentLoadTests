from locust import HttpUser, task, between
class WebsiteTestUser(HttpUser):
  wait_time = between(0.5, 3.0)
  def on_start(self):
    pass

  def on_stop(self):
    pass

  @task(1)
  def hello_world(self):
    self.client.get("https://easyrent-api-dev.cit362.com/reservations")

  @task(2)
  def index(self):
    self.client.get("https://easyrent-api-dev.cit362.com/customer")

  @task(4)
  def post(self):
    self.client.post("https://easyrent-api-dev.cit362.com/login", '{"userName": "test@test125.com","password":"Test@test123"}')

  @task(3)
  def post(self):
    self.client.post("https://easyrent-api-dev.cit362.com/reservations", """{
        "customerId": "test@test124.com",
        "reservationItems": [
            {
                "description": "Canoe",
                "itemId": 4949489,
                "returned": 'false'
            },
            {
                "description": "Paddle",
                "itemId": 4949491,
                "returned": 'true'
            },
            {
                "description": "LifeJacket",
                "itemId": 4949488,
                "returned": 'false'
            }
        ],
        "dueDate": 1610148694321
    }"""                                                               
   )
