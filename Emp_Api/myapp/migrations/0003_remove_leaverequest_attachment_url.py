# Generated by Django 4.0 on 2023-06-16 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_leaverequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaverequest',
            name='attachment_url',
        ),
    ]
