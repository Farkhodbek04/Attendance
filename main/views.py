from . import models
from . import serializers
from datetime import date

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def staff_list(request):
    staffs = models.Staff.objects.all()
    staff_ser = serializers.StaffSerializer(staffs, many=True)
    return Response(staff_ser.data)

@api_view(['POST'])
def create_staff(request):
    f_name = request.data.get('f_name')
    l_name = request.data.get('l_name')
    status = request.data.get('status')
    tel_num = request.data.get('tel_num')
    staff = models.Staff.objects.create(
        f_name=f_name,
        l_name=l_name,
        status=status,
        tel_num=tel_num
    )
    staff_ser = serializers.StaffSerializer(data=staff)
    if staff_ser.is_valid():
        return Response(staff_ser.data)

@api_view(['POST'])
def create_attendance(request, id):
    staff = models.Staff.objects.get(id=id)
    attendance = models.Attendace.objects.create(staff=staff, presence=True)
    attendance_ser = serializers.AttendanceSerializer(data=attendance)
    if attendance_ser.is_valid():
        return Response(attendance_ser.data)
    
@api_view(['GET'])
def daily_attendance(request):
    staffs = models.Attendace.objects.filter(presence=True, arrival_time = date.day)
    staff_ser = serializers.AttendanceSerializer(staffs, many=True)
    print(staff_ser)
    return Response(staff_ser.data)



    





