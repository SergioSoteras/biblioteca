from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from catalogo.models import Book
from catalogo.models import Author
from django.views import generic
from catalogo.forms import AuthorForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

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
     # últimos 5 libros del catálogo
    libros = Book.objects.all().order_by('-id')[:5]

    
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
    context_object_name = 'libros'
    template_name = 'search_results.html'  # No usará la plantilla estándar del ListView
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(title__icontains=query)
        return []  # cuando entramos a buscar o si no se introduce nada
        
# Creación de autor
def crear_autor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Autor creado.')
            return redirect('/')
    else:
        form = AuthorForm()
    datos = {'form': AuthorForm()}
    return render(request, 'crear_autor.html', 
        context=datos)

# Creación de autor con CreateVio. Añadimos SuccessMesaageMixin para mensaje de éxito.
class CrearAutor(SuccessMessageMixin, generic.CreateView):
    model = Author
    fields = '__all__'
    template_name = 'crear_autor.html'
    success_url = '/'
    success_message = "%(first_name)s %(last_name)s se ha creado correctamente"


# Creación de autor con CreateVio. Añadimos SuccessMesaageMixin para mensaje de éxito.
class ModificarAutor(SuccessMessageMixin, generic.UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'modificar_autor.html'
    success_url = '/'
    success_message = "%(first_name)s %(last_name)s se ha modificado correctamente"

# Creación de autor con CreateVio. Añadimos SuccessMesaageMixin para mensaje de éxito.
class EliminarAutor(SuccessMessageMixin, generic.DeleteView):
    model = Author
    template_name = 'autor_confirmar_borrado.html'
    success_url = '/'
    success_message = "%(first_name)s %(last_name)s se ha borrado correctamente"
    