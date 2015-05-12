# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Profilepic', models.FileField(upload_to=b'/media/pics/dp/')),
                ('Coverpic', models.FileField(upload_to=b'/media/pics/cp/')),
                ('user', models.ForeignKey(to='login.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Enroll', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99999999), django.core.validators.MinValueValidator(1)])),
                ('email', models.EmailField(max_length=75)),
                ('user', models.ForeignKey(to='login.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
