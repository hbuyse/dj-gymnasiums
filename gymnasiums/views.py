# coding=utf-8

"""Views."""

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from gymnasiums.models import (
    Gymnasium
)


class GymnasiumListView(ListView):
    """View that returns the list of Gymnasiums."""

    model = Gymnasium
    paginate_by = 10


class GymnasiumDetailView(DetailView):
    """Show the details of a Gymnasium."""

    model = Gymnasium


class GymnasiumCreateView(CreateView):
    """Create a Gymnasium."""

    model = Gymnasium
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        """."""
        if True not in [request.user.is_superuser, request.user.is_staff]:
            raise PermissionDenied

        return super().get(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        """."""
        if True not in [request.user.is_superuser, request.user.is_staff]:
            raise PermissionDenied

        return super().post(request, args, kwargs)

    def get_success_url(self):
        """Get the URL after the success."""
        messages.success(self.request, "Gymnasium '{}' added successfully".format(self.object.name))
        return reverse('gymnasiums:detail', kwargs={'pk': self.object.id})


class GymnasiumUpdateView(UpdateView):
    """Update a Gymnasium."""

    model = Gymnasium
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        """."""
        if True not in [request.user.is_superuser, request.user.is_staff]:

            raise PermissionDenied

        return super().get(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        """."""
        if True not in [request.user.is_superuser, request.user.is_staff]:
            raise PermissionDenied

        return super().post(request, args, kwargs)

    def get_success_url(self):
        """Get the URL after the success."""
        messages.success(self.request, "Gymnasium '{}' updated successfully".format(self.object.name))
        return reverse('gymnasiums:detail', kwargs={'pk': self.object.id})


class GymnasiumDeleteView(DeleteView):
    """View that allows the deletion of a Gymnasium."""

    model = Gymnasium

    def get(self, request, *args, **kwargs):
        """."""
        if True not in [request.user.is_superuser, request.user.is_staff]:
            raise PermissionDenied

        return super().get(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        """."""
        if True not in [request.user.is_superuser, request.user.is_staff]:
            raise PermissionDenied

        return super().post(request, args, kwargs)

    def get_success_url(self, **kwargs):
        """Get the URL after the success."""
        messages.success(self.request, "Gymnasium '{}' deleted successfully".format(self.object.name))
        return reverse('gymnasiums:list')
