# Generated by Django 3.1.7 on 2021-03-22 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hq', '0024_auto_20210323_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compelete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hq.order')),
            ],
        ),
    ]