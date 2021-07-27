from re import escape
from movielist_app.models import Movie
from rest_framework import serializers

def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short")


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()


    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()

        return instance

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description should be different")
        return data

    """ def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value """



  


""" 
def update(self, instance, validated_data):
        return super().update(instance, validated_data)
1. The instaance is the old value in the database
2. The validated_data is the new value currently been worked on by the user.

<<<The Documentation to this is available on the Serializers Page on DRF>>>
LINKS: https://www.django-rest-framework.org/api-guide/serializers/#validation

3. The method 'validate_name' is a field level validation. It is used for checking
a particular field. 
4. The 'validate' method is an Object-level validation. It is used for checking
and comparing field in that model.
5. The 'name_length' is a function it is a Validators. It is used for checking
a individual field. 

LINKS: https://www.django-rest-framework.org/api-guide/fields/
6. This is the Core arugment for serailizers i.e the EmailField, CharField, Boolean,
IP Address field etc 
"""