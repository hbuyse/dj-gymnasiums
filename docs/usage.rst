=====
Usage
=====

To use Django Newsletter in a project, add it to your `INSTALLED_APPS`:

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
