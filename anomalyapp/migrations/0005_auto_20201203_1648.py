# Generated by Django 3.1.4 on 2020-12-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anomalyapp', '0004_auto_20201203_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='vessel',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
