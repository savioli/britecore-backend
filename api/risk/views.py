from rest_framework.viewsets import ModelViewSet
from risk.models import Risk
from risk.serializers import RiskFormSerializer, RiskSerializer


class RiskFormViewSet(ModelViewSet):
    """A ViewSet that generates all the information about
    the Risk and about all the RiskField's
    """

    queryset = Risk.objects.all()
    serializer_class = RiskFormSerializer


class RiskViewSet(ModelViewSet):
    """A ViewSet that retrieves all Risks"""

    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
