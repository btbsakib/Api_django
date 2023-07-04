from rest_framework import serializers
from myapp.models import Contact,LeaveRequest

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields ='__all__'

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=LeaveRequest
        fields='__all__'

class LeavebySerializer(serializers.ModelSerializer):
    leaverequests = LeaveSerializer(many=True, read_only=True)
    class Meta:
        model=Contact
        fields=['first_name','last_name','email','leaverequests']