# Generated by Django 2.0.4 on 2018-11-05 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='frameworks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='frameworks', to='projects.Framework'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='programming_languages',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='programming_language', to='projects.Language'),
        ),
    ]