# Generated by Django 4.1.4 on 2022-12-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, unique=True),
        ),
    ]