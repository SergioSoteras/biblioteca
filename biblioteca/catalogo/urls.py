from django.urls import include,path
from catalogo.views import *


urlpatterns = [
    path('libros/', LibrosListView.as_view(), name='listado_libros'),
    path('autores/', AutoresListView.as_view(), name='listado_autores'),
    path('autor/<int:pk>', AuthorDetailView.as_view(),name='info_autor'),
    path('libro/<int:pk>', BookDetailView.as_view(),name='info_libro'),
    path('libros/search_result', SearchResultsListView.as_view(),name='busqueda_libro'),
    path('autor/create',crear_autor, name="crear_autor"),
]