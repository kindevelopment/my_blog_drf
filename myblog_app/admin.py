from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Books, Author, Publisher, Category, Genry


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_image', 'category', 'permit', )
    list_display_links = ('title', )
    list_filter = ('category', 'authors', 'publisher', 'genrys')
    list_editable = ('permit', )
    search_fields = ('title',)
    readonly_fields = ('get_image', )
    fieldsets = (
        (None, {
            'fields': (('title',), 'file', ('poster', 'get_image'))
        }),
        (None, {
            'fields': ('description', )
        }),
        (None, {
            'fields': (('authors', 'genrys', ), )
        }),
        (None, {
            'fields': (('category', 'publisher', 'user',), )
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
    list_display_links = ('title', )


@admin.register(Publisher)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title', )


@admin.register(Category)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)


@admin.register(Genry)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('title', )