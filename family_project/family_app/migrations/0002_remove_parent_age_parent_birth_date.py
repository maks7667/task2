# Generated by Django 5.0.7 on 2024-08-04 17:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='age',
        ),
        migrations.AddField(
            model_name='parent',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
