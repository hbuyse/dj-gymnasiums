# -*- coding: utf-8 -*-
"""Django Newsletter model implementation."""

from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Gymnasium(models.Model):
    """User model for the website."""

    name = models.CharField(_('Gymnasium name'), max_length=128)
    address = models.CharField(_('Gymnasium address'), max_length=255)
    city = models.CharField(_('Gymnasium city'), max_length=255)
    zip_code = models.IntegerField(_('Gymnasium zip code'))
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
            RegexValidator(regex="^(?:(?:\+|00)33|0)\s*[1-7,9](?:[\s.-]*\d{2}){4}$",
                           message=_("This is not a correct phone number"))
        ]
    )
    surface = models.SmallIntegerField(_('gymnasium surface'), blank=True, null=True)
    capacity = models.SmallIntegerField(_('gymnasium capacity'), blank=True, null=True)

    def __str__(self):
        """String representation."""
        return "Gymnasium {}".format(self.name)

    class Meta:
        """Meta class."""

        verbose_name = _("VCN account")
        verbose_name_plural = _("VCN accounts")
        ordering = ("name", "city")
