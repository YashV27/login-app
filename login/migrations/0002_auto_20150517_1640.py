# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_login',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userimages',
            name='Coverpic',
            field=models.FileField(upload_to=b'cp/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userimages',
            name='Profilepic',
            field=models.FileField(upload_to=b'dp/'),
            preserve_default=True,
        ),
    ]
