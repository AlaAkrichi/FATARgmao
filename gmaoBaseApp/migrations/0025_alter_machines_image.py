# Generated by Django 4.0 on 2022-04-20 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmaoBaseApp', '0024_alter_machines_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='image',
            field=models.FileField(blank=True, default='', null=True, upload_to=''),
        ),
    ]
