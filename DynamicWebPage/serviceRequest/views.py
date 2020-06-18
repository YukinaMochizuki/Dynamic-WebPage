from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from serviceRequest.models import BorrowFacility, EntrustLaundryToWash, ParkingSpaceApplication
from serviceRequest.serializers import BorrowFacilitySerializer, EntrustLaundryToWashSerializer, ParkingSpaceApplicationSerializer

from event.models import Event

@csrf_exempt
def BorrowFacilityRequest(request):
    if request.method == 'POST':
            
            Event.objects.create(
                owner=request.user.username,
                eventType= "BorrowFacility",
                context= "場地借用：" + request.POST['facilityName'] + "，從 " + request.POST['startTime'] + ' 開始，借用時間 ' + request.POST['lengthOfTime'],
                status="等待審核"
            )

            return HttpResponse(status=201)
    return HttpResponse(status=401)

@csrf_exempt
def EntrustLaundryToWashRequest(request):
    if request.method == 'POST':
            
            Event.objects.create(
                owner=request.user.username,
                eventType= "EntrustLaundryToWash",
                context= "送洗衣物類型：" + request.POST['type'] + "，預計收取時間： " + request.POST['returnClothesTime'] + '，備註：' + request.POST['remark'],
                status="處理中"
            )

            return HttpResponse(status=201)
    return HttpResponse(status=401)

@csrf_exempt
def ParkingSpaceApplicationRequest(request):
    if request.method == 'POST':
            
            Event.objects.create(
                owner=request.user.username,
                eventType= "ParkingSpaceApplication",
                context= "申請車位類型：" + request.POST['type'] + "，期望的車位區域：" + request.POST['desiredLocation'],
                status="等待審核"
            )

            return HttpResponse(status=201)
    return HttpResponse(status=401)

