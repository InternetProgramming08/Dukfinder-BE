# Generated by Django 4.2.7 on 2023-12-03 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostpost',
            name='head_image',
            field=models.ImageField(blank=True, default='noimage.jpg', upload_to='lost/images/%Y/%m/%d/'),
        ),
    ]
