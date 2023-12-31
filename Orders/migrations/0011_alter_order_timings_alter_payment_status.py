# Generated by Django 4.1.3 on 2023-01-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0010_alter_order_options_remove_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timings',
            field=models.CharField(blank=True, choices=[('Morning', '06.00-12.00'), ('Evening', '12.00-18.00'), ('Night', '18.00-23.00')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('F', 'Failed'), ('C', 'Complete')], default='P', max_length=1),
        ),
    ]
