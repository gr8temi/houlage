# Generated by Django 2.0.7 on 2019-06-30 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_auto_20190604_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]