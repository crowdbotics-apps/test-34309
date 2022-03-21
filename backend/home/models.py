from django.conf import settings
from django.db import models


class SubUser(models.Model):
    "Generated Model"
    surname = models.CharField(
        max_length=256,
    )
