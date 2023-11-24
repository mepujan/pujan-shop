from django.db import models
from django.contrib.auth.models import User


class ShippingDetail(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shipping')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.user.username} has added shipping details."
