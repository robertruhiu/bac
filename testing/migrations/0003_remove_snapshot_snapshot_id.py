# Generated by Django 2.0.4 on 2018-11-10 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20181110_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snapshot',
            name='snapshot_id',
        ),
    ]