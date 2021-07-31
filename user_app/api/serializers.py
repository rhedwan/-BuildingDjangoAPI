from django.contrib.auth.models import User

from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only' : True}
        }
    
    def save(self, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'Error': 'Password and Password Confirm should be same'})
        
        if User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({'Error': 'Email already exists!.'})

        account = User(email = self.validated_data['email'], username = self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account


""" 
1. The 'save' method is used for creating a new user and registration mechanisms i.e 
    a. To check if the password and password2 are the same
    b. Also the second conditionals are used for avoiding registering multiple accounts with
    same 'email' address.

2. The 'password = self.validated_data['password']'
    NOTE:  The "self.validated_data" is gotten from the instantiated serializers class in the view function 
    i.e "registration_view"

3. The account is kind of a mannual saving of Users that have fullfilled all the criteria. Using the "validated_data"
    NOTE: The 'token' is generated only when the new user 'login'.
"""