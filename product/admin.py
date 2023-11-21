from django.contrib import admin
from .models import Category, Product, Rating

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Rating)


admin.site.site_header = "Pujan's Shop"
admin.site.site_title = "Pujan's Shop Admin Portal"
admin.site.index_title = "Welcome to Pujan's Shop  Portal"
