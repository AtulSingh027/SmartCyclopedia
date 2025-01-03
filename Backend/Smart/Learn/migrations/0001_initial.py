# Generated by Django 5.1.4 on 2024-12-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('chapter', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
