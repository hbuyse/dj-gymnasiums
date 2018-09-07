#!/usr/bin/env python
# coding=utf-8

"""Tests for `dj-gymnasiums` urls module."""

from django.test import TestCase
from django.urls import reverse


class TestUrlsPost(TestCase):
    """Tests the urls for the dj-gymnasiums."""

    def test_post_list_url(self):
        """Test the URL of the listing of posts."""
        url = reverse('dj_gymnasiums:list')
        self.assertEqual(url, '/')

    def test_post_create_url(self):
        """Test the URL of that allows the creation of a post."""
        url = reverse('dj_gymnasiums:create')
        self.assertEqual(url, '/create')

    def test_post_detail_url(self):
        """Test the URL that gives the details of a post."""
        url = reverse('dj_gymnasiums:detail', kwargs={'pk': 1})
        self.assertEqual(url, '/1')

    def test_post_update_url(self):
        """Test the URL of the listing of posts."""
        url = reverse('dj_gymnasiums:update', kwargs={'pk': 1})
        self.assertEqual(url, "/1/update")

    def test_post_delete_url(self):
        """Test the URL of the listing of posts."""
        url = reverse('dj_gymnasiums:delete', kwargs={'pk': 1})
        self.assertEqual(url, "/1/delete")
