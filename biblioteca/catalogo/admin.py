from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    list_filter = ['author','genre']
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fieldsets = (
        ('Datos personales',
        {'fields': ('first_name', 'last_name')}),  #uno debajo de otro
        ('Fechas',
        {'fields': [('date_of_birth', 'date_of_death')]}) #misma linea
    )
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass