from django.contrib import admin
from .models import Book


admin.AdminSite.site_header = 'Book store'


@admin.register(Book)
class FeedBack(admin.ModelAdmin):
    list_display = ('name', 'key', 'author', 'genre', 'price')
    search_fields = ('name', 'key', 'author', 'price')
    list_filter = ('genre',)
    readonly_fields = ('key',)