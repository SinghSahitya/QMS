# Generated by Django 4.1.2 on 2023-01-16 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_rename_usercategoryanswer_usercategoryattempts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercategoryattempts',
            old_name='attempt',
            new_name='attempt_time',
        ),
    ]