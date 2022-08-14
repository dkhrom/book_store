from django.urls import path
from .views import (
    index,
    add_books,
    success_func,
)


urlpatterns = [
    path('', index, name='index'),
    path('book/add/', add_books, name='add_books'),
    path('success-func/<int:pk>/', success_func, name='success_func'),
]