from rest_framework import generics, serializers #, permissions
from .models import Profile
from .serializers import ProfileSerializer
# from .permissions import IsWriterOrReadOnly # new
# Create your views here.

# class ApikeyList(generics.ListAPIView):
# class ApikeyList(generics.CreateAPIView):
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated) # new view level authenticated on view level
    # permission_classes = (IsWriterOrReadOnly) # new
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
