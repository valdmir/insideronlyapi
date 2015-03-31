from django.contrib.auth.models import User,Group
from rest_framework import serializers
from restapi.models import Company,NationalHoliday

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=('url','name')
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields=('url','id','name','email','use_expired_date')
class NationalHolidaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=NationalHoliday
        fields=('url','id','date','description','flag')
