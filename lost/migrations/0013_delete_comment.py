# Generated by Django 4.2.7 on 2023-11-29 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0012_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]