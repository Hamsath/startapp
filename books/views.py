# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
# Create your views here.

def search_form(request):
    return render(request,'books/search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append("Enter a search item")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters")
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request,'books/search_results.html',{'books':books, 'query':q})
    return render(request,'books/search_form.html',{'errors':errors})
