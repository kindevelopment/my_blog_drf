from django.contrib import admin
from django.urls import path

from .views import ListBook, DetailBook, AddBookView, MylistBook

urlpatterns = [
    path('', ListBook.as_view(), name='home'),
    path('<int:pk>/', DetailBook.as_view(), name='detail_book'),
    path('addbook/', AddBookView.as_view(), name='add_book'),
    path('mybook/', MylistBook.as_view(), name='my_book'),
]