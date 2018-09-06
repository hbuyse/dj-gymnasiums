#!/usr/bin/env python
# coding=utf-8

"""
test_dj-sponsoring
------------

Tests for `dj-sponsoring` apps module.
"""

from dj_gymnasiums.apps import DjNewsletterConfig

from django.apps import apps
from django.test import TestCase


class TestApps(TestCase):

    def test_apps(self):
        self.assertEqual(DjNewsletterConfig.name, 'dj_gymnasiums')
        self.assertEqual(apps.get_app_config('dj_gymnasiums').name, 'dj_gymnasiums')
