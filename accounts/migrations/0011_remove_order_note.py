# Generated by Django 3.0.6 on 2020-05-23 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200523_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='note',
        ),
    ]
