# Generated by Django 2.1.4 on 2019-03-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0007_auto_20190304_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='commitrecord',
            name='language',
            field=models.CharField(default='N/A', max_length=15),
        ),
    ]