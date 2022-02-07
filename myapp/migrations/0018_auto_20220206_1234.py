# Generated by Django 3.2.9 on 2022-02-06 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20220206_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatlist',
            old_name='group',
            new_name='grp',
        ),
        migrations.AlterField(
            model_name='chat',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.group'),
        ),
    ]
