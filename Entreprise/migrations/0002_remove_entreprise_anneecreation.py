# Generated by Django 4.0 on 2022-02-08 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Entreprise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entreprise',
            name='anneeCreation',
        ),
    ]
