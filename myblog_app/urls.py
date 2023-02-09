from django.contrib import admin
from django.urls import path
from rest_framework import routers

from .views import ListBook, DetailBook, AddBookView, MylistBook, LikeOrDislike, DownloadBookView

# router = routers.DefaultRouter()
# router.register(r'custom-viewset', LikeorDislike)

urlpatterns = [
    path('', ListBook.as_view(), name='home'),
    path('<int:pk>/', DetailBook.as_view(), name='detail_book'),
    path('addbook/', AddBookView.as_view(), name='add_book'),
    path('mybook/', MylistBook.as_view(), name='my_book'),
    path('add-like/<int:pk>/', LikeOrDislike.as_view({'put': 'set_like'}), name='addordellike'),
    path('add-dislike/<int:pk>/', LikeOrDislike.as_view({'put': 'set_dislike'}), name='addordeldislike'),
    path('download-book/<int:pk>/', DownloadBookView.as_view(), ),
]