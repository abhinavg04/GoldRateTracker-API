from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
r = DefaultRouter()
r.register('goldrate',GoldView,basename='goldrate')

urlpatterns = [

]+r.urls