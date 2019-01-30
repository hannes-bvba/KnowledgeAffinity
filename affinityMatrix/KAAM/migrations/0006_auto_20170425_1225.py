# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KAAM', '0005_auto_20170410_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill_user',
            name='affinity',
            field=models.IntegerField(verbose_name=b'Affinity', choices=[(0, b' '), (1, b'interested'), (2, b'Very interested')]),
        ),
        migrations.AlterUniqueTogether(
            name='skill',
            unique_together=set([('Name', 'company')]),
        ),
    ]
