from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class UserView(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self,request):
        ser = UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"User created"},status=status.HTTP_201_CREATED)
        return Response({"msg":ser.errors},status=status.HTTP_406_NOT_ACCEPTABLE)