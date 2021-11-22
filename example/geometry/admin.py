from django.contrib import admin
from geometry.models import Shape


@admin.register(Shape)
class AdminShape(admin.ModelAdmin):
    ...
