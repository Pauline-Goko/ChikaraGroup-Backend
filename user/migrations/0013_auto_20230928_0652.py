# Generated by Django 3.2.12 on 2023-09-28 06:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20230928_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_created',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2023, 9, 28, 6, 52, 2, 228723, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_updated',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2023, 9, 28, 6, 52, 2, 228741, tzinfo=utc)),
        ),
    ]
