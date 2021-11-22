from django.shortcuts import render

from draw.models import Draw


def foreign(request):
    return render(request, 'draw/foreign.html', {'objects': Draw.objects.all()})