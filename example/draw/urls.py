from django.urls import path, include

from draw import views

app_name = 'draw'

albums_urls = ([
    path('', views.album_list, name='list'),
    path('<int:pk>', views.album_detail, name='detail'),
], 'albums')

urlpatterns = [
    path('albums/', include(albums_urls)),
    path('<int:pk>', views.draw_detail, name='detail')
]
