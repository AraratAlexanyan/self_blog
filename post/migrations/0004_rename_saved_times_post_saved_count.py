# Generated by Django 4.1.5 on 2023-01-06 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_saved_times'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='saved_times',
            new_name='saved_count',
        ),
    ]
