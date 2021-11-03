from django.db import models

# Create your models here.
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
    genre = models.ManyToManyField(Genre, verbose_name='Género')
    author = models.ForeignKey(Author,on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Autor')
    

    def __str__(self):
        return f'{self.title}({self.author})'
    
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Género'

    class Meta:
        verbose_name='Libro'
        
    
