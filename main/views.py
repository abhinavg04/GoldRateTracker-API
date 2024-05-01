from django.shortcuts import render
from .serializers import GoldRateSerializer
from rest_framework.viewsets import ViewSet
from .models import GoldRate
from rest_framework.response import Response
from datetime import datetime

# Create your views here.

class GoldView(ViewSet):
    def list(self,request):
        if 'date' in request.query_params:
            date_str = request.query_params.get('date')
            # print(date_str)
            # added_date = datetime.strptime(date_str,"%Y-%m-%d")
            goldrate = GoldRate.objects.filter(added_date=date_str)
            ser = GoldRateSerializer(goldrate,many=True)
            return Response(data=ser.data)
        if 'start_date' in request.query_params and 'end_date' in request.query_params:
            start_date = request.query_params.get('start_date')
            end_date = request.query_params.get('end_date')
            print(start_date,end_date)
            goldrate = GoldRate.objects.filter(added_date__range=[start_date,end_date])
            ser = GoldRateSerializer(goldrate,many=True)
            return Response(data=ser.data)
        goldrate = GoldRate.objects.all()
        ser = GoldRateSerializer(goldrate,many=True)
        return Response(ser.data)
       