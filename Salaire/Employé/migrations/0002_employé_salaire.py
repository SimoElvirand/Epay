# Generated by Django 4.0 on 2022-02-07 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Salaire', '0001_initial'),
        ('Employé', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employé',
            name='Salaire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Empoyee_Salary', to='Salaire.salaire'),
        ),
    ]
