from django.conf.urls import patterns, include, url
from django.contrib import admin
# from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from restapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'nationalholiday', views.NationalHolidayViewSet)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'insideronlyapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
