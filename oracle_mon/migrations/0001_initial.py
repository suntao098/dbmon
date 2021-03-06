# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OracleDb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('port', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('dbname', models.CharField(max_length=255, null=True, blank=True)),
                ('db_unique_name', models.CharField(max_length=255, null=True, blank=True)),
                ('database_role', models.CharField(max_length=255, null=True, blank=True)),
                ('open_mode', models.CharField(max_length=255, null=True, blank=True)),
                ('inst_id', models.IntegerField(null=True, blank=True)),
                ('instance_name', models.CharField(max_length=255, null=True, blank=True)),
                ('host_name', models.CharField(max_length=255, null=True, blank=True)),
                ('max_process', models.IntegerField(null=True, blank=True)),
                ('current_process', models.IntegerField(null=True, blank=True)),
                ('percent_process', models.CharField(max_length=255, null=True, blank=True)),
                ('conn_rate_level', models.CharField(max_length=255, null=True, blank=True)),
                ('adg_transport_lag', models.CharField(max_length=255, null=True, blank=True)),
                ('adg_apply_lag', models.CharField(max_length=255, null=True, blank=True)),
                ('adg_transport_value', models.IntegerField(null=True, blank=True)),
                ('adg_transport_rate_level', models.CharField(max_length=255, null=True, blank=True)),
                ('adg_apply_value', models.IntegerField(null=True, blank=True)),
                ('adg_apply_rate_level', models.CharField(max_length=255, null=True, blank=True)),
                ('mon_status', models.CharField(max_length=255)),
                ('err_info', models.TextField(null=True, blank=True)),
                ('rate_level', models.CharField(max_length=255)),
                ('chk_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'oracle_db',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OracleDbEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('port', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('event_no', models.CharField(max_length=255)),
                ('event_name', models.CharField(max_length=255)),
                ('event_cnt', models.CharField(max_length=255)),
                ('chk_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'oracle_db_event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OracleDbHis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('port', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('dbname', models.CharField(max_length=255, null=True, blank=True)),
                ('db_unique_name', models.CharField(max_length=255, null=True, blank=True)),
                ('database_role', models.CharField(max_length=255, null=True, blank=True)),
                ('open_mode', models.CharField(max_length=255, null=True, blank=True)),
                ('inst_id', models.IntegerField(null=True, blank=True)),
                ('instance_name', models.CharField(max_length=255, null=True, blank=True)),
                ('host_name', models.CharField(max_length=255, null=True, blank=True)),
                ('max_process', models.IntegerField(null=True, blank=True)),
                ('current_process', models.IntegerField(null=True, blank=True)),
                ('percent_process', models.CharField(max_length=255, null=True, blank=True)),
                ('conn_rate_level', models.CharField(max_length=255, null=True, blank=True)),
                ('adg_transport_lag', models.CharField(max_length=255, null=True, blank=True)),
                ('adg_apply_lag', models.CharField(max_length=255, null=True, blank=True)),
                ('adg_transport_value', models.IntegerField(null=True, blank=True)),
                ('adg_transport_rate_level', models.CharField(max_length=255, null=True, blank=True)),
                ('adg_apply_value', models.IntegerField(null=True, blank=True)),
                ('adg_apply_rate_level', models.CharField(max_length=255, null=True, blank=True)),
                ('mon_status', models.CharField(max_length=255)),
                ('err_info', models.TextField(null=True, blank=True)),
                ('rate_level', models.CharField(max_length=255)),
                ('chk_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'oracle_db_his',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OracleDbRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('port', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('conn_decute', models.IntegerField()),
                ('tbs_decute', models.IntegerField()),
                ('undo_decute', models.IntegerField()),
                ('tmp_decute', models.IntegerField()),
                ('cpu_decute', models.IntegerField()),
                ('mem_decute', models.IntegerField()),
                ('disk_decute', models.IntegerField()),
                ('adg_decute', models.IntegerField()),
                ('db_rate', models.IntegerField()),
                ('db_rate_level', models.CharField(max_length=255, null=True, blank=True)),
                ('db_rate_color', models.CharField(max_length=255, null=True, blank=True)),
                ('db_rate_reason', models.CharField(max_length=255, null=True, blank=True)),
                ('rate_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'oracle_db_rate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OracleDbRateHis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('port', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('dbname_cn', models.CharField(max_length=255)),
                ('conn_decute', models.IntegerField()),
                ('tbs_decute', models.IntegerField()),
                ('undo_decute', models.IntegerField()),
                ('tmp_decute', models.IntegerField()),
                ('cpu_decute', models.IntegerField()),
                ('mem_decute', models.IntegerField()),
                ('disk_decute', models.IntegerField()),
                ('adg_decute', models.IntegerField()),
                ('db_rate', models.IntegerField()),
                ('db_rate_level', models.CharField(max_length=255, null=True, blank=True)),
                ('db_rate_color', models.CharField(max_length=255, null=True, blank=True)),
                ('db_rate_reason', models.CharField(max_length=255, null=True, blank=True)),
                ('rate_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'oracle_db_rate_his',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OracleLock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255, null=True, blank=True)),
                ('host', models.CharField(max_length=255)),
                ('port', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('session', models.CharField(max_length=255)),
                ('lmode', models.CharField(max_length=255)),
                ('ctime', models.CharField(max_length=255)),
                ('inst_id', models.CharField(max_length=255)),
                ('lmode1', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('chk_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'oracle_lock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OracleTbs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('port', models.IntegerField()),
                ('service_name', models.CharField(max_length=255)),
                ('tbs_name', models.CharField(max_length=255)),
                ('datafile_count', models.IntegerField()),
                ('size_gb', models.CharField(max_length=32)),
                ('free_gb', models.CharField(max_length=32)),
                ('used_gb', models.CharField(max_length=32)),
                ('max_free', models.CharField(max_length=32)),
                ('pct_used', models.CharField(max_length=32)),
                ('pct_free', models.CharField(max_length=32)),
                ('rate_level', models.CharField(max_length=255)),
                ('chk_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'oracle_tbs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OracleTbsHis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('port', models.IntegerField()),
                ('service_name', models.CharField(max_length=255)),
                ('tbs_name', models.CharField(max_length=255)),
                ('datafile_count', models.IntegerField()),
                ('size_gb', models.CharField(max_length=32)),
                ('free_gb', models.CharField(max_length=32)),
                ('used_gb', models.CharField(max_length=32)),
                ('max_free', models.CharField(max_length=32)),
                ('pct_used', models.CharField(max_length=32)),
                ('pct_free', models.CharField(max_length=32)),
                ('rate_level', models.CharField(max_length=255)),
                ('chk_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'oracle_tbs_his',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OracleTmpTbs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('port', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('tmp_tbs_name', models.CharField(max_length=255)),
                ('total_mb', models.CharField(max_length=255)),
                ('used_mb', models.CharField(max_length=255)),
                ('pct_used', models.CharField(max_length=255)),
                ('rate_level', models.CharField(max_length=255)),
                ('chk_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'oracle_tmp_tbs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OracleTmpTbsHis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('port', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('tmp_tbs_name', models.CharField(max_length=255)),
                ('total_mb', models.CharField(max_length=255)),
                ('used_mb', models.CharField(max_length=255)),
                ('pct_used', models.CharField(max_length=255)),
                ('rate_level', models.CharField(max_length=255)),
                ('chk_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'oracle_tmp_tbs_his',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OracleUndoTbs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('port', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('undo_tbs_name', models.CharField(max_length=255)),
                ('total_mb', models.CharField(max_length=255)),
                ('used_mb', models.CharField(max_length=255)),
                ('pct_used', models.CharField(max_length=255)),
                ('rate_level', models.CharField(max_length=255)),
                ('chk_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'oracle_undo_tbs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OracleUndoTbsHis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('port', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('undo_tbs_name', models.CharField(max_length=255)),
                ('total_mb', models.CharField(max_length=255)),
                ('used_mb', models.CharField(max_length=255)),
                ('pct_used', models.CharField(max_length=255)),
                ('rate_level', models.CharField(max_length=255)),
                ('chk_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'oracle_undo_tbs_his',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TabOracleServers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('port', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('user_os', models.CharField(max_length=255)),
                ('password_os', models.CharField(max_length=255)),
                ('connect', models.CharField(max_length=255)),
                ('connect_cn', models.CharField(max_length=255)),
                ('tbs', models.CharField(max_length=255)),
                ('tbs_cn', models.CharField(max_length=255)),
                ('adg', models.CharField(max_length=255)),
                ('adg_cn', models.CharField(max_length=255)),
                ('temp_tbs', models.CharField(max_length=255)),
                ('temp_tbs_cn', models.CharField(max_length=255)),
                ('undo_tbs', models.CharField(max_length=255)),
                ('undo_tbs_cn', models.CharField(max_length=255)),
                ('conn', models.CharField(max_length=255)),
                ('conn_cn', models.CharField(max_length=255)),
                ('err_info', models.CharField(max_length=255)),
                ('err_info_cn', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tab_oracle_servers',
                'managed': False,
            },
        ),
    ]
