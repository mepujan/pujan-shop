from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('-updated',)


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='category')
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    descriptions = RichTextField()
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='products')
    quantity = models.PositiveIntegerField(default=1)
    stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('-updated',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Product, self).save(*args, **kwargs)

    @property
    def avg_rating(self):
        ratings = self.product.all()
        if ratings:
            avg = 0.0
            sum = 0.0
            for data in ratings:
                sum += data.rating
            avg = sum / len(ratings)
            return avg
        return 0

    @property
    def category_name(self):
        return self.category.name


class Rating(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    rating = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.username} has rated {self.product.name}"

    class Meta:
        ordering = ('-updated',)

    def save(self, *args, **kwargs):
        if self.rating not in range(1, 6):
            raise ValidationError(
                'Rating should be in range 1 to 5 inclusive.')
        return super().save(*args, **kwargs)
