# Generated by Django 2.2.24 on 2021-10-28 06:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='いいねの数')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='いいねをしたユーザ')),
            ],
        ),
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
                ('name', models.CharField(default='基礎', max_length=20, verbose_name='問題難易度')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='次のうちから正しいものを１つ選びなさい', verbose_name='問題文')),
                ('made_date', models.DateField(default=datetime.date.today, verbose_name='問題作成日')),
                ('correct_choice', models.IntegerField(default=1, verbose_name='正解の選択肢')),
                ('like', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Like', verbose_name='いいね')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Subject', verbose_name='科目')),
                ('type', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.PROTECT, to='app.Type', verbose_name='問題の難易度')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Problem')),
            ],
        ),
    ]
