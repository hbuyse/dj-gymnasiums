# coding=utf-8

import logging

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from gymnasiums.models import Gymnasium

logger = logging.getLogger(__name__)


@receiver(post_migrate, sender=Gymnasium)
def create_new_group(sender, **kwargs):
    groups_permissions = {
        "gymnasium_staff": [
            'Can add gymnasium',
            'Can change gymnasium',
            'Can delete gymnasium',
            ]
    }
    for key, value in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=k)

        if created:
            for perm_name in value:
                perm = Permission.objects.get(name='Can add gymn')
                group.permissions.add(perm)
