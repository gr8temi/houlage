# Generated by Django 2.0.7 on 2019-06-04 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0004_auto_20190514_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='driver',
        ),
    ]