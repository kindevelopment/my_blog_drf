# Generated by Django 4.1.6 on 2023-02-08 13:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myblog_app', '0006_books_date_created_post_alter_books_date_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='dislikes',
            field=models.ManyToManyField(default=0, related_name='dislikes', to=settings.AUTH_USER_MODEL, verbose_name='Не нравится'),
        ),
        migrations.AlterField(
            model_name='books',
            name='likes',
            field=models.ManyToManyField(default=0, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Нравится'),
        ),
    ]
