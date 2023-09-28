# Generated by Django 4.2.5 on 2023-09-28 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20230928_0931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='home_image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_created',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2023, 9, 28, 10, 31, 10, 278701, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_updated',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2023, 9, 28, 10, 31, 10, 278716, tzinfo=datetime.timezone.utc)),
        ),
    ]
