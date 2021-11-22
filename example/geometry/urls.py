from django.urls import path

from geometry import views

app_name = 'geometry'

urlpatterns = [
    path('', views.index, name='index')
]
