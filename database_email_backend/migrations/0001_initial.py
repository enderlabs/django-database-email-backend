# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import models, migrations
import database_email_backend.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('content', database_email_backend.fields.Base64Field(default=None, null=True, db_column='content', blank=True)),
                ('mimetype', models.CharField(default=None, max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('from_email', models.CharField(default='', max_length=255, blank=True)),
                ('to_emails', models.TextField(default='', blank=True)),
                ('cc_emails', models.TextField(default='', blank=True)),
                ('bcc_emails', models.TextField(default='', blank=True)),
                ('all_recipients', models.TextField(default='', blank=True)),
                ('headers', models.TextField(default='', blank=True)),
                ('subject', models.TextField(default='', blank=True)),
                ('body', models.TextField(default='', blank=True)),
                ('raw', models.TextField(default='', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='attachment',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='database_email_backend.Email'),
        ),
        migrations.CreateModel(
            name='SendEmail',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('database_email_backend.email',),
        ),
    ]
