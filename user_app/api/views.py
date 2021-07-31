from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

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
            token = Token.objects.get(user=account).key

            data['token']= token

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
"""