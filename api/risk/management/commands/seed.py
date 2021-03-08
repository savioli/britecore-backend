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
    def add_risk_field_enum_options(
        self, risk_risk_field, risk_field_enum_options, checked_index
    ):

        for index, risk_field_enum_option in enumerate(risk_field_enum_options):

            risk_field_enum_option.save()

            isChecked = False

            if checked_index == index:
                isChecked = True

            self.add_risk_field_enum_option_to_risk_risk_field(
                risk_risk_field=risk_risk_field,
                risk_field_enum_option=risk_field_enum_option,
                order=index,
                checked=isChecked,
            )

    def add_risk_field_to_risk(self, risk, risk_field, required=False, order=0):

        risk.risk_fields.add(risk_field)
        risk.save()

        # Connects the Risk with the EnumRiskField
        risk_risk_field = RiskRiskField.objects.filter(
            risk=risk, risk_field=risk_field
        ).get()

        update = False

        if required:
            update = True
        elif order != 0:
            update = True

        if update:
            risk_risk_field.required = required
            risk_risk_field.order = order
            risk_risk_field.save()

        return risk_risk_field

    def add_risk_field_enum_option_to_risk_risk_field(
        self, risk_risk_field, risk_field_enum_option, checked=False, order=0
    ):

        RiskRiskFieldRiskFieldEnumOption(
            risk_risk_field=risk_risk_field,
            risk_field_enum_option=risk_field_enum_option,
            checked=checked,
            order=order,
        ).save()

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

        # Categories

        # Category 1
        vehicle_risk_category = RiskCategory(
            name="Vehicle", code="vehicle", description="Vehicle Insurance"
        )
        vehicle_risk_category.save()

        # Category 2
        cybernetic_risk_category = RiskCategory(
            name="Cyber Insurance",
            code="cybernetic",
            description="Cybernetic Insurance",
        )
        cybernetic_risk_category.save()

        # Category 3
        property_based_risk_category = RiskCategory(
            name="Property-Based",
            description="Property-Based Insurance",
            code="property_based",
        )
        property_based_risk_category.save()

        # Category 4
        life_risk_category = RiskCategory(
            name="life", code="life", description="Life Insurance"
        )
        life_risk_category.save()

        # Category 4
        travel_risk_category = RiskCategory(
            name="travel", code="travel", description="Travel Insurance"
        )
        travel_risk_category.save()

        # Common Fields

        # Common TextRiskField

        # Field
        first_name_text_risk_field = RiskField(
            name="First Name",
            description="",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.TEXT),
        )
        first_name_text_risk_field.save()

        # Field
        last_name_text_risk_field = RiskField(
            name="Last Name",
            description="",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.TEXT),
        )
        last_name_text_risk_field.save()

        # Common NumberRiskField

        # Field
        age_number_risk_field = RiskField(
            name="Age",
            description="Age Description",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        age_number_risk_field.save()

        # Field
        number_of_beneficiaries_number_risk_field = RiskField(
            name="Number of Beneficiaries",
            description="The total number of beneficiaries.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        number_of_beneficiaries_number_risk_field.save()

        # Common DateRiskField

        # Field
        date_of_birth_date_risk_field = RiskField(
            name="Date of Birth",
            description="",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.DATE),
        )
        date_of_birth_date_risk_field.save()

        # Risks

        # Risk 1

        vehicle_risk = Risk(
            name="Automobile Insurance",
            description="Automobile insurance with coverage for several damages among other additional coverage.",
            risk_category=vehicle_risk_category,
        )
        vehicle_risk.save()

        # Field
        risk_risk_field = self.add_risk_field_to_risk(
            risk=vehicle_risk,
            risk_field=first_name_text_risk_field,
            required=True,
            order=1,
        )

        # Field
        risk_risk_field = self.add_risk_field_to_risk(
            risk=vehicle_risk,
            risk_field=last_name_text_risk_field,
            required=True,
            order=1,
        )

        # Field
        condition_enum_risk_field = RiskField(
            name="Condition",
            description="What is the condition of the automobile?",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.ENUM),
        )
        condition_enum_risk_field.save()

        risk_risk_field = self.add_risk_field_to_risk(
            risk=vehicle_risk,
            risk_field=condition_enum_risk_field,
            required=False,
            order=1,
        )

        # Field Options
        risk_field_enum_option_zero = RiskFieldEnumOption(name="New", description="")
        risk_field_enum_option_zero.save()

        risk_field_enum_option_one = RiskFieldEnumOption(name="Used", description="")
        risk_field_enum_option_one.save()

        risk_field_enum_options = [
            risk_field_enum_option_zero,
            risk_field_enum_option_one,
        ]

        self.add_risk_field_enum_options(risk_risk_field, risk_field_enum_options, 1)

        # Field
        date_risk_field = RiskField(
            name="Acquisition Date",
            description="When the automobile was bought?",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.DATE),
        )
        date_risk_field.save()

        risk_risk_field = self.add_risk_field_to_risk(
            risk=vehicle_risk, risk_field=date_risk_field, required=True, order=1
        )

        # Field
        number_risk_field = RiskField(
            name="Mileage",
            description="What is the mileage of the automobile?",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        number_risk_field.save()

        risk_risk_field = self.add_risk_field_to_risk(
            risk=vehicle_risk, risk_field=number_risk_field, required=True, order=1
        )

        # Field
        fuel_enum_risk_field = RiskField(
            name="Fuel",
            description="What fuel does the automobile use?",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.ENUM),
        )

        fuel_enum_risk_field.save()

        # Field Options
        gasoline_fuel_risk_field_enum_option = RiskFieldEnumOption(
            name="Gasoline", description="Gasoline, the most common fuel used in cars."
        )
        gasoline_fuel_risk_field_enum_option.save()

        ethanol_fuel_risk_field_enum_option = RiskFieldEnumOption(
            name="Ethanol", description="Ethanol, a bio-fuel alternative to gasoline."
        )
        ethanol_fuel_risk_field_enum_option.save()

        flex_fuel_fuel_risk_field_enum_option = RiskFieldEnumOption(
            name="Flex-Fuel",
            description="Flex-Fuel, a combination of gasoline and methanol or ethanol.",
        )
        flex_fuel_fuel_risk_field_enum_option.save()

        bio_diesel_fuel_risk_field_enum_option = RiskFieldEnumOption(
            name="Bio-Diesel", description="Bio-diesel, a diesel substitute."
        )
        bio_diesel_fuel_risk_field_enum_option.save()

        diesel_fuel_risk_field_enum_option = RiskFieldEnumOption(
            name="Diesel",
            description="Diesel fuel that is widely used in transport vehicles.",
        )
        diesel_fuel_risk_field_enum_option.save()

        risk_risk_field = self.add_risk_field_to_risk(
            risk=vehicle_risk, risk_field=fuel_enum_risk_field, required=True, order=1
        )

        risk_field_enum_options = [
            gasoline_fuel_risk_field_enum_option,
            ethanol_fuel_risk_field_enum_option,
            flex_fuel_fuel_risk_field_enum_option,
            bio_diesel_fuel_risk_field_enum_option,
            diesel_fuel_risk_field_enum_option,
        ]

        self.add_risk_field_enum_options(risk_risk_field, risk_field_enum_options, 2)

        # Risk 2

        # Category
        name = "Prize Insurance"
        code = "prize"
        description = "Prize Insurence"
        prize_risk_category = RiskCategory(
            name=name, code=code, description=description
        )
        prize_risk_category.save()

        prize_risk = Risk(
            name="Golf Tournament Prize Insurance",
            description="Insurance with an indemnity to avoid losses if the outcome of your event is not as expected.",
            risk_category=prize_risk_category,
        )

        prize_risk.save()

        # Field
        text_risk_field = RiskField(
            name="Tournament Name",
            description="The exact name that will be made public.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.TEXT),
        )
        text_risk_field.save()

        self.add_risk_field_to_risk(
            risk=prize_risk, risk_field=text_risk_field, required=False, order=1
        )

        # Field
        number_risk_field = RiskField(
            name="Tournament Prize",
            description="The total prize to be covered.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        number_risk_field.save()

        self.add_risk_field_to_risk(
            risk=prize_risk, risk_field=number_risk_field, required=True, order=1
        )

        # Field
        date_risk_field = RiskField(
            name="Start Date",
            description="The tournament start date.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.DATE),
        )
        date_risk_field.save()

        self.add_risk_field_to_risk(
            risk=prize_risk, risk_field=date_risk_field, required=True, order=1
        )

        # Field
        date_risk_field = RiskField(
            name="End Date",
            description="The date the tournament will end.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.DATE),
        )
        date_risk_field.save()

        self.add_risk_field_to_risk(
            risk=prize_risk, risk_field=date_risk_field, required=True, order=1
        )

        # Field
        enum_risk_field = RiskField(
            name="Number of Competitors",
            description="Choose the range that covers the total number of competitors.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.ENUM),
        )
        enum_risk_field.save()

        risk_risk_field = self.add_risk_field_to_risk(
            risk=prize_risk, risk_field=enum_risk_field, required=True, order=1
        )

        # Field Options
        risk_field_enum_option_one = RiskFieldEnumOption(
            name="2 to 10", description="From 2 to 10 competitors."
        )

        risk_field_enum_option_two = RiskFieldEnumOption(
            name="11 to 25", description="From 11 to 25 competitors."
        )

        risk_field_enum_option_three = RiskFieldEnumOption(
            name="26 to 50", description="From 26 to 50 competitors."
        )

        risk_field_enum_option_four = RiskFieldEnumOption(
            name="51 to 100", description="From 51 to 100 competitors."
        )

        risk_field_enum_options = [
            risk_field_enum_option_one,
            risk_field_enum_option_two,
            risk_field_enum_option_three,
            risk_field_enum_option_four,
        ]

        self.add_risk_field_enum_options(
            risk_risk_field, risk_field_enum_options, checked_index=1
        )

        # checked_option_index =
        # for index, risk_field_enum_option in enumerate(risk_field_enum_options):

        #     risk_field_enum_option.save()

        #     self.add_risk_field_enum_option_to_risk_risk_field(
        #         risk_risk_field=risk_risk_field,
        #         risk_field_enum_option=risk_field_enum_option,
        #         order=index
        #     )

        # Risk 3

        cybernetic_risk = Risk(
            name="Cyber Liability Coverage",
            description="Cyber Liability Coverage is used to guard your business against internet threats.",
            risk_category=cybernetic_risk_category,
        )
        cybernetic_risk.save()

        # Field
        text_risk_field = RiskField(
            name="Company Name",
            description="The public name of the company.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.TEXT),
        )
        text_risk_field.save()

        self.add_risk_field_to_risk(
            risk=cybernetic_risk, risk_field=text_risk_field, required=True, order=1
        )

        # Field
        date_risk_field = RiskField(
            name="Foundation Date",
            description="The date of foundation  of the company.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.DATE),
        )
        date_risk_field.save()

        self.add_risk_field_to_risk(
            risk=cybernetic_risk, risk_field=date_risk_field, required=True, order=1
        )

        # Field
        number_risk_field = RiskField(
            name="Years in the Market",
            description="The total of years in the market.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        number_risk_field.save()

        self.add_risk_field_to_risk(
            risk=cybernetic_risk, risk_field=number_risk_field, required=True, order=1
        )

        # Field
        enum_risk_field = RiskField(
            name="Is multinational?",
            description="Does the company operate in several countries abroad?",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.ENUM),
        )
        enum_risk_field.save()

        risk_risk_field = self.add_risk_field_to_risk(
            risk=cybernetic_risk, risk_field=enum_risk_field, required=True, order=1
        )

        # Field Options
        risk_field_enum_option_one = RiskFieldEnumOption(name="Yes", description="")

        risk_field_enum_option_two = RiskFieldEnumOption(name="No", description="")

        risk_field_enum_options = [
            risk_field_enum_option_one,
            risk_field_enum_option_two,
        ]

        for index, risk_field_enum_option in enumerate(risk_field_enum_options):

            risk_field_enum_option.save()

            self.add_risk_field_enum_option_to_risk_risk_field(
                risk_risk_field=risk_risk_field,
                risk_field_enum_option=risk_field_enum_option,
                order=index,
            )

        # Risk 5

        description = "Church Insurance is designed to help you assess and"
        description = (
            description + " manage risk as well as facilitate quick and easy claims."
        )
        property_based_risk = Risk(
            name="Church Insurance",
            description=description,
            risk_category=property_based_risk_category,
        )
        property_based_risk.save()

        # Field
        text_risk_field = RiskField(
            name="Church Name",
            description="The complete name of the church.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.TEXT),
        )
        text_risk_field.save()

        self.add_risk_field_to_risk(
            risk=property_based_risk, risk_field=text_risk_field, required=True, order=1
        )

        # Field
        date_risk_field = RiskField(
            name="Foundation Date",
            description="The date of foundation of the church.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.DATE),
        )
        date_risk_field.save()

        self.add_risk_field_to_risk(
            risk=property_based_risk, risk_field=date_risk_field, required=True, order=1
        )

        # Field
        number_risk_field = RiskField(
            name="Number of Members",
            description="The total of members of the community.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        number_risk_field.save()

        self.add_risk_field_to_risk(
            risk=property_based_risk,
            risk_field=number_risk_field,
            required=True,
            order=1,
        )

        # Field
        enum_risk_field = RiskField(
            name="Type of Coverage",
            description="What is the desired coverage type?",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.ENUM),
        )
        enum_risk_field.save()

        risk_risk_field = self.add_risk_field_to_risk(
            risk=property_based_risk, risk_field=enum_risk_field, required=True, order=1
        )

        # Field Options
        risk_field_enum_option_one = RiskFieldEnumOption(
            name="Basic", description="All the essential coverage."
        )

        risk_field_enum_option_two = RiskFieldEnumOption(
            name="Premium",
            description="All the essential coverage with additional support and services",
        )

        risk_field_enum_options = [
            risk_field_enum_option_zero,
            # risk_field_enum_option_one,
        ]

        for index, risk_field_enum_option in enumerate(risk_field_enum_options):

            risk_field_enum_option.save()

            self.add_risk_field_enum_option_to_risk_risk_field(
                risk_risk_field=risk_risk_field,
                risk_field_enum_option=risk_field_enum_option,
                order=index,
            )

        risk_field_enum_option_one.save()

        self.add_risk_field_enum_option_to_risk_risk_field(
            risk_risk_field=risk_risk_field,
            risk_field_enum_option=risk_field_enum_option_one,
            order=1,
            checked=True,
        )

        # Risk 5
        description = "Home Insurance is reassurance."
        description = description + " It protects the home and its contents against"
        description = description + " damage or theft if the unexpected happens."

        property_based_risk = Risk(
            name="House Insurance",
            description=description,
            risk_category=property_based_risk_category,
        )
        property_based_risk.save()

        # Field
        enum_risk_field = RiskField(
            name="Property Type",
            description="What type of property?",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.ENUM),
        )
        enum_risk_field.save()

        risk_risk_field = self.add_risk_field_to_risk(
            risk=property_based_risk, risk_field=enum_risk_field, required=True, order=1
        )

        # Field Options
        risk_field_enum_option_zero = RiskFieldEnumOption(name="Condo", description="")

        risk_field_enum_option_one = RiskFieldEnumOption(
            name="Townhouse", description=""
        )

        risk_field_enum_option_two = RiskFieldEnumOption(
            name="Detached House", description=""
        )

        risk_field_enum_options = [
            risk_field_enum_option_zero,
            risk_field_enum_option_one,
            # risk_field_enum_option_two,
        ]

        for index, risk_field_enum_option in enumerate(risk_field_enum_options):

            risk_field_enum_option.save()

            self.add_risk_field_enum_option_to_risk_risk_field(
                risk_risk_field=risk_risk_field,
                risk_field_enum_option=risk_field_enum_option,
                order=index,
            )

        risk_field_enum_option_two.save()

        self.add_risk_field_enum_option_to_risk_risk_field(
            risk_risk_field=risk_risk_field,
            risk_field_enum_option=risk_field_enum_option_two,
            order=index + 1,
            checked=True,
        )

        # Field
        self.add_risk_field_to_risk(
            risk=property_based_risk,
            risk_field=first_name_text_risk_field,
            required=True,
            order=1,
        )

        # Field
        self.add_risk_field_to_risk(
            risk=property_based_risk,
            risk_field=last_name_text_risk_field,
            required=True,
            order=1,
        )

        # Field
        date_risk_field = RiskField(
            name="Construction Date",
            description="The date of the construction of the property.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.DATE),
        )
        date_risk_field.save()

        self.add_risk_field_to_risk(
            risk=property_based_risk,
            risk_field=date_risk_field,
            required=False,
            order=1,
        )

        # Field
        number_risk_field = RiskField(
            name="Price",
            description="The updated price of the property in the market.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        number_risk_field.save()

        self.add_risk_field_to_risk(
            risk=property_based_risk,
            risk_field=number_risk_field,
            required=True,
            order=1,
        )

        # Risk 5
        property_based_risk = Risk(
            name="Commercial Farm and Ranch Insurance",
            description="Farm and Ranch Insurance offers protection for farm property and equipment.",
            risk_category=property_based_risk_category,
        )
        property_based_risk.save()

        # Field
        enum_risk_field = RiskField(
            name="Property Type",
            description="What type of property?",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.ENUM),
        )
        enum_risk_field.save()

        risk_risk_field = self.add_risk_field_to_risk(
            risk=property_based_risk, risk_field=enum_risk_field, required=True, order=1
        )

        # Field Options
        risk_field_enum_option_zero = RiskFieldEnumOption(
            name="Dairy Farming", description=""
        )

        risk_field_enum_option_one = RiskFieldEnumOption(
            name="Grain Farming", description=""
        )

        risk_field_enum_option_two = RiskFieldEnumOption(
            name="Plantation Farming", description=""
        )

        risk_field_enum_option_three = RiskFieldEnumOption(
            name="Livestock Ranching", description=""
        )

        risk_field_enum_option_four = RiskFieldEnumOption(
            name="Commercial Gardening and Fruit Farming", description=""
        )

        risk_field_enum_options = [
            risk_field_enum_option_zero,
            risk_field_enum_option_one,
            risk_field_enum_option_two,
            risk_field_enum_option_three,
            risk_field_enum_option_four,
        ]

        self.add_risk_field_enum_options(risk_risk_field, risk_field_enum_options, 3)

        # Field
        date_risk_field = RiskField(
            name="Construction Date",
            description="The date of the construction of the property.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.DATE),
        )
        date_risk_field.save()

        self.add_risk_field_to_risk(
            risk=property_based_risk, risk_field=date_risk_field, required=True, order=1
        )

        # Field
        number_risk_field = RiskField(
            name="Property Market Price",
            description="The updated price of the property in the market.",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        number_risk_field.save()

        self.add_risk_field_to_risk(
            risk=property_based_risk,
            risk_field=number_risk_field,
            required=True,
            order=1,
        )

        # Field
        self.add_risk_field_to_risk(
            risk=property_based_risk,
            risk_field=first_name_text_risk_field,
            required=True,
            order=1,
        )

        # Field
        self.add_risk_field_to_risk(
            risk=property_based_risk,
            risk_field=last_name_text_risk_field,
            required=True,
            order=1,
        )

        # Risk 7
        life_risk = Risk(
            name="Whole Life Insurance",
            description="Permanent type life insurance with coverage throughout the life.",
            risk_category=life_risk_category,
        )
        life_risk.save()

        # Field
        self.add_risk_field_to_risk(
            risk=life_risk,
            risk_field=date_of_birth_date_risk_field,
            required=True,
            order=1,
        )

        # Field
        enum_risk_field = RiskField(
            name="Plan",
            description="What is the desired plan?",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.ENUM),
        )
        enum_risk_field.save()

        risk_risk_field = self.add_risk_field_to_risk(
            risk=life_risk, risk_field=enum_risk_field, required=True, order=1
        )

        # Field Options
        risk_field_enum_option_zero = RiskFieldEnumOption(name="Basic", description="")

        risk_field_enum_option_one = RiskFieldEnumOption(name="Plus", description="")

        risk_field_enum_option_two = RiskFieldEnumOption(name="Premium", description="")

        risk_field_enum_options = [
            risk_field_enum_option_zero,
            risk_field_enum_option_one,
            # risk_field_enum_option_two,
        ]

        for index, risk_field_enum_option in enumerate(risk_field_enum_options):

            risk_field_enum_option.save()

            self.add_risk_field_enum_option_to_risk_risk_field(
                risk_risk_field=risk_risk_field,
                risk_field_enum_option=risk_field_enum_option,
                order=index,
            )

        risk_field_enum_option_two.save()

        self.add_risk_field_enum_option_to_risk_risk_field(
            risk_risk_field=risk_risk_field,
            risk_field_enum_option=risk_field_enum_option_two,
            checked=True,
            order=index + 1,
        )

        # Field
        self.add_risk_field_to_risk(
            risk=life_risk,
            risk_field=first_name_text_risk_field,
            required=True,
            order=1,
        )

        # Field
        self.add_risk_field_to_risk(
            risk=life_risk, risk_field=last_name_text_risk_field, required=True, order=1
        )

        # Field
        self.add_risk_field_to_risk(
            risk=life_risk,
            risk_field=number_of_beneficiaries_number_risk_field,
            required=True,
            order=1,
        )

        # Risk 8
        life_risk = Risk(
            name="Term Life Insurance",
            description="Life insurance with coverage over a period of time.",
            risk_category=life_risk_category,
        )
        life_risk.save()

        # Field
        self.add_risk_field_to_risk(
            risk=life_risk,
            risk_field=date_of_birth_date_risk_field,
            required=True,
            order=1,
        )

        # Field
        enum_risk_field = RiskField(
            name="Plan",
            description="What is the desired plan?",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.ENUM),
        )
        enum_risk_field.save()

        risk_risk_field = self.add_risk_field_to_risk(
            risk=life_risk, risk_field=enum_risk_field, required=True, order=1
        )

        # Field Options
        risk_field_enum_option_zero = RiskFieldEnumOption(name="Basic", description="")

        risk_field_enum_option_one = RiskFieldEnumOption(name="Plus", description="")

        risk_field_enum_option_two = RiskFieldEnumOption(name="Premium", description="")

        risk_field_enum_options = [
            risk_field_enum_option_zero,
            risk_field_enum_option_one,
            # risk_field_enum_option_two,
        ]

        for index, risk_field_enum_option in enumerate(risk_field_enum_options):

            risk_field_enum_option.save()

            self.add_risk_field_enum_option_to_risk_risk_field(
                risk_risk_field=risk_risk_field,
                risk_field_enum_option=risk_field_enum_option,
                order=index,
            )

        risk_field_enum_option_two.save()

        self.add_risk_field_enum_option_to_risk_risk_field(
            risk_risk_field=risk_risk_field,
            risk_field_enum_option=risk_field_enum_option_two,
            checked=True,
            order=index + 1,
        )

        # Field
        self.add_risk_field_to_risk(
            risk=life_risk,
            risk_field=first_name_text_risk_field,
            required=True,
            order=1,
        )

        # Field
        self.add_risk_field_to_risk(
            risk=life_risk, risk_field=last_name_text_risk_field, required=True, order=1
        )

        # Field
        self.add_risk_field_to_risk(
            risk=life_risk,
            risk_field=number_of_beneficiaries_number_risk_field,
            required=True,
            order=1,
        )

        # Risk 8
        travel_risk = Risk(
            name="International Travel Insurance",
            description="International Travel Insurance with coverage over all the period of the travel.",
            risk_category=travel_risk_category,
        )
        travel_risk.save()

        # Field
        self.add_risk_field_to_risk(
            risk=travel_risk,
            risk_field=first_name_text_risk_field,
            required=True,
            order=1,
        )

        # Field
        self.add_risk_field_to_risk(
            risk=travel_risk,
            risk_field=last_name_text_risk_field,
            required=True,
            order=1,
        )

        # Field
        self.add_risk_field_to_risk(
            risk=travel_risk,
            risk_field=date_of_birth_date_risk_field,
            required=True,
            order=1,
        )
        # Field
        enum_risk_field = RiskField(
            name="Passport Number",
            description="The number that identifies the passport",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.NUMBER),
        )
        enum_risk_field.save()

        self.add_risk_field_to_risk(
            risk=travel_risk, risk_field=enum_risk_field, required=True, order=1
        )

        # Field
        enum_risk_field = RiskField(
            name="Continent",
            description="For what continent is the travel?",
            risk_field_type=self.get_risk_field_type_by_code(RiskFieldType.ENUM),
        )
        enum_risk_field.save()

        risk_risk_field = self.add_risk_field_to_risk(
            risk=travel_risk, risk_field=enum_risk_field, required=True, order=1
        )

        # Field Options
        risk_field_enum_option_zero = RiskFieldEnumOption(name="Asia", description="")

        risk_field_enum_option_one = RiskFieldEnumOption(name="Africa", description="")

        risk_field_enum_option_two = RiskFieldEnumOption(name="Europe", description="")

        risk_field_enum_option_three = RiskFieldEnumOption(
            name="North America", description=""
        )

        risk_field_enum_option_four = RiskFieldEnumOption(
            name="South America", description=""
        )

        risk_field_enum_option_five = RiskFieldEnumOption(
            name="Australia/Oceania", description=""
        )

        risk_field_enum_option_six = RiskFieldEnumOption(
            name="Antarctica", description=""
        )

        risk_field_enum_options = [
            risk_field_enum_option_zero,
            risk_field_enum_option_one,
            risk_field_enum_option_two,
            risk_field_enum_option_three,
            risk_field_enum_option_four,
            risk_field_enum_option_five,
            risk_field_enum_option_six,
        ]

        for index, risk_field_enum_option in enumerate(risk_field_enum_options):

            risk_field_enum_option.save()

            self.add_risk_field_enum_option_to_risk_risk_field(
                risk_risk_field=risk_risk_field,
                risk_field_enum_option=risk_field_enum_option,
                order=index,
            )
