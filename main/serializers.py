from . import models

from rest_framework import serializers

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attendace
        fields = '__all__'
