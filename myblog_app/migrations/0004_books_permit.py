# Generated by Django 4.1.6 on 2023-02-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog_app', '0003_alter_books_options_alter_books_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='permit',
            field=models.BooleanField(default=False),
        ),
    ]