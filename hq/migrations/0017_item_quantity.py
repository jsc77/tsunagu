# Generated by Django 3.1.7 on 2021-03-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hq', '0016_auto_20210321_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]