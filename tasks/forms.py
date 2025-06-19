from django import forms
from .models import Task
from ckeditor.widgets import CKEditorWidget

class TaskForm(forms.ModelForm):
    description = forms.CharField(
        widget=CKEditorWidget()
    )

    class Meta:
        model = Task
        fields = ['category', 'title', 'description', 'price', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Ej: Programa en Python con GUI',
                'class': 'w-full p-2 border rounded',
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Ej: 250 MXN',
                'class': 'w-full p-2 border rounded',
            }),
            'deadline': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full p-2 border rounded',
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-2 border rounded',
            }),
        }
