from django.urls import path
from .views import (
    index,
    add_books,
    success_func,

    my_async,
)


urlpatterns = [
    path('', index, name='index'),
    path('book/add/', add_books, name='add_books'),
    path('success-func/<int:pk>/', success_func, name='success_func'),

    path('my_async/', my_async, name='my_async'),
]