from django import forms
from .models import Book, SearchBook


class BookCreateForm(forms.ModelForm):
    class Meta():
        model = Book
        fields = ('name', 'genre', 'author', 'price', 'photo')


class SearchBookForm(forms.ModelForm):
    class Meta():
        model = SearchBook
        fields = ('name', 'genre', 'author', 'price_from', 'price_to')