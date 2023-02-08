from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import views, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import BookListSerializers, BookDetailSerializers, BookAddSerializers
from .models import Books
from rest_framework.response import Response

from .service import BooksFilter


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


class MylistBook(views.APIView):

    def get(self, request):
        books = Books.objects.filter(user=self.request.user)
        serializer = BookListSerializers(books, many=True,)
        return Response(serializer.data)