from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """Time Stamped Abstract Definition"""

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True
