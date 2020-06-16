from rest_framework import serializers
from serviceRequest.models import BorrowFacility, EntrustLaundryToWash, ParkingSpaceApplication

class BorrowFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowFacility
        fields = '__all__'

class EntrustLaundryToWashSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrustLaundryToWash
        fields = '__all__'

class ParkingSpaceApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpaceApplication
        fields = '__all__'