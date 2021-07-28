from django.urls.conf import path

# NB: function based view
# from movielist_app.api.views import movie_list, movie_details

from movielist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformListAV , StreamPlatformDetailAV

urlpatterns = [
    # path('list/', movie_list, name='movie_list'),
    # path('<int:pk>/', movie_details, name='movie_detail'),
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='platform_detail'),
]