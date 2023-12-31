# Generated by Django 4.2.7 on 2023-11-30 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('content', models.TextField()),
                ('notice_image', models.ImageField(blank=True, upload_to='notice/images/%Y/%m/%d/')),
                ('top_fixed', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('view_count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
