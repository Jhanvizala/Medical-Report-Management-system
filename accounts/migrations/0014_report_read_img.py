# Generated by Django 3.0.7 on 2020-07-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_report_read_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='read_img',
            field=models.TextField(default='SOME STRING'),
        ),
    ]
