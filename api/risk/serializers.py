from rest_framework.serializers import ModelSerializer
from risk.models import Risk


class RiskFormSerializer(ModelSerializer):
    """A serializer that generates all the information about
    the Risk and about the RiskField's
    """

    class Meta:
        model = Risk
        fields = ["id", "name"]
