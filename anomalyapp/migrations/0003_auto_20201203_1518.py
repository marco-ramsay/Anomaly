# Generated by Django 3.1.4 on 2020-12-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anomalyapp', '0002_auto_20201203_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anomaly',
            name='date_created',
        ),
        migrations.AddField(
            model_name='anomaly',
            name='DateTime',
            field=models.DateTimeField(null=True),
        ),
    ]
