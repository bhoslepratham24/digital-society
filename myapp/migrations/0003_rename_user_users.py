# Generated by Django 4.0.1 on 2022-02-17 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_emergency_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]
