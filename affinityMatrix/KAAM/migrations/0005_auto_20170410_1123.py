# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KAAM', '0004_competenceteam_teamlead'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill_ct',
            old_name='company',
            new_name='skill',
        ),
    ]
