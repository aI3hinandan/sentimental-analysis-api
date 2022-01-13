import django.db.models
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from django.db import models
from django.db.models import CharField, TextField


class FollowList(models.Model):
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            null=False,
        )
    followList = TextField(
        null=True
    )

    def __str__(self):
        """A string representation of the model."""
        return str(self.user)