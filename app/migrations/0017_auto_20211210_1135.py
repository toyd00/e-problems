# Generated by Django 2.2.24 on 2021-12-10 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_problem_school_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='school_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.SchoolYear'),
        ),
    ]