from django.db import models
from django.contrib.auth.models import User


class User(User):
    name = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name="products")

    class Meta:
        ordering = ["-created"]


class Comment(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name="comments",
        related_query_name="comment",
    )
    user_id = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="comments",
        related_query_name="comment",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateField()

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name


class ProductSize:
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class ProductsSite(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name="site"
    )
    company = models.ForeignKey(
        to=Company, on_delete=models.CASCADE, related_name="sites"
    )
    price = models.DecimalField(default=7.2)
    url = models.URLField()
    productsize = models.ForeignKey(
        to=ProductSize, on_delete=models.CASCADE, related_name="sites"
    )
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
