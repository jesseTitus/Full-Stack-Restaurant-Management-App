# Generated by Django 5.0.5 on 2024-05-08 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_item_name_menu_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('time_log', models.TimeField(help_text='dd/mm/yyyy')),
            ],
        ),
    ]
