from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage

        fields = [
            'name',
            'email',
            'phone',
            'subject',
            'message',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'form-input',
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'you@example.com',
                'class': 'form-input',
            }),

            'phone': forms.TextInput(attrs={
                'placeholder': '+263 00 000 0000',
                'class': 'form-input',
            }),

            'subject': forms.TextInput(attrs={
                'placeholder': 'How can we help?',
                'class': 'form-input',
            }),

            'message': forms.Textarea(attrs={
                'placeholder': 'Tell us about your project...',
                'rows': 6,
                'class': 'form-input',
            }),
        }
