# Generated by Django 3.2.8 on 2021-10-21 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('contactDate', models.DateTimeField(default=datetime.datetime(2021, 10, 21, 6, 19, 55, 210374))),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
