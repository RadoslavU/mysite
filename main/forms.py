from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
            'message': forms.Textarea(attrs={'rows': 6, 'required': True}),
        }
        labels = {
            'name': 'Име',
            'email': 'Email',
            'message': 'Съобщение',
        }
