# Generated by Django 4.1.4 on 2023-02-20 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0021_alter_kukac_duljina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kukac',
            name='lovac',
            field=models.ForeignKey(blank=True, default='0', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
