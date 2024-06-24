from django.shortcuts import render
from django.http import HttpResponse
from rest_api.models import Book, Author

# Create your views here.
def books(request) -> HttpResponse:
    book_list = Book.objects.all().values()
    return HttpResponse(book_list)

def authors(request) -> HttpResponse:
    author_list = Author.objects.all().values()
    return HttpResponse(author_list)