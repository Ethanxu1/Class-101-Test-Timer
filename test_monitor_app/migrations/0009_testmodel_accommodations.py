# Generated by Django 4.0.5 on 2022-07-09 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_monitor_app', '0008_rename_before_essay_break_time_testmodel_before_essay_break_time_act_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='accommodations',
            field=models.BooleanField(default=False),
        ),
    ]