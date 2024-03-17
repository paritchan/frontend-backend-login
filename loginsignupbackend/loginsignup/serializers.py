from rest_framework import serializers
from .models import loginsignup

class loginsignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = loginsignup
        fields = ('name','email','password','dlnum','permitnum')