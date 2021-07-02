from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Apikey

class ApikeySerializer(serializers.ModelSerializer):

    class Meta:
        # fields = ()
        fields = '__all__'
        model = Apikey