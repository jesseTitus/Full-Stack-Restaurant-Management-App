# Generated by Django 5.0.5 on 2024-05-07 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_menu_category_id_alter_menu_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menucategory',
            old_name='menu_category_name',
            new_name='category',
        ),
    ]