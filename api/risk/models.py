from django.db import models


class RiskFieldType(models.Model):
    """A Model that represents the type of a Field of a Risk"""

    TEXT = "text"
    NUMBER = "number"
    ENUM = "enum"
    DATE = "date"

    name = models.CharField(max_length=128)
    code = models.CharField(max_length=64, unique=True)

    class Meta:

        db_table = "risk_field_type"


class RiskField(models.Model):
    """A Model that defines the representation of a Field of a Risk"""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    risk_field_type = models.ForeignKey(RiskFieldType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "risk_field"


class RiskCategory(models.Model):
    """A Model that represents a Category of a Risk"""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    code = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "risk_category"


class Risk(models.Model):
    """A Model that defines the representation of a Risk"""

    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
    description = models.CharField(max_length=256)
    risk_category = models.ForeignKey(RiskCategory, on_delete=models.CASCADE)
    risk_fields = models.ManyToManyField(RiskField, through="RiskRiskField")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "risk"
        ordering = ["id"]


class RiskFieldEnumOption(models.Model):
    """A Model that defines the representation of a RiskFieldEnumOption"""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "risk_field_enum_option"


class RiskRiskField(models.Model):
    """An intermediate Model that defines the relation between Risk and RiskField"""

    required = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    risk = models.ForeignKey(
        Risk, on_delete=models.CASCADE, related_name="risk_to_field"
    )
    risk_field = models.ForeignKey(
        RiskField, on_delete=models.CASCADE, related_name="field_to_risk"
    )

    risk_field_enum_option = models.ManyToManyField(
        RiskFieldEnumOption, through="RiskRiskFieldRiskFieldEnumOption"
    )

    class Meta:
        db_table = "risk_risk_field"
        ordering = ["order"]


class RiskRiskFieldRiskFieldEnumOption(models.Model):
    """An intermediate Model that defines the relation between RiskRiskField and RiskFieldEnumOption"""

    checked = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    risk_risk_field = models.ForeignKey(
        RiskRiskField,
        on_delete=models.CASCADE,
        related_name="risk_risk_field_to_risk_field_enum_option",
    )

    risk_field_enum_option = models.ForeignKey(
        RiskFieldEnumOption,
        on_delete=models.CASCADE,
        related_name="risk_field_enum_option_to_risk_risk_field",
    )

    class Meta:
        db_table = "risk_risk_field_risk_field_enum_option"
        ordering = ["order"]
