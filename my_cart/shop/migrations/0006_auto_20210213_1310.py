# Generated by Django 3.1.6 on 2021-02-13 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210212_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mobile',
            field=models.IntegerField(default=''),
        ),
    ]
