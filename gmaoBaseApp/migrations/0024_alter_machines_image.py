# Generated by Django 4.0 on 2022-04-18 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmaoBaseApp', '0023_rename_currnetstate_machines_currentstate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
