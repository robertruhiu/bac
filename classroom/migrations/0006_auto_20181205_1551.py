# Generated by Django 2.0.4 on 2018-12-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_auto_20181205_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswer',
            name='answer',
            field=models.IntegerField(max_length=255),
        ),
    ]
