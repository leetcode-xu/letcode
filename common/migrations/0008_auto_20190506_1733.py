# Generated by Django 2.1 on 2019-05-06 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20190506_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='common.Group'),
        ),
    ]
