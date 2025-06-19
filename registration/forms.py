from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#formulario para el registro de usuario
class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Pon tu contrasena'
        })
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confrima tu contrasena'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu usuario ej: Pepito'
            }),
        }

#para el formulario de actulizazr o poner perfiles
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'university', 'contact_info', 'profile_image']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Nombre completo'
            }),
            'university': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Universidad'
            }),
            'contact_info': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Opcional: información de contacto como correo oh numero',
                'rows': 3
            }),
            'profile_image': forms.ClearableFileInput(attrs={
                'class': 'w-full block text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
            })
        }