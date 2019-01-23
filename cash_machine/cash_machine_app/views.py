from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .models import Transaction, AccountUser
from .serializers import AccountUserSerializer, TransactionSerializer

# Create your views here.
class AccountUserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        user = Token.objects.get(key=self.request.auth).user
        serializer.save(user=user)