# Generated by Django 2.1.5 on 2019-01-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_machine_app', '0002_bills'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='bill_list',
            field=models.TextField(default=''),
        ),
    ]