# Generated by Django 3.0.7 on 2020-07-09 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_remove_report_cur_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='cur_date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=False,
        ),
    ]