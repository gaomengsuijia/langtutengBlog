# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-13 09:15
from __future__ import unicode_literals

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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('head_img', models.ImageField(upload_to='uploads')),
                ('content', models.TextField(max_length=5000)),
                ('summary', models.CharField(max_length=255)),
                ('publish_date', models.DateTimeField(auto_now=True)),
                ('hidden', models.BooleanField()),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categroy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('comment_date', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Article')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_comment', to='myblog.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Fanjia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=50, unique=True)),
                ('sara', models.CharField(max_length=50, unique=True)),
                ('fanjia', models.CharField(max_length=50, unique=True)),
                ('bili', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThumbUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Article')),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('group', models.ManyToManyField(to='myblog.UserGroup')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='thumbup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.UserProfile'),
        ),
        migrations.AddField(
            model_name='categroy',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.UserProfile'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.UserProfile'),
        ),
        migrations.AddField(
            model_name='article',
            name='categroy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Categroy'),
        ),
    ]
