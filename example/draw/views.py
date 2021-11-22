from django.shortcuts import render

from draw.models import Draw, Album
from django.contrib.auth import get_user_model


User = get_user_model()


def album_list(request):
    return render(
        request,
        'draw/album_list.html',
        {'objects': User.objects.all()}
    )


def album_detail(request, pk):
    return render(
        request,
        'draw/album_detail.html',
        {'object': Album.objects.get(pk=pk)}
    )


def draw_detail(request, pk):
    return render(
        request,
        'draw/draw_detail.html',
        {'object': Draw.objects.get(pk=pk)}
    )
