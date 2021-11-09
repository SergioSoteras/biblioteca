from catalogo.models import Author
import random
nombres=["Maria","Teresa","Mariana","Jose","Pedro","Juan"]
apellidos=["Perez","Reverte","Rodriguez","De la Fuente","Cebollada","Avezuela"]

for n in range(1,20):
    a = Author(first_name=nombres[random.randint(0, 5)],last_name=apellidos[random.randint(0, 5)])
    a.save()