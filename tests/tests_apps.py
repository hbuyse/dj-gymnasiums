#!/usr/bin/env python
# coding=utf-8

"""
test_dj-sponsoring
------------

Tests for `dj-sponsoring` apps module.
"""

from gymnasiums.apps import GymnasiumsConfig

from django.apps import apps
from django.test import TestCase


class TestApps(TestCase):

    def test_apps(self):
        self.assertEqual(GymnasiumsConfig.name, 'gymnasiums')
        self.assertEqual(apps.get_app_config('gymnasiums').name, 'gymnasiums')
