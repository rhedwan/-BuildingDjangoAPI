from re import T
from django.db import models
from django.db.models import fields
from movielist_app.models import WatchList , StreamPlatform
from rest_framework import serializers


class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['active']

    
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'


""" def name_length(value):
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

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value

 """

  


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

LINKS:  https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
7. The exclude save the listing a specified fields
8. The fields take both list,[] and tuple,() i.e ('id', 'name', 'description')

Custom Serializers Fields
LINKS: https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
9. "get_len_name" is the custom method for accesing the models in the database.
10. The "object" has access to everything in the database model field.


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< SERIALIZERS RELATIONS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


LINKS: https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
11. The class attribute 'watchlist' is from the related_name set in the model.
12. Many is set to 'True' because it A Streaming platform can have many/severals video attached to it.
13. The "WatchListSerializer(many=True, read_only=True)" returns all the fields of the models associated with it.
i.e It returns all the attribute/fields of the video.

LINKS: https://www.django-rest-framework.org/api-guide/relations/#stringrelatedfield
14. "serializers.StringRelatedField(many=True)" returns the string representations "__str__"

LINKS: https://www.django-rest-framework.org/api-guide/relations/#primarykeyrelatedfield
15. "serializers.PrimaryKeyRelatedField(many=True, read_only=True)" returns the pk or id of the movie assocaited with it.

LINKS: https://www.django-rest-framework.org/api-guide/relations/#hyperlinkedrelatedfield
16. "serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie-detail'
    )"
This return the links of each movies associated with it. Where "'movie-detail'" is the url name in the urls.py.
Also, the "context={'request': request}" must be passed into the "StreamPlatformSerializer" class in the view.

"   watchlist = serializers.StringRelatedField(many=True)
    watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie-detail')
"
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< HyperlinkedModelSerializer  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LINKS: https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer
17. The "HyperlinkedModelSerializer" uses the "url" while  the "ModelSerializer" uses the "id"
18. Also, the "context={'request': request}" must be passed into the "StreamPlatformSerializer" class in the views.py 
for the lising of each stream platform.
19. Also, the "context={'request': request}" must be passed into the "StreamPlatformDetailAV" class in the views.py
for the clicking of each stream platform to work.

"""