# Generated by Django 3.2.9 on 2022-01-05 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('flat', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]