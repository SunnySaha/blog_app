# Generated by Django 2.2 on 2019-08-06 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyshare', '0002_posts_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='is_favorite',
        ),
    ]
