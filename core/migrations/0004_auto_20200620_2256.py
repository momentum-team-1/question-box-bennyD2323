# Generated by Django 3.0.7 on 2020-06-20 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200620_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='title',
        ),
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(max_length=1500),
        ),
    ]