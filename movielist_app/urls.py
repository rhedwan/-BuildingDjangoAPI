from  django.urls import __path__
from django.urls.conf import path
from .views import movielist, movie_details

urlpatterns = [
    path('list/', movielist, name='movie_list'),
    path('<int:pk>/', movie_details, name='movie_detail'),
]