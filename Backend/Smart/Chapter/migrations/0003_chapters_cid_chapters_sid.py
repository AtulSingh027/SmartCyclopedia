# Generated by Django 5.1.4 on 2024-12-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chapter', '0002_chapters_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapters',
            name='cid',
            field=models.CharField(default='default_value', max_length=255),
        ),
        migrations.AddField(
            model_name='chapters',
            name='sid',
            field=models.CharField(default='default_value', max_length=255),
        ),
    ]
