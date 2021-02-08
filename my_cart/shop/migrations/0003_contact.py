# Generated by Django 3.1.6 on 2021-02-08 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210204_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('name_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]