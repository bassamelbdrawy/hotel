# Generated by Django 2.2.7 on 2020-03-15 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='pic',
            field=models.ImageField(upload_to='booking/images/'),
        ),
    ]