from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
]

"""
1. The login endpoints will fetch the user token and it returns it while using "POSTMAN"
2. In "POSTMAN" it would be passed via the body/form-data.
The 'username' and 'password' , 'key' and 'value' must be passed respectively

For example: when making the a 'POST' request i.e(http://127.0.0.1:8000/watch/3/review-create/)
The token needs to be passed on the 'headers' as a 'key and value pair'.
i.e {'Authorization' : 'Token fead1ec9fcfb40dce5b8717c3f684c41a974e884'}

"""