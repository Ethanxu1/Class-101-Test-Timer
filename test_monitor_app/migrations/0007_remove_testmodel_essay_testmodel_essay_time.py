# Generated by Django 4.0.5 on 2022-06-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_monitor_app', '0006_rename_before_essay_break_testmodel_before_essay_break_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmodel',
            name='essay',
        ),
        migrations.AddField(
            model_name='testmodel',
            name='essay_time',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
