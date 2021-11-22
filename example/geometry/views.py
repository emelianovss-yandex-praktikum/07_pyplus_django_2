from django.shortcuts import render

from geometry.models import Shape


def index(request):
    objects = Shape.objects.order_by('id')
    return render(request, 'geometry/shapes_list.html', {'objects': objects})
