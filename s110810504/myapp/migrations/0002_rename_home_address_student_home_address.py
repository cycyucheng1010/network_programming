# Generated by Django 4.0.2 on 2022-03-23 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='home_Address',
            new_name='Home_Address',
        ),
    ]
