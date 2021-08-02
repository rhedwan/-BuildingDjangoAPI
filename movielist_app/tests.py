from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from movielist_app.api import serializers
from movielist_app import models


class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username = self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(
            name = "Netflix",
            about = "#1 Streaming Platform",
            website = "https://netflix.com"
        )


    def test_streamplatform_create(self):
        data = {
            "name" : "Netflix",
            "about" : "#1 Streaming Platform",
            "website" : "https://netflix.com"
        }

        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail' ,args= (self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
class WatchListTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username = self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(
            name = "Netflix",
            about = "#1 Streaming Platform",
            website = "https://netflix.com"
        )

        self.watchlist = models.WatchList.objects.create(
            title = "Example Movie" ,
            storyline = "Example Story",
            platform = self.stream ,
            active = True
        )

    def test_watchlist_create(self):
        data = {
            "title": "Example Movie" ,
            "storyline": "Example Story",
            "platform" : self.stream ,
            "active" : True
        }
        response = self.client.post(reverse('movie-list') , data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_ind(self):
        response = self.client.get(reverse('movie-detail' ,args= (self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, 'Example Movie')


"""
    IMPORTANT: The we are using the 'user' which isn't the 'admin'. Hence
    it going to return "HTTP_403_FORBIDDEN" which  'ok'

NOTE: Once the request is sent without the authorization. It returns
"HTTP_401_UNAUTHORIZED". 
    The "setUp" method is taking care of that.

NOTE: Once the request is sent without "admin" credentials. It returns
"HTTP_403_FORBIDDEN"

NOTE: "self.stream" is used for creating the "streamplatorm" manually.

NOTE: "test_streamplatform_ind" method is  for getting the individual object
    using the "self.stream" 

    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< WatchListTestCase >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
1. we are using the "setUp" methods again to create a "StreamPlatform" 
    for test we are currently writing. Hence, "each test classes are independent".

2. "self.watchlist" is attribute in the "setUp" for creating the "watchlist" object
    manually.

3. 
"""