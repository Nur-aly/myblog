# Generated by Django 3.1 on 2020-08-18 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200818_1851'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PublishedManager',
        ),
    ]