# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KAAM', '0006_auto_20170425_1225'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='competenceteam',
            unique_together=set([('Name', 'company')]),
        ),
    ]
