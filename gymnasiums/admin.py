"""..."""

# Django
from django.contrib import admin

# Current django project
from gymnasiums.models import Gymnasium


@admin.register(Gymnasium)
class GymnasiumAdmin(admin.ModelAdmin):
    """Gymnasium admin object."""

    list_display = ('name', 'city')
