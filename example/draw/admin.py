from django.contrib import admin
from draw.models import Draw, Album


@admin.register(Draw)
class AdminDraw(admin.ModelAdmin):
    ...


@admin.register(Album)
class AdminAlbum(admin.ModelAdmin):
    ...
