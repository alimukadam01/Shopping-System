# Generated by Django 4.1.3 on 2023-01-17 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0010_alter_cartitem_quantity'),
        ('Orders', '0019_alter_order_timings_alter_orderitem_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timings',
            field=models.CharField(blank=True, choices=[('Evening', '12.00-18.00'), ('Morning', '06.00-12.00'), ('Night', '18.00-23.00')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='Orders.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderitem', to='Products.product'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Complete'), ('F', 'Failed')], default='P', max_length=1),
        ),
    ]