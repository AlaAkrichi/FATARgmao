# Generated by Django 4.0 on 2022-04-18 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gmaoBaseApp', '0022_rename_schudledtiem_machines_schudledtime_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machines',
            old_name='currnetState',
            new_name='currentState',
        ),
    ]
