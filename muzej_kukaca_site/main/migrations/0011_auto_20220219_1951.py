# Generated by Django 3.2.8 on 2022-02-19 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20220211_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='kukac',
            name='izbrisi',
            field=models.TextField(default='0'),
        ),
        migrations.AddField(
            model_name='kukac',
            name='uredi',
            field=models.TextField(default='0'),
        ),
    ]