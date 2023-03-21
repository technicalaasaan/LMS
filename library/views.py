from django.shortcuts import render
from django.http import HttpResponse
from .models import Books
from django.core.serializers import serialize
import json
from .form import BookForm
from django.views.generic import CreateView, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.

class Home(TemplateView):
    template_name = 'bootstrap/dashboard.html'

def add_book(request):
    if request.method == 'GET':
        form_data = BookForm(request.POST or None)
        return render(request, 'sample/books.html', {'user': 'mohideen', 'form': form_data})
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
    template_name = 'sample/home.html'

class BookDetailView(DetailView):
    model = Books
    template_name = 'home.html'

class BookUpdateView(UpdateView):
    model = Books
    template_name = 'books.html'
    fields = '__all__' # ['book', 'author']
    success_url = '/book/'

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'del_book.html'
    fields = '__all__' # ['book', 'author']
    success_url = '/book/'