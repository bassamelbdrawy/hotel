# Generated by Django 2.2.7 on 2020-03-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
