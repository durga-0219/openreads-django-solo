from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=4)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)  # ✅ Not auto_now or auto_now_add
