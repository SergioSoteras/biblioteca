from django.db import models

# Create your models here.
class Idioma(models.Model):
    '''
    Representa el idioma del libro
    '''
    name = models.CharField("Idioma",max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        pass

class Genre(models.Model):
    '''
    Representa un genero literario
    '''
    name = models.CharField("Género",max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Género'
        verbose_name_plural ='Géneros'

class Author(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Fallecido', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'

class Book(models.Model):
    '''
    Libro para aplicacion de biblioteca
    '''
    title = models.CharField('Título',max_length=250)
    summary = models.TextField('Resumen',blank=True)
    isbn = models.CharField(max_length=13,blank=True)
    fecha = models.DateField(blank = True, null=True, help_text='Fecha de publicación')
    genre = models.ManyToManyField(Genre, verbose_name='Género', blank=True)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Autor')
    idioma = models.ForeignKey(Idioma,on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.title}({self.author})'
    
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Género'
    
    def disponible(self):
        libros = self.bookinstance_set.all()
        for l in libros:
            if l.status == "a":
                return True
        return False

    class Meta:
        verbose_name='Libro'

import uuid # Required for unique book instances

class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Mantenimiento'),
        ('o', 'En préstamo'),
        ('a', 'Disponible'),
        ('r', 'Reservado'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Disponibilidad',
    )

    class Meta:
        verbose_name='Estado del libro'
        verbose_name_plural='Estado de los libros'
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'
        
    
