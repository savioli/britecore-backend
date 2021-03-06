from risk.models import (
    Risk,
    RiskCategory,
    RiskField,
    RiskFieldEnumOption,
    RiskFieldType,
    RiskRiskField,
    RiskRiskFieldRiskFieldEnumOption,
)

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def get_risk_field_type_by_code(self, code):
        """A function to help the creation of RiskField objects based on the type"""

        if code not in [
            RiskFieldType.TEXT,
            RiskFieldType.NUMBER,
            RiskFieldType.DATE,
            RiskFieldType.ENUM,
        ]:
            raise ValueError("Invalid FieldType")

        return RiskFieldType.objects.filter(code=code).get()

    def handle(self, *args, **options):

        call_command("flush", "--no-input")
        call_command("loaddata", "risk/fixtures/risk_field_type.json")

        # TextRiskField
        first_name_text_risk_field = RiskField(
            name="First Name",
            description="Middle Name Description",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.TEXT),
        )
        first_name_text_risk_field.save()

        middle_name_text_risk_field = RiskField(
            name="Middle Name",
            description="Middle Name Description",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.TEXT),
        )
        middle_name_text_risk_field.save()

        last_name_text_risk_field = RiskField(
            name="Last Name",
            description="Last Name Description",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.TEXT),
        )
        last_name_text_risk_field.save()

        website_name_text_risk_field = RiskField(
            name="Website",
            description="Website Description",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.TEXT),
        )
        website_name_text_risk_field.save()

        # NumberRiskField
        age_number_risk_field = RiskField(
            name="Age",
            description="Age Description",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        age_number_risk_field.save()

        number_of_beneficiaries_number_risk_field = RiskField(
            name="Number of Beneficiaries",
            description="Number of Beneficiaries Description",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        number_of_beneficiaries_number_risk_field.save()

        mileage_number_risk_field = RiskField(
            name="Mileage",
            description="Mileage Description",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        mileage_number_risk_field.save()

        years_in_the_market_risk_field = RiskField(
            name="Years in the Market",
            description="Years in the Market",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        years_in_the_market_risk_field.save()

        mileage_number_risk_field = RiskField(
            name="Mileage",
            description="Mileage Description",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        mileage_number_risk_field.save()

        number_of_employees_number_risk_field = RiskField(
            name="Number of Employees",
            description="Number of Employees Description",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        number_of_employees_number_risk_field.save()
        # Is Multinational

        # DateRiskField
        date_of_birth_date_risk_field = RiskField(
            name="Date of Birth",
            description="Date of Birth Description",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.DATE),
        )
        date_of_birth_date_risk_field.save()

        acquisition_date_risk_field = RiskField(
            name="Acquisition Date",
            description="Acquisition Date",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.DATE),
        )
        acquisition_date_risk_field.save()

        # Options
        yes_risk_field_enum_option = RiskFieldEnumOption(
            name="Yes", description="Yes Description"
        )
        yes_risk_field_enum_option.save()

        no_risk_field_enum_option = RiskFieldEnumOption(
            name="No", description="No Description"
        )
        no_risk_field_enum_option.save()

        new_condition_risk_field_enum_option = RiskFieldEnumOption(
            name="New", description="New Description"
        )
        new_condition_risk_field_enum_option.save()

        used_condition_risk_field_enum_option = RiskFieldEnumOption(
            name="Used", description="Used Description"
        )
        used_condition_risk_field_enum_option.save()

        # Enum
        has_children_enum_risk_field = RiskField(
            name="Has Children?",
            description="Has Children Description",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.ENUM),
        )

        has_children_enum_risk_field.save()

        condition_enum_risk_field = RiskField(
            name="Condition",
            description="Condition Description",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.ENUM),
        )

        condition_enum_risk_field.save()

        # Categories
        name = "Vehicle"
        code = "vehicle"
        description = "Vehicle Category Description"
        vehicle_risk_category = RiskCategory(
            name=name, code=code, description=description
        )
        vehicle_risk_category.save()

        name = "Cyber Insurance"
        code = "cybernetic"
        description = "Cybernetic Category Description"
        cybernetic_risk_category = RiskCategory(
            name=name, code=code, description=description
        )
        cybernetic_risk_category.save()

        name = "Property-Based"
        description = "Property-Based Category Description"
        code = "property_based"
        property_based_risk_category = RiskCategory(
            name=name, code=code, description=description
        )
        property_based_risk_category.save()

        name = "Prize Insurance"
        code = "prize"
        description = "Prize Category Description"
        prize_risk_category = RiskCategory(
            name=name, code=code, description=description
        )
        prize_risk_category.save()

        name = "life"
        code = "life"
        description = "Life Insurance"
        life_risk_category = RiskCategory(name=name, code=code, description=description)
        life_risk_category.save()

        # name = "Prize Insurance"
        # code = "prize"
        # description = "Prize Category Description"
        # prize_risk_category = RiskCategory(name=name, code=code,description=description)
        # prize_risk_category.save()

        # Risks

        vehicle_risk_category_risk = Risk(
            name="Automobile Insurance", risk_category=vehicle_risk_category
        )
        vehicle_risk_category_risk.save()

        vehicle_risk_category_risk.risk_fields.add(first_name_text_risk_field)
        vehicle_risk_category_risk.risk_fields.add(middle_name_text_risk_field)
        vehicle_risk_category_risk.risk_fields.add(last_name_text_risk_field)
        vehicle_risk_category_risk.risk_fields.add(acquisition_date_risk_field)
        vehicle_risk_category_risk.risk_fields.add(mileage_number_risk_field)

        # Add a relation
        vehicle_risk_category_risk.risk_fields.add(condition_enum_risk_field)
        vehicle_risk_category_risk.save()

        # Connects the Risk with the EnumRiskField
        risk_risk_field = RiskRiskField.objects.filter(
            risk=vehicle_risk_category_risk, risk_field=condition_enum_risk_field
        ).get()

        # Add  an EnumRiskFieldOption
        RiskRiskFieldRiskFieldEnumOption(
            risk_risk_field=risk_risk_field,
            risk_field_enum_option=new_condition_risk_field_enum_option,
            checked=True,
        ).save()

        cybernetic_risk_category_risk_category = Risk(
            name="Cyber Liability Coverage", risk_category=cybernetic_risk_category
        )
        cybernetic_risk_category_risk_category.save()

        cybernetic_risk_category_risk_category.risk_fields.add(
            number_of_employees_number_risk_field
        )
        cybernetic_risk_category_risk_category.risk_fields.add(
            acquisition_date_risk_field
        )
        cybernetic_risk_category_risk_category.risk_fields.add(
            years_in_the_market_risk_field
        )
        cybernetic_risk_category_risk_category.risk_fields.add(
            website_name_text_risk_field
        )

        cybernetic_risk_category_risk_category.save()

        property_based_risk_category_risk_one = Risk(
            name="Home Insurance", risk_category=property_based_risk_category
        )
        property_based_risk_category_risk_one.save()

        property_based_risk_category_risk_one.risk_fields.add(
            first_name_text_risk_field
        )
        property_based_risk_category_risk_one.risk_fields.add(
            middle_name_text_risk_field
        )
        property_based_risk_category_risk_one.risk_fields.add(last_name_text_risk_field)
        property_based_risk_category_risk_one.save()
        # property_based_risk_category_risk_two = Risk(
        #   name="Renters Insurance",
        #   risk_category=property_based_risk_category
        # )
        # property_based_risk_category_risk_two.save()

        # risk_category = Risk(name="Builder's Risk Insurance")
        # risk_category.save()

        # Risk 1
        life_risk_category_risk = Risk(
            name="Whole Life", risk_category=life_risk_category
        )
        life_risk_category_risk.save()

        life_risk_category_risk.risk_fields.add(first_name_text_risk_field)
        life_risk_category_risk.risk_fields.add(middle_name_text_risk_field)
        life_risk_category_risk.risk_fields.add(last_name_text_risk_field)

        life_risk_category_risk.risk_fields.add(date_of_birth_date_risk_field)
        life_risk_category_risk.risk_fields.add(
            number_of_beneficiaries_number_risk_field
        )

        # Add a relation
        life_risk_category_risk.risk_fields.add(has_children_enum_risk_field)
        life_risk_category_risk.save()

        # Connects the Risk with the EnumRiskField
        risk_risk_field = RiskRiskField.objects.filter(
            risk=life_risk_category_risk, risk_field=has_children_enum_risk_field
        ).get()

        # Add  an EnumRiskFieldOption
        RiskRiskFieldRiskFieldEnumOption(
            risk_risk_field=risk_risk_field,
            risk_field_enum_option=yes_risk_field_enum_option,
        ).save()

        RiskRiskFieldRiskFieldEnumOption(
            risk_risk_field=risk_risk_field,
            risk_field_enum_option=no_risk_field_enum_option,
            checked=True,
        ).save()
        
        # Risk 2
        life_risk_category_risk.save()

        life_risk_category_risk = Risk(
            name="Term Life Insurance", risk_category=life_risk_category
        )
        life_risk_category_risk.save()

        life_risk_category_risk.risk_fields.add(first_name_text_risk_field)
        life_risk_category_risk.risk_fields.add(middle_name_text_risk_field)
        life_risk_category_risk.risk_fields.add(last_name_text_risk_field)

        life_risk_category_risk.risk_fields.add(date_of_birth_date_risk_field)

        life_risk_category_risk.risk_fields.add(
            number_of_beneficiaries_number_risk_field
        )

        life_risk_category_risk.save()

        # Universal life insurance
        life_risk_category_risk.save()

        life_risk_category_risk = Risk(
            name="Universal life insurance", risk_category=life_risk_category
        )
        life_risk_category_risk.save()

        life_risk_category_risk.risk_fields.add(first_name_text_risk_field)
        life_risk_category_risk.risk_fields.add(middle_name_text_risk_field)
        life_risk_category_risk.risk_fields.add(last_name_text_risk_field)

        life_risk_category_risk.risk_fields.add(date_of_birth_date_risk_field)

        life_risk_category_risk.risk_fields.add(
            number_of_beneficiaries_number_risk_field
        )

        # Add a relation
        life_risk_category_risk.risk_fields.add(has_children_enum_risk_field)
        life_risk_category_risk.save()

        # Connects the Risk with the EnumRiskField
        risk_risk_field = RiskRiskField.objects.filter(
            risk=life_risk_category_risk, risk_field=has_children_enum_risk_field
        ).get()

        # Add  an EnumRiskFieldOption
        RiskRiskFieldRiskFieldEnumOption(
            risk_risk_field=risk_risk_field,
            risk_field_enum_option=yes_risk_field_enum_option,
        ).save()

        RiskRiskFieldRiskFieldEnumOption(
            risk_risk_field=risk_risk_field,
            risk_field_enum_option=no_risk_field_enum_option,
            checked=True,
        ).save()

        life_risk_category_risk.save()
