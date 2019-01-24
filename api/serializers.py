from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models.states import State, StateRevenue
from api.models.counties import County, CountyRevenue

# Taken from SO: https://stackoverflow.com/questions/23643204/django-rest-framework-dynamically-return-subset-of-fields
class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class StateSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('FIPS_Code_State', 'Name')


class StateRevenueSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = StateRevenue
        fields = ('State_id', 'Name', 'Year', 'Population', 'Total_Revenue', 'Total_Taxes', 'Tot_Sales_Gr_Rec_Tax', 'Total_License_Taxes', 'Total_Income_Taxes', 'Death_and_Gift_Tax', 'Docum_and_Stock_Tr_Tax', 'Severance_Tax', 'Taxes_NEC')
    
    # def to_representation(self, data):
    #     res = super(StateRevenueSerializer, self).to_representation(data)
    #     return {res['State_id']: res}


class CountySerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = County
        fields = ('State_id', 'FIPS_County', 'Name', 'GFD_ID')


class CountyRevenueSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = CountyRevenue
        many = False
        fields = ('County_id', 'Name', 'Year', 'Population', 'Total_Revenue', 'Total_Taxes', 'Tot_Sales_Gr_Rec_Tax', 'Total_License_Taxes', 'Total_Income_Taxes', 'Death_and_Gift_Tax', 'Docum_and_Stock_Tr_Tax', 'Severance_Tax', 'Taxes_NEC')

    def to_representation(self, data):
        res = super(CountyRevenueSerializer, self).to_representation(data)
        return {res['County_id']: res}
