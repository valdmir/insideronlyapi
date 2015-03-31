from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from restapi.models import Company,NationalHoliday
from rest_framework import viewsets
from restapi.serializer import UserSerializer, GroupSerializer,CompanySerializer,NationalHolidaySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class NationalHolidayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = NationalHoliday.objects.all()
    serializer_class = NationalHolidaySerializer
