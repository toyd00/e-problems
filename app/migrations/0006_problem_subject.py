# Generated by Django 2.2.24 on 2021-09-13 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_problem_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='subject',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, to='app.Subject'),
            preserve_default=False,
        ),
    ]
