# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CenterWater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_d', models.DateField(auto_now_add=True, verbose_name='抄表日期')),
                ('m3', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='用水数量')),
                ('ps', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注信息')),
                ('price', models.DecimalField(decimal_places=2, default=3.6, help_text='水费单价，默认是3.6元/m3', max_digits=5, verbose_name='单价')),
                ('is_pay', models.BooleanField(default=False, verbose_name='已缴费')),
            ],
            options={
                'verbose_name': '总表信息',
                'verbose_name_plural': '总表信息',
                'ordering': ['-mark_d'],
                'get_latest_by': 'mark_d',
            },
        ),
        migrations.CreateModel(
            name='WaterNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, max_length=28, null=True, verbose_name='描述')),
                ('create_d', models.DateTimeField(auto_now_add=True, verbose_name='录入日期')),
                ('update_d', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否注销')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='water_num', to='account.Account', verbose_name='所属户号')),
            ],
            options={
                'verbose_name': '水表号',
                'verbose_name_plural': '水表号',
            },
        ),
        migrations.CreateModel(
            name='WaterRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m3', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='用水数量')),
                ('ps', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注信息')),
                ('is_pay', models.BooleanField(default=False, verbose_name='已缴费')),
                ('create_d', models.DateTimeField(auto_now_add=True, verbose_name='录入日期')),
                ('update_d', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('WaterNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='livingcost.WaterNum', verbose_name='水表号码')),
                ('mark_d', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_rate', to='livingcost.CenterWater', verbose_name='抄表日期')),
            ],
            options={
                'verbose_name': '水费',
                'verbose_name_plural': '水费',
            },
        ),
    ]