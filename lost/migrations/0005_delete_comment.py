# Generated by Django 4.2.7 on 2023-11-28 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0004_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]