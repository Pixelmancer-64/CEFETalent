# Generated by Django 4.1.3 on 2022-12-01 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0012_auto_20221127_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participante',
            name='matricula',
        ),
    ]
