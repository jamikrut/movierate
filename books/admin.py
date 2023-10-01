from django.contrib import admin
from .models import Book, PublishPlace

# Register your models here.
admin.site.register(Book)
admin.site.register(PublishPlace)
