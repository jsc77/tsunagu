# Generated by Django 3.1.7 on 2021-03-07 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hq', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='name',
        ),
    ]
