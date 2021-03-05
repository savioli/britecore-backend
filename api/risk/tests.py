import json

from rest_framework import status
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

    def test_if_and_non_existent_risk_returns_not_found(self):
        """Test if the API displays correctly
        HTTP 404 NOT FOUND status for a risk that does not exists"""

        Risk.objects.all().delete()

        response = self.client.post("http://localhost:8000/api/risks/1")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_an_existent_risk_returns_found(self):
        """Test if the API displays correctly
        HTTP 200 OK status for a risk that exists"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        response = self.client.get("http://localhost:8000/api/v1/risks/" + str(risk.pk))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_an_existent_risk_returns_as_json(self):
        """Checks the format returned"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        response = self.client.get("http://localhost:8000/api/v1/risks/" + str(risk.pk))

        try:
            json.loads(response.content)
            is_json = True
        except Exception:
            is_json = False

        self.assertTrue(is_json)

    def test_if_an_existing_risk_retrieved_matches_with_the_risk_id_requested(self):
        """Checks whether the Risk received matches the requested Risk id"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        response = self.client.get("http://localhost:8000/api/v1/risks/" + str(risk.pk))

        response_risk_id = response.data["id"]

        self.assertEqual(response_risk_id, risk.pk)

    def test_if_a_request_with_a_negative_risk_id_responds_with_not_found(self):
        """Tests a negative entry for Risk id"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        response = self.client.get(
            "http://localhost:8000/api/v1/risks/-" + str(risk.pk)
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_the_risk_has_the_attribute_category(self):
        """Checks if the attribute category is returned"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        response = self.client.get("http://localhost:8000/api/v1/risks/" + str(risk.pk))

        try:
            response_risk_category = response.data["category"]
        except Exception:
            response_risk_category = None

        self.assertIsNotNone(response_risk_category)

    def test_if_the_risk_has_the_attribute_fields(self):
        """Checks if the attribute fields is returned"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        response = self.client.get("http://localhost:8000/api/v1/risks/" + str(risk.pk))

        try:
            response_fields_attribute = response.data["fields"]
        except Exception:
            response_fields_attribute = None

        self.assertIsNotNone(response_fields_attribute)

    def test_if_the_fields_attribute_of_a_risk_is_a_list(self):
        """Checks the format of the returned attribute"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        response = self.client.get("http://localhost:8000/api/v1/risks/" + str(risk.pk))

        try:
            response_risk_fields_attribute = type(response.data["fields"])
        except Exception:
            response_risk_fields_attribute = None

        self.assertEqual(response_risk_fields_attribute, list)

    def test_if_the_fields_attribute_of_a_risk_is_not_empty(self):
        """Checks the content of the returned attribute"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        text_risk_field = self.create_a_risk_field_by_field_type(RiskFieldType.TEXT)

        risk.risk_fields.add(text_risk_field)

        risk.save()

        response = self.client.get("http://localhost:8000/api/v1/risks/" + str(risk.pk))

        try:
            response_fields_attribute = response.data["fields"]
        except Exception:
            response_fields_attribute = None

        attributes_lenght = len(response_fields_attribute)

        self.assertGreater(attributes_lenght, 0)

    def test_if_a_text_field_present_in_the_fields_attribute_of_risk_has_the_correct_type_attribute(
        self,
    ):
        """Checks the type of the text field attribute"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        text_risk_field = self.create_a_risk_field_by_field_type(RiskFieldType.TEXT)

        risk.risk_fields.add(text_risk_field)

        risk.save()

        response = self.client.get("http://localhost:8000/api/v1/risks/" + str(risk.pk))

        try:
            required_attribute = response.data["fields"][0]["type"]
        except Exception:
            required_attribute = None

        self.assertEqual(required_attribute, RiskFieldType.TEXT)

    def test_if_a_text_field_present_in_the_fields_attribute_of_risk_has_the_attribute_required(
        self,
    ):
        """Checks if the attribute required is returned"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        text_risk_field = self.create_a_risk_field_by_field_type(RiskFieldType.TEXT)

        risk.risk_fields.add(text_risk_field)

        risk.save()

        response = self.client.get("http://localhost:8000/api/v1/risks/" + str(risk.pk))

        try:
            required_attribute = response.data["fields"][0]["required"]
        except Exception:
            required_attribute = None

        self.assertIsNotNone(required_attribute)

    def test_if_a_text_field_present_in_the_fields_attribute_of_risk_has_the_attribute_order(
        self,
    ):
        """Checks if the attribute order is returned"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        text_risk_field = self.create_a_risk_field_by_field_type(RiskFieldType.TEXT)

        risk.risk_fields.add(text_risk_field)

        risk.save()

        response = self.client.get("http://localhost:8000/api/v1/risks/" + str(risk.pk))

        try:
            required_attribute = response.data["fields"][0]["order"]
        except Exception:
            required_attribute = None

        self.assertIsNotNone(required_attribute)

    def test_if_a_number_field_present_in_the_fields_attribute_of_risk_has_the_correct_type_attribute(
        self,
    ):
        """Checks the type of the number field attribute"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        number_risk_field = self.create_a_risk_field_by_field_type(RiskFieldType.NUMBER)

        risk.risk_fields.add(number_risk_field)

        risk.save()

        response = self.client.get("http://localhost:8000/api/v1/risks/" + str(risk.pk))

        try:
            required_attribute = response.data["fields"][0]["type"]
        except Exception:
            required_attribute = None

        self.assertEqual(required_attribute, RiskFieldType.NUMBER)

    def test_if_a_number_field_present_in_the_fields_attribute_of_risk_has_the_attribute_required(
        self,
    ):
        """Checks if the attribute required is returned"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        number_risk_field = self.create_a_risk_field_by_field_type(RiskFieldType.NUMBER)

        risk.risk_fields.add(number_risk_field)
        risk.save()

        response = self.client.get("http://localhost:8000/api/v1/risks/" + str(risk.pk))

        try:
            required_attribute = response.data["fields"][0]["required"]
        except Exception:
            required_attribute = None

        self.assertIsNotNone(required_attribute)

    def test_if_a_number_field_present_in_the_fields_attribute_of_risk_has_the_attribute_order(
        self,
    ):
        """Checks if the attribute order is returned"""

        risk_category = self.create_a_risk_category()
        risk = self.create_a_risk(risk_category)

        number_risk_field = self.create_a_risk_field_by_field_type(RiskFieldType.NUMBER)

        risk.risk_fields.add(number_risk_field)
        risk.save()

        response = self.client.get("http://localhost:8000/api/v1/risks/" + str(risk.pk))

        try:
            required_attribute = response.data["fields"][0]["order"]
        except Exception:
            required_attribute = None

        self.assertIsNotNone(required_attribute)
