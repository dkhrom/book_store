from .models import Book
from django.db.models import Q
from celery import shared_task
from celery import Celery


app = Celery('tasks', broker='pyamqp://guest@localhost//')


@shared_task
def get_book(pk):
    return Book.objects.get(pk=pk)


@shared_task
def get_books_list():
    return Book.objects.all()


@shared_task
def get_books_search_list(search_form):
    return Book.objects.filter(
        Q(name__icontains=search_form.cleaned_data['name']),
        Q(author__icontains=search_form.cleaned_data['author']),
        Q(genre__icontains=search_form.cleaned_data['genre']),
        Q(price__gt=search_form.cleaned_data['price_from'] or 0),
        Q(price__lt=search_form.cleaned_data['price_to'] or 999999),
    )


@shared_task
def book_success_func(book):
    if not book.success:
        book.success = True
        book.save()
    else:
        book.success = False
        book.save()