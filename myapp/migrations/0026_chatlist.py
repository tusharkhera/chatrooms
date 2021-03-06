# Generated by Django 3.2.9 on 2022-02-06 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0025_auto_20220206_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('grp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.group')),
            ],
        ),
    ]
