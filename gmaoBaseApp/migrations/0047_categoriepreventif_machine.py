# Generated by Django 4.0 on 2022-05-23 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gmaoBaseApp', '0046_alter_piecederechange_quantite'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriepreventif',
            name='machine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='gmaoBaseApp.machines'),
        ),
    ]
