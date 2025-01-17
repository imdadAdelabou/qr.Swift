# Generated by Django 4.0.6 on 2022-08-12 07:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qr_gen', '0009_alter_qr_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='qr',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qrs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='qr',
            name='name',
            field=models.CharField(default=datetime.date(2022, 8, 12), max_length=200),
        ),
    ]
