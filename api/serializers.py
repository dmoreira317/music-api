# Modules
from .models import *

# Django Rest Framework
from rest_framework import serializers
from rest_framework import response


class ArtistsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artists
        fields = "__all__"


class AlbumsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Albums
        fields = ("albumid", "title", "artistid", "tracks")
        depth=1


class TracksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tracks
        fields = ("trackid", "name", "albumid", "mediatypeid", "genreid", "composer", "milliseconds", "bytes", "unitprice")


class AlbumsArtistsTracksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Albums
        fields = "__all__"

    artist_name = serializers.SerializerMethodField('get_artist_name')
    tracks_count = serializers.SerializerMethodField('get_tracks_count')

    def get_artist_name(self, album):
        artist = Artists.objects.get(artistid=album.artistid.artistid)
        album.artist_name = artist.name
        #print(artist.name)
        return album.artist_name
    
    def get_tracks_count(self, album):
        track_count = Tracks.objects.filter(albumid=album.albumid).count()
        return track_count


class MediaTypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MediaTypes
        fields = "__all__"


class GenresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genres
        fields = "__all__"

# This works even with raw queries!
# class ArtistsSerializer(serializers.Serializer):
#     """ Get a list of artists."""
#     ArtistId = serializers.SerializerMethodField()
#     Name = serializers.SerializerMethodField()
    
#     def get_ArtistId(self, obj):
#         return obj[0]
    
#     def get_Name(self, obj):
#         return obj[1]