# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('KAAM', '0003_auto_20170331_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='competenceteam',
            name='TeamLead',
            field=models.ForeignKey(default=1, verbose_name=b'The Teamlead of this team', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
