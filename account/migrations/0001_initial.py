# Generated by Django 4.1.1 on 2022-10-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('userid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=30)),
                ('middlename', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('passowrd', models.CharField(max_length=30)),
            ],
        ),
    ]
