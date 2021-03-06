# Generated by Django 3.0.8 on 2020-07-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HubuUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('username', models.BigIntegerField(verbose_name='username')),
                ('password', models.CharField(max_length=32, verbose_name='password')),
                ('nickName', models.CharField(max_length=32, verbose_name='nickName')),
                ('realName', models.CharField(max_length=8, verbose_name='realName')),
                ('sex', models.BooleanField(verbose_name='sex')),
                ('birthday', models.DateField(verbose_name='生日')),
                ('englishName', models.CharField(max_length=16, verbose_name='英文名称')),
                ('nation', models.CharField(max_length=16, verbose_name='民族')),
                ('avatar', models.CharField(max_length=255, verbose_name='头像')),
                ('image', models.CharField(max_length=255, verbose_name='全身照')),
                ('phone', models.CharField(max_length=16, verbose_name='电话')),
                ('email', models.CharField(max_length=32, verbose_name='邮箱')),
                ('university', models.CharField(max_length=32, verbose_name='大学')),
                ('profession', models.CharField(max_length=32, verbose_name='专业')),
                ('address', models.CharField(max_length=32, verbose_name='现居城市')),
                ('synopsis', models.CharField(max_length=128, verbose_name='简介')),
                ('description', models.CharField(max_length=511, verbose_name='详细描述')),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('modifyTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'hubu_users',
            },
        ),
    ]
