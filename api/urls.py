from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'artists', ArtistsViewSet)
router.register(r'albums', AlbumsViewSet)
router.register(r'albums_info', AlbumsArtistsTracksViewSet, basename='albums_extra_info')
router.register(r'tracks', TracksViewSet)
router.register(r'media_types', MediaTypesViewSet)
router.register(r'genres', GenresViewSet)

# This works even with raw queries!
# router.register(r'artists', ArtistsViewSet, basename='Artist')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]