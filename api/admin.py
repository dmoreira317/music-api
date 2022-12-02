from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Albums)
admin.site.register(Artists)
admin.site.register(Tracks)
admin.site.register(Genres)
admin.site.register(Playlists)
admin.site.register(PlaylistTrack)
