# Generated by Django 2.2.24 on 2021-11-19 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_auto_20211118_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='solving_user',
            field=models.ManyToManyField(related_name='問題を解いたユーザ', to=settings.AUTH_USER_MODEL, verbose_name='問題を解いたユーザ'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='問題を作成したユーザ', to=settings.AUTH_USER_MODEL, verbose_name='問題を作成したユーザ'),
        ),
    ]