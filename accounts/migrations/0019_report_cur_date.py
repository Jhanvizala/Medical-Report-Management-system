# Generated by Django 3.0.7 on 2020-07-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_report_read_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='cur_date',
            field=models.DateField(auto_now=True),
        ),
    ]