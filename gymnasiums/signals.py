# coding=utf-8
"""Django Newsletter signals implementation."""

# Standard library
import logging

# Django
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Current django project
from gymnasiums.models import Gymnasium

logger = logging.getLogger(__name__)


@receiver(post_migrate, sender=Gymnasium)
def create_new_group(sender, **kwargs):
    """Create new group to handle the gymnasium."""
    groups_permissions = {
        "gymnasium_staff": [
            'Can add gymnasium',
            'Can change gymnasium',
            'Can delete gymnasium',
        ]
    }
    for key, value in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=key)

        if created:
            for perm_name in value:
                perm = Permission.objects.get(name='Can add gymn')
                group.permissions.add(perm)
