# Generated by Django 4.2.10 on 2024-03-08 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postattachment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostAttachment',
        ),
    ]