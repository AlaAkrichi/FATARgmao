# Generated by Django 4.0 on 2022-05-22 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmaoBaseApp', '0045_rename_prixtotale_piecederechange_prixunitaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piecederechange',
            name='quantite',
            field=models.FloatField(blank=True),
        ),
    ]
