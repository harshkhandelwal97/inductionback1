# Generated by Django 3.2.18 on 2024-01-31 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ind', '0004_auto_20240131_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image1',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='member',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='member',
            name='image3',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
