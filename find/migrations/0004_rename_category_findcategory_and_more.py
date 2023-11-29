# Generated by Django 4.2.7 on 2023-11-22 21:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('find', '0003_category_tag_post_author_post_file_upload_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='FindCategory',
        ),
        migrations.RenameModel(
            old_name='Comment',
            new_name='FindComment',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
