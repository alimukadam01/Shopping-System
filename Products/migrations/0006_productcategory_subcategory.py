# Generated by Django 4.1.3 on 2023-01-11 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_productcategory_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='subcategory',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]