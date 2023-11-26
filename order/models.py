from django.db import models
from django.contrib.auth.models import User
from product.models import Product

ORDER_STATUS = (
    ('processing', 'Processing'),
    ('delivered', 'Delivered'),
)


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.title

    def sub_total(self):
        return self.quantity*self.item.price


class Order(models.Model):
    tracking_number = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem)
    order_status = models.CharField(
        max_length=10, choices=ORDER_STATUS, default='processing')
    ordered = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total_price = 0
        for orders in self.products.all():
            total_price += orders.sub_total()
        return total_price
