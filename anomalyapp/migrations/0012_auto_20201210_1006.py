# Generated by Django 3.1.4 on 2020-12-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anomalyapp', '0011_anomaly_criticality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anomaly',
            name='criticality',
            field=models.CharField(choices=[('Select', 'Select'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Select', max_length=200),
        ),
    ]
