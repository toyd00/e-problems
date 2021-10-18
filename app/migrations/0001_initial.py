# Generated by Django 2.2.24 on 2021-10-14 05:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='科目名')),
                ('explain', models.TextField(max_length=400, verbose_name='科目に関する説明')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='基礎', max_length=20, verbose_name='種類名')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_num', models.IntegerField(verbose_name='選択肢の数')),
                ('made_date', models.DateField(default=datetime.date.today, verbose_name='問題作成日')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Subject', verbose_name='科目')),
                ('type', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.PROTECT, to='app.Type', verbose_name='問題の種類')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Problem')),
            ],
        ),
    ]
