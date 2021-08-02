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


class ReviewTestCase(APITestCase):

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

        self.watchlist2 = models.WatchList.objects.create(
            title = "Example Movie" ,
            storyline = "Example Story",
            platform = self.stream ,
            active = True
        )

        self.review = models.Review.objects.create(
            review_user =self.user ,
            rating  = 5,
            description = "Great Movie!!!",
            watchlist = self.watchlist2,
            active  = True
        )

    def test_review_create(self):
        data = {
            "review_user": self.user ,
            "rating " : 5,
            "description" : "Great Movie!!!",
            "watchlist" : self.watchlist,
            "active" : True
        }
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Added more checks to the tests. i.c(For the content and
        #  the number of reviews that can be created on a movie)
        self.assertEqual(models.Review.objects.count(), 2)

        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_review_create_unauth(self):
        data = {
            "review_user": self.user ,
            "rating " : 5,
            "description" : "Great Movie!!!",
            "watchlist" : self.watchlist,
            "active" : True
        }

        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_create_update(self):
        data = {
            "review_user": self.user ,
            "rating " : 4,
            "description" : "Great Movie!!!-(Updated)",
            "watchlist" : self.watchlist,
            "active" : False
        }
        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


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

    ----------------------- Forcing authentication-------------------------
    LINKS: https://www.django-rest-framework.org/api-guide/testing/#forcing-authentication

3. We are "Forcing authentication" to login as anonymous
4. Created a "self.watchlist" attribute to get an id for the review to be updated.
    NOTE: The 2 'self.watchlist' i.e('self.watchlist & self.watchlist2') was created because
     we aren't allowed to send multilpe review on a watchlist. 
     The first is used to test the "test_review_create and test_review_create_unauth"
    While, the second is used to for the update, "PUT"
"""