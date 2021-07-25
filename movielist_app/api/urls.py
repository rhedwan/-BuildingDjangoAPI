from django.urls.conf import path
from movielist_app.api.views import movie_list, movie_details

urlpatterns = [
    path('list/', movie_list, name='movie_list'),
    path('<int:pk>/', movie_details, name='movie_detail'),
]