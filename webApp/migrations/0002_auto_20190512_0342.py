# Generated by Django 2.1.7 on 2019-05-11 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='customerId',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='keymakerId',
            new_name='keymaker',
        ),
    ]
