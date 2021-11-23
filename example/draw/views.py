from django.forms import ModelForm
from django.shortcuts import render, redirect, reverse

from draw.models import Draw, Album
from django.contrib.auth import get_user_model


User = get_user_model()


def album_list(request):
    return render(
        request,
        'draw/album_list.html',
        {'objects': User.objects.all()}
    )


class DrawForm(ModelForm):
    class Meta:
        model = Draw
        fields = '__all__'


def album_detail(request, pk):
    # Обработка POST запросов, проверка должна быть на метод
    album = Album.objects.get(pk=pk)
    # Обязательно None, т.к. даже при GET запросе здесь пустой QueryDict
    # и Django посчитает что форма не валидная
    form = DrawForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # Важно мы можем добавлять только после создания instance,
            # когда есть id
            form.instance.album_set.add(album)
            return redirect(reverse('draw:albums:detail', kwargs={'pk': pk}))
    return render(
        request,
        'draw/album_detail.html',
        {'object': album, 'form': form}
    )


def draw_detail(request, pk):
    return render(
        request,
        'draw/draw_detail.html',
        {'object': Draw.objects.get(pk=pk)}
    )
