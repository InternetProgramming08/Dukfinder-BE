# Generated by Django 4.2.7 on 2023-11-23 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0009_post_date_select'),
    ]

    operations = [
        migrations.AddField(
            model_name='findcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='find.findcomment'),
        ),
    ]
