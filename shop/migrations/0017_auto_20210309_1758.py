# Generated by Django 3.1.7 on 2021-03-09 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20210309_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', max_length=45, upload_to='', verbose_name='Обложка'),
        ),
    ]
