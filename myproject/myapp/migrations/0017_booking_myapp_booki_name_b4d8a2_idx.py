# Generated by Django 5.0.5 on 2024-05-15 17:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_delete_logger'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name='booking',
            index=models.Index(fields=['name'], name='myapp_booki_name_b4d8a2_idx'),
        ),
    ]
