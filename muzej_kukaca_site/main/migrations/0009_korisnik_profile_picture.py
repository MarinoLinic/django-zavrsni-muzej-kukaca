# Generated by Django 3.2.8 on 2022-02-11 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_kukac_slika'),
    ]

    operations = [
        migrations.AddField(
            model_name='korisnik',
            name='profile_picture',
            field=models.ImageField(default='0', upload_to='images/'),
        ),
    ]
