from typing import TYPE_CHECKING
from django import template
from django.conf import settings


if TYPE_CHECKING:
    from geometry.models import Shape


register = template.Library()


@register.inclusion_tag('geometry/shape.html')
def render_shape(shape: 'Shape'):
    radius = 0
    if shape.kind == shape.CIRCLE:
        radius = 50
    return {'radius': radius, 'size': settings.SHAPE_SIZE, 'color': shape.color}
