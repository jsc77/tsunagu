# Generated by Django 3.1.7 on 2021-03-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hq', '0018_auto_20210321_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]