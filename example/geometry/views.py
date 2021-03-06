from django.urls import reverse

from geometry.models import Shape
from django.views.generic import CreateView, ListView


class ListShapes(ListView):
    # Или queryset или get_query_set
    queryset = Shape.objects.order_by('id')


class CreateShape(CreateView):
    # Или модель
    model = Shape
    fields = ['color', 'kind']

    def get_success_url(self):
        return reverse('draw:detail', kwargs=self.kwargs)

    def form_valid(self, form):
        # Тут мы покажем как можно переопределив какой-то маленький кусок
        # изменить поведение
        form.instance.draw_id = self.kwargs['pk']
        return super().form_valid(form)
