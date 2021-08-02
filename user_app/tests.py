from django.contrib.auth.models import User
from django.http import response
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


class LoginLogoutTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username = "example", password="NewPassword@123")

    def test_login(self):
        data = {
            "username": "example",
            "password": "NewPassword@123"
        }
    
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username = "example")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


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

LINKS : https://www.django-rest-framework.org/api-guide/status-codes/

8. NOTE: By default it returns "status.HTTP_200_OK"
9. NOTE: If the 'password or username' isn't correct it returns "HTTP_400_BAD_REQUEST" (i.e the response returns that)
"""