from .models import AccountUser, Transaction, Bill
from rest_framework import serializers


class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = ('username', 'first_name', 'last_name', 'email', 'account_number',)


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('denomination',)


class TransactionSerializer(serializers.ModelSerializer):
    bills = BillSerializer(many=True, read_only=True)

    class Meta:
        model = Transaction
        fields = ('amount', 'date', 'bills',)