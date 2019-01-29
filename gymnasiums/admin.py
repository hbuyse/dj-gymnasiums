"""..."""

# Django
from django.contrib.admin import ModelAdmin, register

# Current django project
from gymnasiums.models import Gymnasium


@register(Gymnasium)
class GymnasiumAdmin(ModelAdmin):
    """Gymnasium admin object."""

    list_display = ('name', 'city')
