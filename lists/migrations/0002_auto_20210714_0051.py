# Generated by Django 2.2.5 on 2021-07-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
