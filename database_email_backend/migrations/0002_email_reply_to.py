# -*- coding: utf-8 -*-

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database_email_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='reply_to',
            field=models.CharField(default='', max_length=255, blank=True),
        ),
    ]
