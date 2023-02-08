from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Books, Author, Category, Genry, Publisher


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('title', )


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', )


class GenrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Genry
        fields = ('title', )


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class DislikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class PublisherSeriazlizers(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('title', )


class BookListSerializers(serializers.ModelSerializer):
    authors = AuthorSerializers(many=True)
    category = CategorySerializers()
    genrys = GenrySerializers(many=True)

    class Meta:
        model = Books
        fields = ('poster', 'title', 'authors', 'category', 'genrys')


class BookDetailSerializers(serializers.ModelSerializer):
    authors = AuthorSerializers(many=True)
    category = CategorySerializers()
    genrys = GenrySerializers(many=True)
    user = UserSerializers()
    publisher = PublisherSeriazlizers()
    likes = LikeSerializers(many=True)
    dislikes = DislikeSerializers(many=True)

    class Meta:
        model = Books
        fields = '__all__'


class BookAddSerializers(serializers.ModelSerializer):

    class Meta:
        model = Books
        exclude = ('likes', 'dislikes', 'user', 'date_publication', )

