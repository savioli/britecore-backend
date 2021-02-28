from risk.views import RiskFormViewSet, RiskViewSet

from django.conf.urls import url

urlpatterns = [
    url(r"^risks", RiskViewSet.as_view({"get": "list"})),
    url(r"^risks/(?P<pk>\d+)$", RiskFormViewSet.as_view({"get": "retrieve"})),
]
