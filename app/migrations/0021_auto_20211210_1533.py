# Generated by Django 2.2.24 on 2021-12-10 06:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0020_calculation_problem_solving_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculation_problem',
            name='solving_user',
        ),
        migrations.AddField(
            model_name='calculation_problem',
            name='solving_user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
