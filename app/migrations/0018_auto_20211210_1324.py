# Generated by Django 2.2.24 on 2021-12-10 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20211210_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation_Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_count', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='problem',
            name='school_year',
        ),
        migrations.DeleteModel(
            name='SchoolYear',
        ),
    ]
