from django.urls.conf import path

# NB: function based view
# from movielist_app.api.views import movie_list, movie_details

from movielist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformListAV , StreamPlatformDetailAV, ReviewList, ReviewDetail

urlpatterns = [
    # path('list/', movie_list, name='movie_list'),
    # path('<int:pk>/', movie_details, name='movie_detail'),
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    # path('review/', ReviewList.as_view(), name='review'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),  
]
 
"""

LINKS: https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer
views-url name was changed because:
By default hyperlinks are expected to correspond to a view name that matches the style 
'{model_name}-detail', and looks up the instance by a pk keyword argument. 
HENCE: Our model name was 'streamplatform'. That why it now 'streamplatform-detail'

"""