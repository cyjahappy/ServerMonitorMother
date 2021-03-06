# Generated by Django 2.2.12 on 2020-05-06 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerInfoThreshold',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cpu_threshold', models.FloatField(default=90.0)),
                ('memory_threshold', models.FloatField(default=90.0)),
                ('disk_threshold', models.FloatField(default=90.0)),
                ('bandwidth_threshold', models.FloatField(default=3.0)),
                ('HTML_open_time_threshold', models.FloatField(default=3.0)),
                ('file_transfer_speed_threshold', models.FloatField(default=0.0)),
                ('microservices_exec_time_threshold', models.FloatField(default=0.0)),
                ('backend_management_system_open_time_threshold', models.FloatField(default=0.0)),
            ],
        ),
    ]
