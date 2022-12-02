# Django
from .models import *

# Django Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
from rest_framework import viewsets


# Create your views here.
class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all().order_by("artistid")
    serializer_class = ArtistsSerializer

    @action(detail=True, methods=['get'])
    def get_artist_albums(self, request, pk=None):
        """
        Function to filter the Albums by Artist Id
        :param queryset: (QuerySet <Albums>) The queryset to filter
        :param pk: (int) Artist Id to filter queryset
        :param request: Client request context
        :return: (QuerySet <Albums>) The filtered queryset
        """
        queryset = Albums.objects.filter(artistid=pk)
        res = []
        for album in queryset:
                serializer = AlbumsSerializer(album, context={'request': request})
                res.append(serializer.data)
        return Response(res)


class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Albums.objects.all().order_by("albumid")
    serializer_class = AlbumsSerializer

    @action(detail=True, methods=['get'])
    def get_album_tracks(self, request, pk=None):
        """
        Function to filter the Tracks by Album Id
        :param queryset: (QuerySet <Tracks>) The queryset to filter
        :param pk: (int) Album Id to filter queryset
        :param request: Client request context
        :return: (QuerySet <Tracks>) The filtered queryset
        """
        queryset = Tracks.objects.filter(albumid=pk)
        res = []
        for track in queryset:
                serializer = TracksSerializer(track, context={'request': request})
                res.append(serializer.data)
        return Response(res)


class AlbumsArtistsTracksViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumsArtistsTracksSerializer

    def get_queryset(self):
        queryset = Albums.objects.all().order_by("albumid")
        return queryset


class TracksViewSet(viewsets.ModelViewSet):
    queryset = Tracks.objects.all()
    serializer_class = TracksSerializer


class MediaTypesViewSet(viewsets.ModelViewSet):
    queryset = MediaTypes.objects.all()
    serializer_class = MediaTypesSerializer


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


# This works even with raw queries!
#from django.db import connection
#import sqlite3
# def my_custom_sql(query):
#     connection = sqlite3.connect("chinook.db")
#     results = connection.cursor().execute(query).fetchall()
#     return results
# class ArtistsViewSet(viewsets.ModelViewSet):
#     serializer_class = ArtistsSerializer
#     def get_queryset(self):
#         query = """
#                 SELECT ArtistId, Name FROM artists
#             """
#         queryset = list(my_custom_sql(query))
#         return queryset