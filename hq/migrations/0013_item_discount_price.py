# Generated by Django 3.1.7 on 2021-03-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hq', '0012_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
