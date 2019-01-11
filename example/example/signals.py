import logging

from django.db.models.signals import pre_save
from django.dispatch import receiver
from gymnasiums.models import Gymnasium

logger = logging.getLogger(__name__)


@receiver(pre_save, sender=Gymnasium)
def gymnasium_pre_save_logger(sender, **kwargs):
    logger.info("Receive pre_save Gymnasium")
