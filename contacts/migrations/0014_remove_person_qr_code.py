# Generated by Django 4.0.3 on 2022-08-16 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0013_alter_deletedcontacts_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='qr_code',
        ),
    ]
