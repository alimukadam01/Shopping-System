# Generated by Django 4.1.3 on 2023-01-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='addresses',
            field=models.ManyToManyField(through='Customers.CustomerAddress', to='Customers.address'),
        ),
    ]
