from rest_framework.serializers import ModelSerializer
from risk.models import (
    Risk,
    RiskCategory,
    RiskField,
    RiskFieldEnumOption,
    RiskFieldType,
    RiskRiskField,
)


class RiskCategorySerializer(ModelSerializer):
    """A Serializer that generates
    the information about the RiskCategory
    """

    class Meta:
        fields = ["id", "code", "name", "description"]
        model = RiskCategory


class RiskFieldTypeSerializer(ModelSerializer):
    """A Serializer that generates
    the information about the RiskFieldType
    """

    class Meta:
        fields = ["id", "code", "name"]
        model = RiskFieldType


class RiskFieldEnumOptionSerializer(ModelSerializer):
    """A Serializer that generates
    the information about the RiskFieldEnumOption
    """

    class Meta:
        fields = ["id", "name"]
        model = RiskFieldEnumOption


class RiskFieldSerializer(ModelSerializer):
    """A Serializer that generates
    the information about the RiskField
    """

    risk_field_type = RiskFieldTypeSerializer()

    class Meta:
        fields = [
            "id",
            "name",
            "description",
            "risk_field_type",
        ]
        model = RiskField


class RiskRiskFieldSerializer(ModelSerializer):
    """A Serializer that generates the information
    about the model RiskRiskField that intermediates
    the model Risk and the model RiskField
    """

    def to_representation(self, instance):

        risk_field = RiskField.objects.get(pk=instance.risk_field_id)

        risk_type = risk_field.risk_field_type

        risk_field_enum_options = instance.risk_field_enum_option.all()

        risk_field_enum_options = [
            RiskFieldEnumOptionSerializer(risk_field_enum_option).data
            for risk_field_enum_option in risk_field_enum_options
        ]

        risk_field = RiskFieldSerializer(risk_field).data

        if risk_type.code == "enum":
            risk_field.update({"options": risk_field_enum_options})

        risk_field.update({"required": instance.required, "type": risk_type.code})

        risk_type = risk_field.pop("risk_field_type")

        return risk_field

    class Meta:
        fields = ["id", "name"]
        model = RiskRiskField


class RiskFormSerializer(ModelSerializer):
    """A Serializer that generates all the information about
    the Risk and about the RiskField's
    """

    risk_category = RiskCategorySerializer()

    risk_fields = RiskRiskFieldSerializer(
        source="risk_to_field", many=True, read_only=True
    )

    class Meta:
        model = Risk
        fields = ["id", "name", "risk_category", "risk_fields"]


class RiskSerializer(ModelSerializer):
    """A Serializer that generates the information about
    the Risk
    """

    risk_category = RiskCategorySerializer()

    class Meta:
        model = Risk
        fields = ["id", "name", "risk_category"]
