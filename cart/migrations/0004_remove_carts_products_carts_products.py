# Generated by Django 4.2.7 on 2023-11-23 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_carts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carts',
            name='products',
        ),
        migrations.AddField(
            model_name='carts',
            name='products',
            field=models.ManyToManyField(related_name='carts', to='cart.cartitem'),
        ),
    ]
