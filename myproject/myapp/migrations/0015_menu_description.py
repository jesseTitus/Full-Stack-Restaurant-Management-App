# Generated by Django 5.0.5 on 2024-05-10 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_menu_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.CharField(default='-', max_length=200),
            preserve_default=False,
        ),
    ]