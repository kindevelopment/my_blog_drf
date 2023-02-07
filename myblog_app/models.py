from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField('Категория', max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Author(models.Model):
    title = models.CharField('Автор', max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genry(models.Model):
    title = models.CharField('Жанр', max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Publisher(models.Model):
    title = models.CharField('Издатель', max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class Books(models.Model):
    title = models.CharField('Название', max_length=250)
    description = models.TextField('Описание', )
    poster = models.ImageField('Постер', upload_to='poster/')
    file = models.FileField('Файл книги', upload_to='filebooks/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', verbose_name='Пользователь')
    author = models.ManyToManyField(Author, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books_category', verbose_name='Категория')
    genry = models.ManyToManyField(Genry, related_name='books_genry', verbose_name='Жанр')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books_publisher', verbose_name='Издатель')
    date_publication = models.DateField('Дата публикации', auto_now_add=True)
    num_pages = models.PositiveIntegerField('Кол-во страниц', default=0)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, verbose_name='Нравится')
    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True, verbose_name='Не нравится')
    permit = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'




