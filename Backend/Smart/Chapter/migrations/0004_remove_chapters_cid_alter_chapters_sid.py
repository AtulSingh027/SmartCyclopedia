# Generated by Django 5.1.4 on 2024-12-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chapter', '0003_chapters_cid_chapters_sid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapters',
            name='cid',
        ),
        migrations.AlterField(
            model_name='chapters',
            name='sid',
            field=models.IntegerField(),
        ),
    ]
