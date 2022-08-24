from django.shortcuts import render
from django.http import JsonResponse
from .forms import BookCreateForm, SearchBookForm
from .services import (
    get_book,
    get_books_list, 
    get_books_search_list,
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
        if book_form.is_valid():
            try:
                book_form.save()
                return JsonResponse({'Response': 'Success'})
            except:
                return JsonResponse({'Response': 'Error'})
    else:
        book_form = BookCreateForm()

    return render(request, 'app/books/add_books.html', {'book_form': book_form})


def success_func(request, pk):
    book = get_book(pk)
    book_success_func(book)

    if book.success:
        book_res = True
    else:
        book_res = False

    return JsonResponse({'Response': book_res})



async def my_async(request):
    func = {"message": "Hello!!!"}
    return JsonResponse(func)
