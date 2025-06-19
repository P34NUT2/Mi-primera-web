from django import forms
from .models import Offer

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'w-full p-4 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Escribe un mensaje para acompañar tu oferta...',
                'rows': 4,
            })
        }
        labels = {
            'message': 'Mensaje de la oferta',
        }

