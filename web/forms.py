from django import forms
from django.core import validators

class FormContact(forms.Form):
    email = forms.EmailField(
        required=True,
        widget = forms.TextInput(
            attrs={
                'placeholder': ''
            }
        ),
        validators=[
            validators.EmailValidator('Correo electrónico incorrecto')
        ]
    )
    nombre = forms.CharField(
        required=True,
        widget = forms.TextInput(
            attrs={
                'placeholder': ''
            }
        ),
         validators=[
             validators.RegexValidator('^[a-zA-Z\u00C0-\u00FF\s]*$', 'Utiliza carácteres válidos', 'ErrNameFormat')
         ]
    )
    asunto = forms.CharField(
        required=True,
        widget = forms.TextInput(
            attrs={
                'placeholder': ''
            }
        ),
         validators=[
             validators.MaxLengthValidator(40, 'Asunto máximo 20 carácteres'),
             validators.RegexValidator('^[a0-zA9-Z\u00C0-\u00FF\s]*$', 'Utiliza carácteres válidos', 'ErrNameFormat')
         ]
    )
    mensaje = forms.CharField(
        required=True,
        widget = forms.Textarea(
            attrs={
                'placeholder': ''
            }
        ),
         validators=[
             validators.RegexValidator('^[a-zA-Z\u00C0-\u00FF\s]*$', 'Utiliza carácteres válidos', 'ErrNameFormat')
         ]
    )