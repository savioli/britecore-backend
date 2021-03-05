from rest_framework.test import APITestCase
from risk.models import Risk, RiskCategory


class RiskAPITestCase(APITestCase):
    """Test class for the Risk API"""

    fixtures = ["risk/fixtures/risk_field_type.json"]

    def create_a_risk_category(self, code="test_category"):
        """A function to help the creation of RiskCategory objects during the tests"""

        risk_category = RiskCategory(
            name="Test Category",
            description="Test category description",
            code=code,
        )
        risk_category.save()

        return risk_category

    def create_a_risk(self, risk_category):
        """A function to help the creation of Risk objects during the tests"""

        risk = Risk(name="Test Risk", risk_category=risk_category)
        risk.save()

        return risk
