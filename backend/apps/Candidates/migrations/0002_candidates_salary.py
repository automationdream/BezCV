# Generated by Django 4.1.4 on 2022-12-23 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='salary',
            field=models.CharField(default='4000-5000', max_length=255),
            preserve_default=False,
        ),
    ]