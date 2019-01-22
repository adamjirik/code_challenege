from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('user', AccountUserViewSet)

urlpatterns = [
    path('transaction', TransactionViewSet.as_view({'post': 'create'}))
]