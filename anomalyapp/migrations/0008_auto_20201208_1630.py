# Generated by Django 3.1.4 on 2020-12-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anomalyapp', '0007_auto_20201208_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='anomaly',
            name='review_status',
            field=models.CharField(choices=[('Client_signed', 'Client_signed'), ('Not_Signed', 'Not_Signed')], default='Not_Signed', max_length=200),
        ),
        migrations.AlterField(
            model_name='anomaly',
            name='image_1',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='anomaly',
            name='image_1_description',
            field=models.CharField(blank=True, default='Image_1', max_length=200),
        ),
        migrations.AlterField(
            model_name='anomaly',
            name='image_2',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='anomaly',
            name='image_2_description',
            field=models.CharField(blank=True, default='Image_2', max_length=200),
        ),
        migrations.AlterField(
            model_name='anomaly',
            name='video',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='anomaly',
            name='video_description',
            field=models.CharField(blank=True, default='Anomaly Video', max_length=200),
        ),
    ]
