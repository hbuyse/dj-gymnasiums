"""..."""

from django.contrib import admin

# Register your models here.
from gymnasiums.models import Gymnasium


@admin.register(Gymnasium)
class GymnasiumAdmin(admin.ModelAdmin):
    """Gymnasium admin object."""

    list_display = ('name', 'city')
