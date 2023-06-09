from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm #importando sistema de registro
from django.contrib.auth.models import User # importando el modelo que usaremos para el registro

class FormArticle(forms.Form):
    name_products = forms.CharField(
        label = "Nombre del producto",
        max_length=150,
        widget=forms.TextInput()
    )

    shipping_type_options = [
        (0, "Envio Disponible"),(1, "Envio No Disponible")
    ]

    shipping_type = forms.TypedChoiceField(
        choices= shipping_type_options,
        label= "¿Tipo Envio?"
    )

    shipping_price_options = [
        (0, "Envio Gratis"), (1, "Envio Con costo")
    ]

    shipping_price = forms.TypedChoiceField(
        choices= shipping_price_options,
        label= "¿Tipo Envio?"
    )

    description_products = forms.CharField(
        label="Descripcion",
        widget=forms.Textarea,
        max_length=150
    )

    product_city = forms.CharField(
        label= "ciudad",
        widget=forms.TextInput()
    )

    product_price = forms.DecimalField(
        label= "Precio",
        max_digits=10,
        decimal_places=2

    )

    status_op = [
        (0, "Privado"), (1, "Publico")
    ]

    status = forms.TypedChoiceField(
        choices= status_op,
        label= "¿Estado?"
    )

class RegisterForm(UserCreationForm):

    class Meta:
        model = User #asignando el modelo en el que se va a basar
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2'] # campos que queremos mostrar (basados en el modelo que elegimos)



