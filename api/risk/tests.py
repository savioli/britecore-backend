from rest_framework.test import APITestCase
from risk.models import (
    Risk,
    RiskCategory,
    RiskField,
    RiskFieldEnumOption,
    RiskFieldType,
)


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

    def create_a_risk_field_by_field_type(self, risk_field_type):
        """A function to help the creation of RiskField objects based on the type during the tests"""

        if risk_field_type not in [
            RiskFieldType.TEXT,
            RiskFieldType.NUMBER,
            RiskFieldType.DATE,
            RiskFieldType.ENUM,
        ]:
            raise ValueError("Invalid FieldType")

        text_risk_field_type = RiskFieldType.objects.filter(code=risk_field_type).get()

        if RiskFieldType.TEXT == risk_field_type:
            risk_field_type_name = "Text"

        elif RiskFieldType.NUMBER == risk_field_type:
            risk_field_type_name = "Number"

        elif RiskFieldType.DATE == risk_field_type:
            risk_field_type_name = "Date"

        elif RiskFieldType.ENUM == risk_field_type:
            risk_field_type_name = "Enum"

        text_risk_field = RiskField(
            name="Test " + risk_field_type_name + " Risk Field",
            risk_field_type=text_risk_field_type,
        )

        text_risk_field.save()

        return text_risk_field

    def create_a_risk_field_enum_option(self):
        """A function to help the creation of RiskFieldEnumOption objects during the tests"""
        risk_field_enum_option = RiskFieldEnumOption(
            name="Test Risk Field Enum Option",
            description="Test Risk Field Enum Option",
        )

        risk_field_enum_option.save()

        return risk_field_enum_option
