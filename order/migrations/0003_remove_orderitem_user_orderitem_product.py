# Generated by Django 4.2.7 on 2023-11-26 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_price'),
        ('order', '0002_remove_order_products_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order_products', to='product.product'),
        ),
    ]
