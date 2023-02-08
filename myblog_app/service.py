from django.template.defaultfilters import slugify
from django_filters import rest_framework as filters

from .models import Books


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BooksFilter(filters.FilterSet):
    genrys = CharFilterInFilter(field_name='genrys__title', lookup_expr='in')
    category = CharFilterInFilter(field_name='category__title', lookup_expr='in')
    title = CharFilterInFilter(field_name='title', lookup_expr='in')
    date_publication = filters.RangeFilter()
    authors = CharFilterInFilter(field_name='authors__title', lookup_expr='in')
    publisher = CharFilterInFilter(field_name='publisher__title', lookup_expr='in')
    num_pages = filters.RangeFilter()

    class Meta:
        model = Books
        fields = ['genrys', 'category', 'title', 'date_publication', 'authors', 'publisher', 'num_pages']


