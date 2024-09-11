from django.contrib import admin

# Register your models here.

from lib_b.models import LibraryBook

admin.site.register(LibraryBook)