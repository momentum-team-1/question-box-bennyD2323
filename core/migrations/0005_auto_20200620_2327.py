# Generated by Django 3.0.7 on 2020-06-20 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200620_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.TextField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.Question'),
        ),
    ]