# Generated by Django 3.2 on 2023-05-16 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230516_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='user',
            new_name='follower',
        ),
    ]
