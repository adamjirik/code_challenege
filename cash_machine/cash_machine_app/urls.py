from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from .views import *

router = routers.DefaultRouter()
router.register(r'users', AccountUserViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('getToken/', views.obtain_auth_token),
    path('auth/', include('rest_framework.urls'))
] +  router.urls
