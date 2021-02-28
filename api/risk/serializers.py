from rest_framework.serializers import ModelSerializer
from risk.models import Risk, RiskCategory, RiskField, RiskFieldType


class RiskCategorySerializer(ModelSerializer):
    """A Serializer that generates
    the information about the RiskCategory
    """

    class Meta:
        fields = ["id", "code", "name"]
        model = RiskCategory


class RiskFieldTypeSerializer(ModelSerializer):
    """A Serializer that generates
    the information about the RiskFieldType
    """

    class Meta:
        fields = ["id", "code", "name"]
        model = RiskFieldType


class RiskFieldSerializer(ModelSerializer):
    """A Serializer that generates
    the information about the RiskField
    """

    risk_field_type = RiskFieldTypeSerializer()

    class Meta:
        fields = ["id", "name", "description", "required", "risk_field_type"]
        model = RiskField


class RiskFormSerializer(ModelSerializer):
    """A Serializer that generates all the information about
    the Risk and about the RiskField's
    """

    risk_category = RiskCategorySerializer()
    risk_fields = RiskFieldSerializer(many=True)

    class Meta:
        model = Risk
        fields = ["id", "name", "risk_category", "risk_fields"]
