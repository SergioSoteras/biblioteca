from django.urls import include,path
from catalogo.views import *


urlpatterns = [
    path('libros/', LibrosListView.as_view(), name='listado_libros'),
    path('autores/', AutoresListView.as_view(), name='listado_autores'),
    path('autor/<int:pk>', AuthorDetailView.as_view(),name='info_autor'),
    path('libro/<int:pk>', BookDetailView.as_view(),name='info_libro'),
    path('buscarlibros/', SearchResultsListView.as_view(),name="buscalibros" ),
    path('autor/crear',crear_autor, name="crear_autor"),
    path('autor/crear2', CrearAutor.as_view(), name='crear_autor2'),
    path('autor/modificar/<int:pk>', ModificarAutor.as_view(), name='modificar_autor'),
    path('autor/eliminar/<int:pk>', EliminarAutor.as_view(), name='eliminar_autor'),
]