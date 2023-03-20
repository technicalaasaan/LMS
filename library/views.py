from django.shortcuts import render
from django.http import HttpResponse
from .models import Books
from django.core.serializers import serialize
import json
from .form import BookForm
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
def add_book(request):
    if request.method == 'GET':
        pass
        # data = Book.objects.get(pk=request.GET())
        # data.delete()
    form_data = BookForm(request.POST)
    if form_data.is_valid():
        form_data.save()
    return render(request, 'books.html', {'form': form_data})

def home(request):
    # return HttpResponse('Welcome you All!')
    # Books.objects.all() .filter .get
    print(request.GET.get('category'))
    category = request.GET.get('category')
    if category:
        data = Books.objects.filter(category=request.GET.get('category')) #all()
    else:
        data = Books.objects.all()
    return HttpResponse(serialize('json', data))
    # return render(request, 'home.html', {'object': data})

class BookCreateView(CreateView):
    model = Books
    template_name = 'books.html'
    fields = '__all__'
    success_url = '/'

class BookListView(ListView):
    model = Books
    template_name = 'home.html'

class
    (DetailView):
    model = Books
    template_name = 'home.html'
