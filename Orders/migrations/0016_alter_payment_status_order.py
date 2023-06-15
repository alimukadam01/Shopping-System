# Generated by Django 4.1.3 on 2023-01-17 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0007_alter_customer_options'),
        ('Orders', '0015_alter_payment_status_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('F', 'Failed'), ('C', 'Complete'), ('P', 'Pending')], default='P', max_length=1),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('timings', models.CharField(blank=True, choices=[('Night', '18.00-23.00'), ('Morning', '06.00-12.00'), ('Evening', '12.00-18.00')], max_length=255, null=True)),
                ('promocode', models.CharField(blank=True, max_length=255, null=True)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='Customers.customer')),
                ('payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Orders.payment')),
            ],
            options={
                'permissions': [('cancel_order', 'Can cancel order')],
            },
        ),
    ]