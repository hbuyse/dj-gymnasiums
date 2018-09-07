#!/usr/bin/env python
# coding=utf-8

"""Tests for `dj-gymnasiums` models module."""

from dj_gymnasiums.models import Gymnasium

from django.test import TestCase


class TestGymnasiumModel(TestCase):
    """Test post class model."""

    def setUp(self):
        """Setup function."""
        self.dict = {
            'name': 'Watteau',
            'address': '37 rue Lequesne',
            'city': 'Nogent-Sur-Marne',
            'zip_code': '94130',
            'phone': '0100000000',
            'surface': '123',
            'capacity': '456',
        }

    def test_string_representation(self):
        """Test the string representation of the post model."""
        g = Gymnasium(**self.dict)
        self.assertEqual(str(g), "Gymnasium {}".format(g.name))

    def test_verbose_name(self):
        """Test the verbose name in singular."""
        self.assertEqual(str(Gymnasium._meta.verbose_name), "gymnasium")

    def test_verbose_name_plural(self):
        """Test the verbose name in plural."""
        self.assertEqual(str(Gymnasium._meta.verbose_name_plural), "gymnasiums")
