# Generated by Django 4.1.1 on 2022-09-14 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitante',
            old_name='numero_cada',
            new_name='numero_casa',
        ),
    ]
