# Generated by Django 3.1.7 on 2021-03-05 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210305_1630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'managed': True, 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
