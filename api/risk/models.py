from django.db import models


class Risk(models.Model):
    """A Model that defines the representation of a Risk"""

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "risk"


class RiskFieldType(models.Model):
    """A Model that represents the type of a Field of a Risk"""

    name = models.CharField(max_length=128)
    code = models.CharField(max_length=64)

    class Meta:

        db_table = "risk_field_type"


class RiskField(models.Model):
    """A Model that defines the representation of a Field of a Risk"""

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "risk_field"
