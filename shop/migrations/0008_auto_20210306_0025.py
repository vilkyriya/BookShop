# Generated by Django 3.1.7 on 2021-03-05 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210305_1833'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Basket',
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'managed': False, 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
