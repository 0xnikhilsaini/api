from django.shortcuts import render
from rest_framework import generics, serializers #, permissions
from .models import Apikey
from .serializers import ApikeySerializer
# from .permissions import IsWriterOrReadOnly # new
# Create your views here.

# class ApikeyList(generics.ListCreateAPIView):
# class ApikeyList(generics.CreateAPIView):
class ApikeyList(generics.ListAPIView):
    queryset = Apikey.objects.all()
    serializer_class = ApikeySerializer

class ApikeyPost(generics.CreateAPIView):
    queryset = Apikey.objects.all()
    serializer_class = ApikeySerializer

class ApikeyDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated) # new view level authenticated on view level
    # permission_classes = (IsWriterOrReadOnly) # new
    queryset = Apikey.objects.all()
    serializer_class = ApikeySerializer
