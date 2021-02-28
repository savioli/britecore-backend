from django.db import models


class RiskFieldType(models.Model):
    """A Model that represents the type of a Field of a Risk"""

    name = models.CharField(max_length=128)
    code = models.CharField(max_length=64, unique=True)

    class Meta:

        db_table = "risk_field_type"


class RiskField(models.Model):
    """A Model that defines the representation of a Field of a Risk"""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    required = models.BooleanField(default=False)

    risk_field_type = models.ForeignKey(RiskFieldType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "risk_field"


class RiskCategory(models.Model):
    """A Model that represents a Category of a Risk"""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    code = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "risk_category"


class Risk(models.Model):
    """A Model that defines the representation of a Risk"""

    name = models.CharField(max_length=128)

    risk_category = models.ForeignKey(RiskCategory, on_delete=models.CASCADE)
    risk_fields = models.ManyToManyField(RiskField, through="RiskRiskField")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "risk"


class RiskRiskField(models.Model):
    """An intermediate Model that defines the relation between Risk and RiskField"""

    risk_field = models.ForeignKey(RiskField, on_delete=models.CASCADE)
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)

    class Meta:
        db_table = "risk_risk_field"
