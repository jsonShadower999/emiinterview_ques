from rest_framework import  serializers

from calculator.models import Enroller 

class  EnrollerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Enroller 
        fields="__all__"