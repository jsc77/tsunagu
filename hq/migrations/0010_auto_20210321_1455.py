# Generated by Django 3.1.7 on 2021-03-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hq', '0009_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]