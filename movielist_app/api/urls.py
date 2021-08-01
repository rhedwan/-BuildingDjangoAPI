from django.urls import include, path

# NB: function based view
# from movielist_app.api.views import movie_list, movie_details
from movielist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformListAV , StreamPlatformDetailAV, StreamPlatformVS, ReviewList, ReviewDetail, ReviewCreate, UserReview

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    # path('list/', movie_list, name='movie_list'),
    # path('<int:pk>/', movie_details, name='movie_detail'),
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),

    path('', include(router.urls)),

    # path('stream/', StreamPlatformListAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    # path('review/', ReviewList.as_view(), name='review'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),  
    path('reviews/<str:username>/', UserReview.as_view(), name='user-review-detail'),  
]
 
"""

LINKS: https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer
views-url name was changed because:
By default hyperlinks are expected to correspond to a view name that matches the style 
'{model_name}-detail', and looks up the instance by a pk keyword argument. 
HENCE: Our model name was 'streamplatform'. That why it now 'streamplatform-detail'

"""