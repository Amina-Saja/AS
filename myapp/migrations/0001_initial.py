# Generated by Django 4.0.2 on 2022-03-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.IntegerField()),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]