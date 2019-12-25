from django import forms
from .models import Vehicle


class VechicleModelForm(forms.ModelForm):
    name = forms.CharField(label='Vehicle Name:', widget=forms.TextInput(attrs={
        'placeholder': 'Vehicle name', 'class': 'form-control'
    }))
    model = forms.CharField(label='Model:', widget=forms.TextInput(attrs={
        'placeholder': 'Model of Vehicle', 'class': 'form-control'
    }))
    rate = forms.CharField(label='Price:', widget=forms.TextInput(attrs={
        'placeholder': 'Rate of Vehicle', 'class': 'form-control'
    }))
    body_number = forms.CharField(label='Body Number:', widget=forms.TextInput(attrs={
        'placeholder': 'Body number of Vehicle', 'class': 'form-control'
    }))
    engine_number = forms.CharField(label='Engine Number:', widget=forms.TextInput(attrs={
        'placeholder': 'Engine number of Vehicle', 'class': 'form-control'
    }))
    registration_number = forms.CharField(label='Registration Number:', widget=forms.TextInput(attrs={
        'placeholder': 'Registration number of Vehicle', 'class': 'form-control'
    }))
    description = forms.CharField(label='Description:', widget=forms.Textarea(attrs={
        'placeholder': 'Description', 'class': 'form-control'
    }))
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Vehicle
        fields = ['name', 'model', 'rate',
                  'body_number', 'engine_number', 'registration_number', 'description', 'images']
