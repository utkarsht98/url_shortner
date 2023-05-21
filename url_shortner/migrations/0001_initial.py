# Generated by Django 4.2.1 on 2023-05-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlInfo',
            fields=[
                ('url_id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('short_url', models.CharField(max_length=20)),
                ('long_url', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
