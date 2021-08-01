from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from user_app.api.serializers import RegistrationSerializer 

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successful"
            data['username'] = account.username
            data['email'] = account.email

            # token = Token.objects.get(user=account).key
            # data['token']= token

            refresh = RefreshToken.for_user(account)
            data['token']= {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

        else:
            data = serializer.errors

        return Response(data)

"""
<<<<<<<< Create Token Automatically &  Return Token With Response >>>>>>>
The token get generated as soon as the "serializer.save()" is instantiated.
1. The "account" is a variable for retrieving and storing all of the return 
value of the "save" method in the "RegistrationSerializer" class.
2. The "data" is a variable for saving the response 
3. The "token" is for retrieving the token for the just registered "User"

<<<<<<<<<<<<<<<<<<<<< JSON Web Token Registration >>>>>>>>>>>>>>>>>>>>>
LINKS: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/creating_tokens_manually.html

Enpoints Used: http://127.0.0.1:8000/account/register/
1. The 'token' was created manually, then stored in the 'refresh' variable.
    The 'access and refesh token' created are also sent as response in JSON
2. Info about the user are gotten from the 'account' which is used in creating the token
"""