from rest_framework.serializers import ModelSerializer
from risk.models import (
    Risk,
    RiskCategory,
    RiskField,
    RiskFieldEnumOption,
    RiskFieldType,
    RiskRiskField,
    RiskRiskFieldRiskFieldEnumOption,
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


class RiskRiskFieldRiskFieldEnumOptionSerializer(ModelSerializer):
    """A Serializer that generates
    the information about the RiskFieldEnumOption
    """

    class Meta:
        fields = ["id", "checked"]
        model = RiskRiskFieldRiskFieldEnumOption


class RiskFieldEnumOptionSerializer(ModelSerializer):
    """A Serializer that generates
    the information about the RiskFieldEnumOption
    """

    class Meta:
        fields = ["id", "name", "description"]
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

    risk_risk_field_risk_field_enum_option = RiskRiskFieldRiskFieldEnumOptionSerializer(
        source="risk_risk_field_to_risk_field_enum_option", many=True, read_only=True
    )

    def to_representation(self, instance):

        risk_field = RiskField.objects.get(pk=instance.risk_field_id)

        risk_type = risk_field.risk_field_type

        if risk_type.code == "enum":

            risk_field_enum_options = instance.risk_field_enum_option.all()

            risk_field_enum_options_with_through_properties = []

            for risk_field_enum_option in risk_field_enum_options:

                risk_risk_field_risk_field_enum_option = (
                    RiskRiskFieldRiskFieldEnumOption.objects.filter(
                        risk_risk_field_id=risk_field.id,
                        risk_field_enum_option_id=risk_field_enum_option.id,
                    ).first()
                )

                serialized_risk_risk_field_risk_field_enum_option = (
                    RiskFieldEnumOptionSerializer(risk_field_enum_option).data
                )

                serialized_risk_risk_field_risk_field_enum_option.update(
                    {"checked": risk_risk_field_risk_field_enum_option.checked}
                )

                risk_field_enum_options_with_through_properties.append(
                    serialized_risk_risk_field_risk_field_enum_option
                )

            risk_field = RiskFieldSerializer(risk_field).data

            risk_field.update(
                {"options": risk_field_enum_options_with_through_properties}
            )

        else:
            risk_field = RiskFieldSerializer(risk_field).data

        risk_field.update(
            {
                "required": instance.required,
                "type": risk_type.code,
                "order": instance.order,
            }
        )

        risk_type = risk_field.pop("risk_field_type")

        return risk_field

    class Meta:
        fields = ["id", "name", "risk_risk_field_risk_field_enum_option"]
        model = RiskRiskField


class RiskFormSerializer(ModelSerializer):
    """A Serializer that generates all the information about
    the Risk and about the RiskField's
    """

    risk_category = RiskCategorySerializer()

    fields = RiskRiskFieldSerializer(source="risk_to_field", many=True, read_only=True)

    class Meta:
        model = Risk
        fields = ["id", "name", "risk_category", "fields"]


class RiskSerializer(ModelSerializer):
    """A Serializer that generates the information about
    the Risk
    """

    risk_category = RiskCategorySerializer()

    class Meta:
        model = Risk
        fields = ["id", "name", "risk_category"]
