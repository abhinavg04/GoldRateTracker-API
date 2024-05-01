# from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
r = DefaultRouter()
r.register('adduser',UserView,basename='adduser')

urlpatterns = [

]+r.urls
