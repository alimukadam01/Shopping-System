# Generated by Django 4.1.3 on 2023-01-08 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0004_remove_address_terittory_customeraddress_terittory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeraddress',
            old_name='terittory',
            new_name='territory',
        ),
    ]
