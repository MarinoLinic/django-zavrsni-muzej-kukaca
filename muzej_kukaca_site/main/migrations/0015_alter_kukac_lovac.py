# Generated by Django 3.2.8 on 2022-02-21 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0014_kukac_datum_sakupljanja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kukac',
            name='lovac',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
