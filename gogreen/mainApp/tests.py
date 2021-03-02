from rest_framework.test import APIRequestFactory

# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()

request = factory.get('/http://127.0.0.1:8000/scores?test=Elie', {'user_id' : user})