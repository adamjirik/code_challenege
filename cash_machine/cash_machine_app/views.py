from rest_framework import viewsets
from rest_framework.response import Response

from .models import Transaction, Bill, AccountUser
from .utils.utils import get_notes
from .serializers import AccountUserSerializer, TransactionSerializer

# Create your views here.
class AccountUserViewSet(viewsets.ModelViewSet):
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


    """
    Create (POST) has to be overwritten since rest_framework serializers
    by default have nested relations as read only. The transaction object
    must first be created in order to add the correct Bills to it, and then
    serialized to be returned as a JSON.
    """
    def create(self, request, *args, **kwargs):
        amount = int(request.data['amount'])
        user = AccountUser.objects.first()
        transaction = Transaction.objects.create(amount=amount, user=user)
        denominations = get_notes(amount)
        bill_list = str(denominations)
        transaction.bill_list = bill_list
        for denom in denominations:
            bill= Bill.objects.get(denomination=denom)
            transaction.bills.add(bill)
        transaction.save()
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)