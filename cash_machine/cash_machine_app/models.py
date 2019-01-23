from random import randint

from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .utils.utils import get_notes


class AccountUserManager(UserManager):

    def generate_account_number(self):
        while True:
            new_number = randint(1000000000, 9999999999)
            if len(AccountUser.objects.filter(account_number=new_number)) == 0:
                account_number = new_number
                break
        return account_number


    def create_user(self, username, email=None, password=None, **extra_fields):
        if not email:
            msg = "Email address is required"
            raise ValueError(msg)

        if len(password) < 8:
            msg = "Password must be at least 8 characters long"
            raise ValueError(msg)

        """
        Generate a new account number 
        """
        account_number = self.generate_account_number()

        user = self.model(
            username=username,
            email=email,
            account_number=account_number
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        if not email:
            msg = "Email address is required"
            raise ValueError(msg)

        if len(password) < 8:
            msg = "Password must be at least 8 characters long"
            raise ValueError(msg)

        """
        Generate a new account number 
        """
        account_number = self.generate_account_number()

        user = self.model(
            username=username,
            email=email,
            account_number=account_number
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class AccountUser(AbstractUser):
    account_number = models.BigIntegerField(unique=True)
    objects = AccountUserManager()

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


class Bill(models.Model):
    denomination = models.IntegerField()

class Transaction(models.Model):
    amount = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    bills = models.ManyToManyField(Bill) # Only creates relation to types of bills used
    bill_list = models.TextField(default='') # Convert list to str


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
            # user = AccountUser.objects.first() # user should be changed once authentitcation is implemented
            # self.user = user
            denominations = get_notes(self.amount)
            self.bill_list = str(denominations)
            super(Transaction, self).save()
            for denom in denominations:
                bill = Bill.objects.get(denomination=denom)
                self.bills.add(bill)
