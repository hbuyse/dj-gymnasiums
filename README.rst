=============================
Django Newsletter
=============================

.. image:: https://travis-ci.org/hbuyse/dj-gymnasiums.svg?branch=master
    :target: https://travis-ci.org/hbuyse/dj-gymnasiums

.. image:: https://codecov.io/gh/hbuyse/dj-gymnasiums/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/hbuyse/dj-gymnasiums

Django Newsletter for the VCN club

Quickstart
----------

Install Django Newsletter::

    pip install git+https://github.com/hbuyse/dj-gymnasiums@master

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'gymnasiums',
        ...
    )

Add Django Newsletter's URL patterns:

.. code-block:: python

    from gymnasiums import urls as gymnasiums_urls


    urlpatterns = [
        ...
        url(r'^', include(gymnasiums_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox
