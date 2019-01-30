# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ownedObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=30, verbose_name=b'Name')),
            ],
        ),
        migrations.CreateModel(
            name='Skill_CT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=30, verbose_name=b'Name')),
                ('company', models.ForeignKey(verbose_name=b'Skill/Affinity', to='KAAM.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Skill_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=30, verbose_name=b'Name')),
                ('skill', models.ForeignKey(verbose_name=b'Skill/Affinity', to='KAAM.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('ownedobject_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='KAAM.ownedObject')),
                ('Name', models.CharField(max_length=30, verbose_name=b'Name')),
            ],
            bases=('KAAM.ownedobject',),
        ),
        migrations.CreateModel(
            name='CompetenceTeam',
            fields=[
                ('ownedobject_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='KAAM.ownedObject')),
                ('Name', models.CharField(max_length=30, verbose_name=b'Name')),
                ('company', models.ForeignKey(verbose_name=b'The company to which this team belongs', to='KAAM.Company')),
            ],
            bases=('KAAM.ownedobject',),
        ),
        migrations.AddField(
            model_name='skill_user',
            name='teamMember',
            field=models.ForeignKey(verbose_name=b'Team member', to='KAAM.TeamMember'),
        ),
        migrations.AddField(
            model_name='ownedobject',
            name='Owner',
            field=models.ForeignKey(verbose_name=b'owner of this object', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teammember',
            name='competenceTeam',
            field=models.ForeignKey(verbose_name=b'The competence team to which this user belongs', to='KAAM.CompetenceTeam'),
        ),
        migrations.AddField(
            model_name='skill_ct',
            name='competenceTeam',
            field=models.ForeignKey(verbose_name=b'The competence team to which this skill belongs', to='KAAM.CompetenceTeam'),
        ),
        migrations.AddField(
            model_name='skill',
            name='company',
            field=models.ForeignKey(verbose_name=b'The company to which this skill belongs', to='KAAM.Company'),
        ),
    ]
