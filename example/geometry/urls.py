from django.urls import path

from geometry import views

app_name = 'geometry'

urlpatterns = [
    path('add/draw/<int:pk>', views.CreateShape.as_view(), name='add-to-draw'),
    path('', views.ListShapes.as_view(), name='index'),
]
