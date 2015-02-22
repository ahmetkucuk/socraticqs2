# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ct', '0011_auto_20150129_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAttributes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(max_length=10)),
                ('field', models.CharField(default=b'Unknown', max_length=10)),
                ('study_level', models.CharField(default=b'Unknown', max_length=10)),
                ('knowledge_level', models.IntegerField(max_length=10)),
                ('atime', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'time submitted')),
                ('course', models.ForeignKey(to='ct.Course')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
