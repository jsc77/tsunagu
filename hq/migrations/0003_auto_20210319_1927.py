# Generated by Django 3.1.7 on 2021-03-19 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hq', '0002_auto_20210308_0101'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='menu_images/')),
                ('price', models.IntegerField()),
                ('label', models.CharField(choices=[('P', 'p'), ('S', 's'), ('D', 'd')], default='D', max_length=1)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['name'], unique=True)),
                ('quantity', models.IntegerField(default=1)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
    ]
