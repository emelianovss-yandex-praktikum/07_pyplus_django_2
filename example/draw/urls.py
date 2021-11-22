from django.urls import path

from draw import views

app_name = 'draw'

urlpatterns = [
    path('foreign', views.foreign, name='foreign')
]