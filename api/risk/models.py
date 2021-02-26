from django.db import models


class Risk(models.Model):
    """A Model that defines the representation of a Risk"""

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "risk"
