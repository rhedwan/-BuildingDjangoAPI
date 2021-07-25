from movielist_app.models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
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

  


""" 
def update(self, instance, validated_data):
        return super().update(instance, validated_data)
1. The instaance is the old value in the database
2. The validated_data is the new value currently been worked on by the user.
"""