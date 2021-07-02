from django.urls import path
from trade.views import ApikeyList, ApikeyDetail ,ApikeyPost

urlpatterns = [
    path('<int:pk>/', ApikeyDetail.as_view()),
    path('', ApikeyList.as_view()),
    path('add/',ApikeyPost.as_view()),
]


