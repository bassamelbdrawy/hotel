# Generated by Django 2.2.7 on 2020-03-24 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0020_auto_20200324_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='from_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 24, 14, 27, 50, 991450)),
        ),
        migrations.AlterField(
            model_name='books',
            name='to_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 24, 14, 27, 50, 991450)),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='lat',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='longtude',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
