# Generated by Django 4.0 on 2022-02-08 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entreprise', '0002_remove_entreprise_anneecreation'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreprise',
            name='anneeCreation',
            field=models.IntegerField(null=True),
        ),
    ]
