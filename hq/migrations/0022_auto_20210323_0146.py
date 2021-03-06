# Generated by Django 3.1.7 on 2021-03-22 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hq', '0021_billingaddress_payment_option'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='labe',
            new_name='label',
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='payment_option',
            field=models.CharField(choices=[('C', '現金'), ('P', 'ペイパル')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('W', '和菓子'), ('S', '精肉'), ('K', '海産物')], max_length=10),
        ),
    ]
