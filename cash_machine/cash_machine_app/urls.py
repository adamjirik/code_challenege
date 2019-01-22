from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', AccountUserViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = router.urls
#     path('transaction', TransactionViewSet.as_view({'post': 'create', 'get': 'retrieve'}))
