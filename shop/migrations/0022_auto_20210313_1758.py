# Generated by Django 3.1.7 on 2021-03-13 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20210310_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='created',
        ),
        migrations.RemoveField(
            model_name='book',
            name='updated',
        ),
        migrations.AddField(
            model_name='book',
            name='sale',
            field=models.IntegerField(default=0, verbose_name='Скидка'),
        ),
    ]
