from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hi(models.Model):
    message = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    hi = models.CharField(
        default="hi",
        editable="False",
        max_length=200,
        blank=False,
        null=False,
    )
    sender = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    timestamp = models.DateTimeField(
        auto_now=True,
    )
