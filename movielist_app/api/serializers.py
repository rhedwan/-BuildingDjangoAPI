from movielist_app.models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()


    def create(self, validated_data):
        return Movie.objects.create(**validated_data)