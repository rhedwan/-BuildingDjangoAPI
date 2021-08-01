from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path
from user_app.api.views import registration_view, logout_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    # path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

"""
1. The login endpoints will fetch the user token and it returns it while using "POSTMAN"
2. In "POSTMAN" it would be passed via the body/form-data.
The 'username' and 'password' , 'key' and 'value' must be passed respectively

For example: when making the a 'POST' request i.e(http://127.0.0.1:8000/watch/3/review-create/)
The token needs to be passed on the 'headers' as a 'key and value pair'.
i.e {'Authorization' : 'Token fead1ec9fcfb40dce5b8717c3f684c41a974e884'}

3.  The 'logout' endpoint get destroys as soon as the request is made.


<<<<<<<<<<<<<<<< TokenAuthentication >>>>>>>>>>>>>>>>

LINKS: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation,
https://jwt.io/
4. It is passed with the header in the form of "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI3ODA1NDUyLCJqdGkiOiI0NGM1MzQ4YWQ4Mzc0MGY2ODFkOGFmZDE5YzU3YWU2MCIsInVzZXJfaWQiOjF9.0OSKtZ7qxW-pBl2lvVtChpnEWlnEtNzmVfJfVESA_6Q"
where the long code is the JWT access token.
5.  The "access token" last for 5mins. 
6.  The "refresh token" last for 24hours.
7. To regenerate the "access token" this is passed to body/x-www-form-uriencoded/
    in "refresh" : "refresh 'refresh token' " key and value pair.
    on this endpoint "http://127.0.0.1:8000/account/api/token/refresh/" and it will only returns a new
    "access token"
    NOTE: The "refresh token" is stil going to be the same

LINKS: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation
8. To regenerate both the access and refresh token.
"""