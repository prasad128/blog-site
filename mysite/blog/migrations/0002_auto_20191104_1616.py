# Generated by Django 2.2 on 2019-11-04 16:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 4, 16, 16, 20, 895612, tzinfo=utc)),
        ),
    ]