# Generated by Django 4.1.4 on 2022-12-17 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidateroles_candidate', to='Candidates.candidates')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidateroles_ability', to='Candidates.roles')),
            ],
            options={
                'verbose_name_plural': 'Candidate roles',
                'unique_together': {('candidate', 'role')},
            },
        ),
    ]
