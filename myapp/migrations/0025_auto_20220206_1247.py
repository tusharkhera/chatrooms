# Generated by Django 3.2.9 on 2022-02-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_delete_chatlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='group',
            name='unique_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]
