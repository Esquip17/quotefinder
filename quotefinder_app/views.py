from django.shortcuts import render
from .models import Author, Quote


# Create your views here.
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'quotefinder_app/author_list.html', {'authors': authors})


def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotefinder_app/quote_list.html', {'quotes': quotes})


def author_detail(request, pk):
    author = Author.objects.get(id=pk)
    return render(request, 'quotefinder_app/author_detail.html', {'author': author})


def quote_detail(request, pk):
    quote = Quote.objects.get(id=pk)
    return render(request, 'quotefinder_app/quote_detail.html', {'quote': quote})
