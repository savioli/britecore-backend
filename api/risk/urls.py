from risk.views import RiskFormViewSet

from django.conf.urls import url

urlpatterns = [
    url(r"^risks/(?P<pk>\d+)$", RiskFormViewSet.as_view({"get": "retrieve"})),
]
