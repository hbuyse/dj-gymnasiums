#!/usr/bin/env python
# coding=utf-8

"""
test_dj-sponsoring
------------

Tests for `dj-sponsoring` apps module.
"""

# Django
from django.apps import apps
from django.test import TestCase

# Current django project
from gymnasiums.apps import GymnasiumsConfig


class TestApps(TestCase):

    def test_apps(self):
        self.assertEqual(GymnasiumsConfig.name, 'gymnasiums')
        self.assertEqual(apps.get_app_config('gymnasiums').name, 'gymnasiums')
