# Generated by Django 2.2.7 on 2020-03-21 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_auto_20200321_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_information',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
