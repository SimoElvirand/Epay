# Generated by Django 4.0 on 2022-02-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salaireBase', models.IntegerField(null=True)),
                ('salaireBrut', models.IntegerField(null=True)),
                ('salaireNet', models.IntegerField(null=True)),
                ('aCompte', models.IntegerField(null=True)),
                ('salaireCotisable', models.IntegerField(null=True)),
                ('salaireTaxable', models.IntegerField(null=True)),
                ('irpp', models.FloatField(null=True)),
                ('cnps', models.FloatField(null=True)),
                ('cac', models.FloatField(null=True)),
                ('cfc', models.FloatField(null=True)),
                ('crtv', models.IntegerField(null=True)),
                ('tc', models.IntegerField(null=True)),
                ('indemniteRepresentation', models.IntegerField(null=True)),
                ('indemniteTransport', models.IntegerField(null=True)),
            ],
        ),
    ]