from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()


class BaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CartItem(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='carts')
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.product.name} is added to cart.'

    def total_price(self):
        total = self.product.price * self.quantity
        return total


class Cart(BaseModel):
    carts = models.ManyToManyField(
        CartItem, related_name='carts')

    def grand_total(self):
        grand_total = 0
        for cart in self.carts.all():
            grand_total += cart.product.price
        return grand_total
