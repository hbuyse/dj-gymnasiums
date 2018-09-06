=============================
Django Newsletter
=============================

.. image:: https://gitlab.com/hbuyse/dj-gymnasiums/badges/dev/build.svg
    :target: https://gitlab.com/hbuyse/dj-gymnasiums

.. image:: https://gitlab.com/hbuyse/dj-gymnasiums/badges/dev/coverage.svg
    :target: https://gitlab.com/hbuyse/dj-gymnasiums

.. image:: https://codecov.io/gh/hbuyse/dj-gymnasiums/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/hbuyse/dj-gymnasiums

Django Newsletter for django

Documentation
-------------

The full documentation is at https://dj-gymnasiums.readthedocs.io.

Quickstart
----------

Install Django Newsletter::

    pip install dj-gymnasiums

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_gymnasiums.apps.DjNewsletterConfig',
        ...
    )

Add Django Newsletter's URL patterns:

.. code-block:: python

    from dj_gymnasiums import urls as dj_gymnasiums_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_gymnasiums_urls)),
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

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
