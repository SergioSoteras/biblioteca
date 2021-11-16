from django.forms import ModelForm, DateInput
from catalogo.models import Author

class AuthorForm(ModelForm):
    """
    Formulario para crear autores
    """
    class Meta:
        model=Author
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(
                attrs={'type':'date'}),
            'date_of_death': DateInput(
                attrs={'type':'date'}),
        }
