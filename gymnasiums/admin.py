"""..."""

# Django
from django.contrib.admin import ModelAdmin

# Current django project
from gymnasiums.models import Gymnasium


@admin.register(Gymnasium)
class GymnasiumAdmin(ModelAdmin):
    """Gymnasium admin object."""

    list_display = ('name', 'city')
