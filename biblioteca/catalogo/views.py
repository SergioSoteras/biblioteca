from django.shortcuts import render
from catalogo.models import Book

# Create your views here.
def indice(request):
    '''
    Pagina inicial de nuestra web
    '''
    libros = Book.objects.all()
    datos = {'autor':'Sergio Soteras',
            'libros':libros}
    
    return render(request, 'index.html', context=datos)

def libro(request):
    '''
    Pagina inicial de nuestra web
    '''
    libros = Book.objects.all()
    datos = {'autor':'Sergio Soteras'}
    
    return render(request, 'libro.html', context=datos)
    