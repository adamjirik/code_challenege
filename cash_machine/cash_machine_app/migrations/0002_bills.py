# Generated by Django 2.1.5 on 2019-01-20 23:22

import cash_machine_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_machine_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.IntegerField()),
            ],
        ),
        migrations.AlterModelManagers(
            name='accountuser',
            managers=[
                ('objects', cash_machine_app.models.AccountUserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='account_number',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='bills',
            field=models.ManyToManyField(to='cash_machine_app.Bill'),
        ),
    ]
