# Generated by Django 4.2.21 on 2025-05-29 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_no_of_guests_alter_menu_inventory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='MenuItem',
        ),
    ]
