# Generated by Django 4.0 on 2022-02-08 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employé', '0003_remove_employé_salaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='employé',
            name='sexe',
            field=models.CharField(choices=[('Maxculin', 'Maxculin'), ('Féminin', 'Féminin')], max_length=10, null=True),
        ),
    ]
