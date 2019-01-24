from django.contrib.auth.models import User, Group
from api.models.states import State, StateRevenue
from api.models.counties import County, CountyRevenue
from api.models.states import State, StateRevenue
from rest_framework import viewsets, generics
from .serializers import StateSerializer, StateRevenueSerializer, CountySerializer, CountyRevenueSerializer
from django.http import HttpResponse
import json

# https://www.django-rest-framework.org/api-guide/viewsets/


# Attempted this with serializers, but couldn't get the JSON response in the correct shape. For now, the return looks ugly, but should work.
def StateRevenueApiView(request):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    # import pdb; pdb.set_trace()
    # pagination_class = None
    # serializer_class = StateRevenueSerializer
    return HttpResponse(json.dumps(dict([(state['State_id'], {k: state[k] for k in state.keys() & set(request.GET.get('fields', '').split(','))}) for state in StateRevenue.objects.filter(Year=2012).values()])), content_type="application/json")

    # def get_queryset(self):
    #     # import pdb; pdb.set_trace()
    #     return dict([(state['State_id'], state) for state in StateRevenue.objects.filter(Year=2012).values()])


def CountyRevenueApiView(request):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    # pagination_class = None
    # serializer_class = CountyRevenueSerializer

    return HttpResponse(json.dumps(dict([(county['County_id'], {k: county[k] for k in county.keys() & set(request.GET.get('fields', '').split(','))}) for county in CountyRevenue.objects.filter(Year=2012).values()])), content_type="application/json")

    # def get_queryset(self):
        
    #     return CountyRevenue.objects.filter(Year=2012)
