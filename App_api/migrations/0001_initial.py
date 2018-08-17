# Generated by Django 2.1 on 2018-08-17 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App_api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionname', models.CharField(max_length=64, verbose_name='模块名称')),
                ('sectiondesc', models.CharField(max_length=200, verbose_name='模块描述')),
                ('sectionmake', models.CharField(max_length=200, verbose_name='模块负责人')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='船舰时间')),
            ],
            options={
                'verbose_name': '模块管理',
                'verbose_name_plural': '模块管理',
            },
        ),
    ]
