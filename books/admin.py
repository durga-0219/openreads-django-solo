from django.contrib import admin
from .models import Book, Author, Order, Review

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Order)
admin.site.register(Review)
