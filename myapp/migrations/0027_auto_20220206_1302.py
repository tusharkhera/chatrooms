# Generated by Django 3.2.9 on 2022-02-06 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_chatlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatlist',
            name='grp',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.group'),
        ),
        migrations.AlterField(
            model_name='group',
            name='unique_id',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
