from django.forms import ModelForm
from catalogo.models import Author

class AuthorForm(ModelForm):
    """
    Formulario para crear autores
    """
    class Meta:
        model=Author
        fields = '__all__'
