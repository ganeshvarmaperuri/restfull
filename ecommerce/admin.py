from django.contrib import admin
from .models import Category, Grocery, Book

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Grocery)
