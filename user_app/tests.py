from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class RegisterTestCase(APITestCase):

    def test_register(self):

        data = {
            "username": "testcase",
            "email": "testcase@example.com",
            "password": "NewPassword@123"
        }

        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)






"""  
LINKS: https://www.django-rest-framework.org/api-guide/testing/, 
https://github.com/encode/django-rest-framework/blob/master/rest_framework/test.py

1. The 'client' are from the 'APITestCase'. We use it to send 'POST' case. 
2. The 'reverse' helps us target our endpoint
3. The methods needs to start with 'test_'
4. "setUp()" - This method is called before the invocation of each test method 
    in the given class.
5. "tearDown()"- This method is called after the invocation of each test method 
    in given class. 
6. The 'self.client.post(reverse('register'), data)' returns a response. Which can be stored
7. NOTE: The "self.assertEqual" is for checking if there are equal
8. NOTE: By default it returns "status.HTTP_200_OK"
"""