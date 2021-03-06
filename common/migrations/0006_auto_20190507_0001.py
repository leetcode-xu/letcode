# Generated by Django 2.1 on 2019-05-07 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20190505_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupCommitRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='状态')),
                ('result', models.CharField(default='', max_length=20, verbose_name='结果')),
                ('cost_time', models.IntegerField(default=-1, verbose_name='时间消耗')),
                ('cost_memory', models.IntegerField(default=-1, verbose_name='内存消耗')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交时间')),
                ('code', models.TextField(verbose_name='代码')),
                ('language', models.CharField(default='N/A', max_length=15)),
                ('is_simulation', models.IntegerField(default=False, verbose_name='是否模拟')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='common.Contest', verbose_name='比赛')),
            ],
            options={
                'verbose_name': '小组提交记录',
                'verbose_name_plural': '小组提交记录',
                'db_table': 'group_commit_record',
            },
        ),
        migrations.CreateModel(
            name='UserCommitRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='状态')),
                ('result', models.CharField(default='', max_length=20, verbose_name='结果')),
                ('cost_time', models.IntegerField(default=-1, verbose_name='时间消耗')),
                ('cost_memory', models.IntegerField(default=-1, verbose_name='内存消耗')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交时间')),
                ('code', models.TextField(verbose_name='代码')),
                ('language', models.CharField(default='N/A', max_length=15)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usercommitrecord', to='common.Problem', verbose_name='题目编号')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '个人提交记录',
                'verbose_name_plural': '个人题提交记录',
                'db_table': 'user_commit_record',
            },
        ),
        migrations.RemoveField(
            model_name='contestcommitrecord',
            name='contest',
        ),
        migrations.RemoveField(
            model_name='contestcommitrecord',
            name='group',
        ),
        migrations.RemoveField(
            model_name='contestcommitrecord',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='problemcommitrecord',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='problemcommitrecord',
            name='user',
        ),
        migrations.AlterField(
            model_name='doubtcomment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doubtcomment_replied', to=settings.AUTH_USER_MODEL, verbose_name='回复'),
        ),
        migrations.AlterField(
            model_name='group',
            name='people_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='problemcomment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='problemcomment_replied', to=settings.AUTH_USER_MODEL, verbose_name='回复'),
        ),
        migrations.DeleteModel(
            name='ContestCommitRecord',
        ),
        migrations.DeleteModel(
            name='ProblemCommitRecord',
        ),
        migrations.AddField(
            model_name='groupcommitrecord',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='common.Group', verbose_name='队伍'),
        ),
        migrations.AddField(
            model_name='groupcommitrecord',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupcommitrecord', to='common.Problem', verbose_name='题目编号'),
        ),
    ]
