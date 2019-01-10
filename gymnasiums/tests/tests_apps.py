#!/usr/bin/env python
# coding=utf-8

"""
test_dj-sponsoring
------------

Tests for `dj-sponsoring` apps module.
"""

from gymnasiums.apps import DjGymnasiumsConfig

from django.apps import apps
from django.test import TestCase


class TestApps(TestCase):

    def test_apps(self):
        self.assertEqual(DjGymnasiumsConfig.name, 'gymnasiums')
        self.assertEqual(apps.get_app_config('gymnasiums').name, 'gymnasiums')
