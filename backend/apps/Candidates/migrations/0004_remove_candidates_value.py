# Generated by Django 4.1.4 on 2022-12-16 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0003_alter_candidates_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidates',
            name='value',
        ),
    ]