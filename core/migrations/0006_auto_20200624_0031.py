# Generated by Django 3.0.7 on 2020-06-24 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200620_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='og_user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='og_user',
            new_name='user',
        ),
    ]
