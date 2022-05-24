# Generated by Django 4.0 on 2022-05-23 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gmaoBaseApp', '0048_remove_interventionpreventive_planintervention_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervenctioncurative',
            name='machine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gmaoBaseApp.machines'),
        ),
        migrations.AlterField(
            model_name='interventionpreventive',
            name='machine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gmaoBaseApp.machines'),
        ),
    ]
