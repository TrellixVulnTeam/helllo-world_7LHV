# Generated by Django 2.1.1 on 2018-09-17 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('username', models.TextField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.TextField(max_length=20)),
            ],
        ),
    ]
