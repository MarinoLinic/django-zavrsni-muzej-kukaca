# Generated by Django 3.2.8 on 2022-02-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_kukac_slika'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kukac',
            name='slika',
            field=models.ImageField(upload_to='images'),
        ),
    ]
