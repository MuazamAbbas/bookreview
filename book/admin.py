from django.contrib import admin
from book.models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'isbn')
    list_filter = ('genre', 'published_date')
    search_fields = ('title', 'author', 'isbn')
    ordering = ('title',)
    date_hierarchy = 'published_date'
    readonly_fields = ('created_at', 'updated_at')