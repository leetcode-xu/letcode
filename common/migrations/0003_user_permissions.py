# Generated by Django 2.1.7 on 2019-04-22 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20190417_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='permissions',
            field=models.IntegerField(default=0),
        ),
    ]