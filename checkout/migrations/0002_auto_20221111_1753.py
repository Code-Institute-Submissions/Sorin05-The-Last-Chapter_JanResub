# Generated by Django 3.2 on 2022-11-11 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_adress1',
            new_name='street_address1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_adress2',
            new_name='street_address2',
        ),
    ]
