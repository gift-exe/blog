# Generated by Django 4.1 on 2022-08-30 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app_1', '0002_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='emaill',
            new_name='email',
        ),
    ]