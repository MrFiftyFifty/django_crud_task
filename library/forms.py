from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publication_year', 'genres', 'co_authors', 'summary']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'genres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Укажите жанры через запятую'}),
            'co_authors': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Укажите соавторов через запятую'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
