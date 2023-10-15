from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category, related_name="book_category", on_delete=models.CASCADE
    )
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Grocery(models.Model):
    name = models.CharField(max_length=100)
    product_tag = models.CharField(max_length=10)
    category = models.ForeignKey(
        Category, related_name="grocery", on_delete=models.CASCADE
    )
    price = models.IntegerField()
    quantity = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.name

