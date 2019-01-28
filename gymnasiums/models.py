# -*- coding: utf-8 -*-
"""Django Newsletter model implementation."""

# Django
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _  # noqa


class Gymnasium(models.Model):
    """User model for the website."""

    name = models.CharField(_('name'), max_length=128)
    address = models.CharField(_('address'), max_length=255)
    city = models.CharField(_('city'), max_length=255)
    zip_code = models.IntegerField(_('zip code'))
    phone = models.CharField(
        _('phone number'),
        max_length=10,
        blank=True,
        validators=[
            # ^
            #     (?:(?:\+|00)33|0)     # Dialing code
            #     \s*[1-9]              # First number (from 1 to 9)
            #     (?:[\s.-]*\d{2}){4}   # End of the phone number
            # $
            RegexValidator(regex=r"^(?:(?:\+|00)33|0)\s*[1-7,9](?:[\s.-]*\d{2}){4}$",
                           message=_("This is not a correct phone number"))
        ]
    )
    surface = models.SmallIntegerField(_('surface'), blank=True, null=True)
    capacity = models.SmallIntegerField(_('capacity'), blank=True, null=True)

    def __str__(self):
        """Representation of a Gymnasium as a string."""
        return "Gymnasium {}".format(self.name)

    class Meta:
        verbose_name = _("gymnasium")
        verbose_name_plural = _("gymnasiums")
        ordering = ("name", "city")
