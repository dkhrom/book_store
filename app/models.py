from django.db import models
import datetime
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from .key_gen import new_key


def book_photo_folder(instance, filename):
    return 'books/{0}/photos/{1}'.format(instance.key, filename)


class Book(models.Model):

    genre_choices = (
        ('fantasy', 'Фантастика'),
        ('detective', 'Детектив'),
        ('history', 'История'),
        ('other', 'Прочее'),
    )

    key = models.CharField(max_length=150, blank=True, verbose_name='Уникальный ключ')
    name = models.CharField(max_length=150, verbose_name='Наименование')
    author = models.CharField(max_length=150, verbose_name='Автор')
    genre = models.CharField(choices=genre_choices, max_length=50, default='fantasy', verbose_name='Жанр')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена')
    photo = models.ImageField(upload_to=book_photo_folder, verbose_name='Фото')
    photo_small = ImageSpecField(
        source='photo',
        processors=[ResizeToFill(400, 400)],
        format='JPEG',
        options={'quality': 70},
    )
    success = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.key = str(new_key) + str(datetime.datetime.now().day)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class SearchBook(models.Model):

    genre_choices = (
        ('fantasy', 'Фантастика'),
        ('detective', 'Детектив'),
        ('history', 'История'),
        ('other', 'Прочее'),
    )

    name = models.CharField(max_length=150, blank=True, verbose_name='Наименование')
    author = models.CharField(max_length=150, blank=True, verbose_name='Автор')
    genre = models.CharField(choices=genre_choices, blank=True, max_length=50, default='fantasy', verbose_name='Жанр')
    price_from = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name='Цена (от)')
    price_to = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name='Цена (до)')
