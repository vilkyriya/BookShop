# Generated by Django 3.1.7 on 2021-02-23 12:31

from django.db import migrations, models
import django.db.models.deletion
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id_address', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=45)),
                ('street', models.CharField(max_length=45)),
                ('house_number', models.IntegerField()),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id_author', models.AutoField(primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=45)),
                ('first_name', models.CharField(max_length=45)),
                ('second_name', models.CharField(blank=True, max_length=45, null=True)),
                ('patronymic_name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id_book', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=45)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('number_page', models.IntegerField(blank=True, null=True)),            ],
            options={
                'db_table': 'book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bookauthor',
            fields=[
                ('id_bookauthor', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'bookauthor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id_color', models.AutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'color',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id_cover', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'cover',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id_genre', models.AutoField(primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'genre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id_material', models.AutoField(primary_key=True, serialize=False)),
                ('material', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'material',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField()),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id_payment', models.AutoField(primary_key=True, serialize=False)),
                ('payment', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id_publisher', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=45)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'publisher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'basket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('created_at', models.DateField()),
                ('text', models.TextField()),
                ('rating', models.IntegerField()),
            ],
            options={
                'db_table': 'feedback',
                'managed': False,
            },
        ),
    ]
