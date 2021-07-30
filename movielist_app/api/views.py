from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from movielist_app.models import WatchList , StreamPlatform , Review
from movielist_app.api.serializers import WatchListSerializer , StreamPlatformSerializer,ReviewSerializer

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        serializer.save(watchlist = watchlist)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

""" class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) """

class StreamPlatformVS(viewsets.ViewSet):

    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(watchlist)
        return Response(serializer.data)

    def create(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformListAV(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True,context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'Platform not found'}, status = status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





""" @api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
 """

"""  
1. It is also very important to pass the id of item to be updated, when making a "PUT" request
else a new model get created.
2. The data we are using after checking it "is_vald()" is from the return statement
in create method in the MovieSerializer

LINKS: https://www.django-rest-framework.org/api-guide/generic-views/#listmodelmixin
3. 'mixins.ListModelMixin' is similar to the 'get request'
4. 'mixins.CreateModelMixin' is similar to the 'create request' i.e 
it implements creating and saving a new model instance

5. 'generics.GenericAPIView' is used for building the 2 
NOTE: The the mixins subclasses go in hand with the 'generics.GenericAPIView'

LINKS: https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-generic-class-based-views ,
https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes
6. The Concrete View Classes (i.e using the generics only) are inherited from the 'mixins' Classes.
READ MORE: https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< SAVING OF REVIEW FOR A VIDEO INNSTANCE /Overwriting Querset  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LINKS: https://www.django-rest-framework.org/api-guide/generic-views/#api-reference
7. 'perform_create(self, serializer)' method is Called by CreateModelMixin when saving a new object instance.
it is use here for saving the 'watchlist' id. i.e the id/pk of the video which we are creating the review for.
NOTE: The to avoid errors the "fields = '__all__'" needs to exclude the watchlist, hence: "exclude = ['watchlist']"

8. 'watchlist' variable in the 'perform_create(self, serializer)' is for getting the id of the videos(i.e the /<int:pk>/ in endpoint) 


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ViewSets & Routers  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

LINKS: https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/,
https://www.django-rest-framework.org/api-guide/viewsets/#viewset

9. The 'ViewSets & Routers' saves a lot of energy by creating our urls for us automatically. Depending on the methods available in it.

"""