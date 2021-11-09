from django.shortcuts import render
from django.views.generic.list import ListView
from catalogo.models import Book
from catalogo.models import Author
from django.views import generic
from catalogo.forms import AuthorForm

# Create your views here.
def indice(request):
    '''
    Pagina inicial de nuestra web
    '''
    num_books = Book.objects.all().count()
    num_authors= Author.objects.all().count()
    datos = {'autor':'Sergio Soteras',
            'num_books': num_books,
            'num_authors': num_authors}
    busqueda = request.GET.get('q')
    if busqueda:
        libros = Book.objects.filter(title__icontains = busqueda)
        datos['noencontrado'] = True
    else:
        libros = Book.objects.all()
    
    datos['libros'] = libros
    return render(request, 'index.html', context=datos)

def libro(request):
    '''
    Página de información de cada libro
    '''
    
    datos = {}
    
    return render(request, 'libro.html', context=datos)

def contacto(request):
    '''
    Pagina de contacto de nuestra web
    '''
    datos = {'autor':'Sergio Soteras',
            'email': 'emaildecontacto@gmail.com',
            'fax': '976542198'}
    
    return render(request, 'contacto.html', context=datos)

def todos_libros(request):
    libros = Book.objects.all().order_by('title')

    return render(request,'todos_libros.html',context={'libros':libros})

class LibrosListView(generic.ListView):
    '''
    Vista generica para nuestro listado de libros
    '''
    model = Book
    paginate_by = 30
    
class AutoresListView(generic.ListView):
    '''
    Vista generica para nuestro listado de autores
    '''
    model = Author
    paginate_by = 15

class AuthorDetailView(generic.DetailView):
    model = Author

class BookDetailView(generic.DetailView):
    model = Book

class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'libros/search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Book.objects.filter(title__icontains=query)

def crear_autor(request):
    datos={'form':AuthorForm()}
    return render(request,"crear_autor.html",context=datos)