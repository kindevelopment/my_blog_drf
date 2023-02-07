from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Books, Author, Publisher, Category, Genry


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_image', 'category',)
    list_display_links = ('title', )
    list_filter = ('category', 'author', 'publisher', 'genry')
    search_fields = ('title',)
    readonly_fields = ('get_image', 'date_publication', )
    fieldsets = (
        (None, {
            'fields': (('title',), 'file', ('poster', 'get_image'))
        }),
        (None, {
            'fields': ('description', )
        }),
        (None, {
            'fields': (('author', 'genry', ), )
        }),
        (None, {
            'fields': (('category', 'publisher', ), )
        }),
        (None, {
            'fields': (('date_publication', 'num_pages',), )
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="60"')

    get_image.short_description = 'Постер'


@admin.register(Author)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Publisher)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Category)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Genry)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
