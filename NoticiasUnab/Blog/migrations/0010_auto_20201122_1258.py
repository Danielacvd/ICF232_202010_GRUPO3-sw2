# Generated by Django 3.1.3 on 2020-11-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_auto_20201120_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]
