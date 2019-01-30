# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KAAM', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill_user',
            name='Name',
        ),
        migrations.AddField(
            model_name='skill_user',
            name='affinity',
            field=models.IntegerField(default=1, verbose_name=b'Affinity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill_user',
            name='skills',
            field=models.IntegerField(default=1, verbose_name=b'Skills 0=no 10=expert'),
            preserve_default=False,
        ),
    ]
