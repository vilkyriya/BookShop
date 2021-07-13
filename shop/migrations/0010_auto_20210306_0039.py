# Generated by Django 3.1.7 on 2021-03-05 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0009_orderbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderbook',
            name='id_user',
            field=models.OneToOneField(db_column='id_user', on_delete=django.db.models.deletion.CASCADE,
                                       to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderbook',
            name='id_orderbook',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=False,
        ),

    ]
