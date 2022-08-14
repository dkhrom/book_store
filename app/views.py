from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookCreateForm, SearchBookForm
from .tasks import (
    get_book,
    get_books_list, 
    get_books_search_list, 
    add_book_func,
    book_success_func,
)


def index(request):
    
    books = get_books_list()

    search_form = SearchBookForm(request.GET)
    if search_form.is_valid() and 'search_form_btn' in request.GET:
        books = get_books_search_list(search_form)
        if not books:
            books = get_books_list()

    context = {
        'books': books,
        'search_form': search_form,
    }
    
    return render(request, 'app/index.html', context=context)


def add_books(request):
    if request.method == 'POST':
        book_form = BookCreateForm(request.POST, request.FILES)
        add_book_func(book_form)
        messages.success(request, "Книга успешно добавлена!")
        return redirect(index)
    else:
        book_form = BookCreateForm()

    return render(request, 'app/books/add_books.html', {'book_form': book_form})


def success_func(request, pk):
    book = get_book(pk)
    book_success_func(book)
    return redirect(index)
