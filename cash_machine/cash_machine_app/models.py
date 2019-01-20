from random import randint

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.

class AccountUserManager(UserManager):
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
        while True:
            new_number = randint(1000000000, 9999999999)
            if len(AccountUser.objects.filter(account_number=new_number)) == 0:
                account_number = new_number
                break

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
        while True:
            new_number = randint(1000000000, 9999999999)
            if len(AccountUser.objects.filter(account_number=new_number)) == 0:
                account_number = new_number
                break

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


class Transaction(models.Model):
    amount = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
