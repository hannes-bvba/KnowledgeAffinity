# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('KAAM', '0002_auto_20170328_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill_user',
            name='affinity',
            field=models.IntegerField(verbose_name=b'Affinity', choices=[(0, b'No affinity'), (1, b'interested'), (2, b'Very interested')]),
        ),
        migrations.AlterField(
            model_name='skill_user',
            name='skills',
            field=models.IntegerField(verbose_name=b'Skills 0=no 10=expert', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
