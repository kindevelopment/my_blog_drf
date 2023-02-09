import os.path

from django.http import FileResponse, Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import views, generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .serializers import BookListSerializers, BookDetailSerializers, BookAddSerializers
from .models import Books
from rest_framework.response import Response

from .service import BooksFilter, MyListBook


class ListBook(generics.ListAPIView):
    queryset = Books.objects.filter(permit=True)
    serializer_class = BookListSerializers
    permission_classes = (IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, )
    filterset_class = BooksFilter
    # authentication_classes = (TokenAuthentication, )


class DetailBook(views.APIView):
    def get(self, request, pk):
        books = Books.objects.get(id=pk)
        serializer = BookDetailSerializers(books)
        return Response(serializer.data)


# class AddBook(views.APIView):
#     def post(self, request):
#         serializer = BookAddSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(status=201)
#         return Response(status=400)


class AddBookView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookAddSerializers
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MylistBook(generics.ListAPIView):
    serializer_class = BookListSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MyListBook

    def get_queryset(self):
        queryset = Books.objects.filter(user=self.request.user)
        return queryset


class LikeOrDislike(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookDetailSerializers

    @action(detail=True, methods=['put'])
    def set_like(self, request, pk):
        book = self.get_object()
        if self.request.user in book.dislikes.all():
            book.dislikes.remove(self.request.user)
        if self.request.user in book.likes.all():
            book.likes.remove(self.request.user)
        else:
            book.likes.add(self.request.user)
        return Response(status=201)

    @action(detail=True, methods=['put'])
    def set_dislike(self, request, pk):
        book = self.get_object()
        if self.request.user in book.likes.all():
            book.likes.remove(self.request.user)
        if self.request.user in book.dislikes.all():
            book.dislikes.remove(self.request.user)
        else:
            book.dislikes.add(self.request.user)
        return Response(status=201)


class DownloadBookView(views.APIView):

    def get(self, request, pk):
        book = get_object_or_404(Books, id=pk)
        if os.path.exists(book.file.path):
            return FileResponse(open(book.file.path, 'rb'), filename=book.file.name, as_attachment=True)
        else:
            return Http404

