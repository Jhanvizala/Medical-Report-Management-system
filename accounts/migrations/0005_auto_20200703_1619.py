# Generated by Django 3.0.7 on 2020-07-03 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='read',
            name='read_img',
            field=models.CharField(max_length=1000),
        ),
    ]