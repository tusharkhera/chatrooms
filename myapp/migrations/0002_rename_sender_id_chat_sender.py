# Generated by Django 3.2.9 on 2022-01-16 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='sender_id',
            new_name='sender',
        ),
    ]
