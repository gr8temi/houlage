# Generated by Django 2.0.7 on 2019-05-06 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pickup_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='order',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
