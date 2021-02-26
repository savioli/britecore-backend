from rest_framework.serializers import ModelSerializer
from risk.models import Risk, RiskField, RiskFieldType


class RiskFieldTypeSerializer(ModelSerializer):
    class Meta:
        fields = ["id", "code", "name"]
        model = RiskFieldType


class RiskFieldSerializer(ModelSerializer):
    """A Serializer that generates
    the information about the RiskField
    """

    risk_field_type = RiskFieldTypeSerializer()

    class Meta:
        fields = ["id", "name", "risk_field_type"]
        model = RiskField


class RiskFormSerializer(ModelSerializer):
    """A Serializer that generates all the information about
    the Risk and about the RiskField's
    """

    risk_fields = RiskFieldSerializer(many=True)

    class Meta:
        model = Risk
        fields = ["id", "name", "risk_fields"]
