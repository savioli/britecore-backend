from rest_framework.viewsets import ModelViewSet
from risk.models import Risk
from risk.serializers import RiskFormSerializer


class RiskFormViewSet(ModelViewSet):
    """A ViewSet that generates all the information about
    the Risk and about all the RiskField's
    """

    queryset = Risk.objects.all()
    serializer_class = RiskFormSerializer
