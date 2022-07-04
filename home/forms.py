from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше Имя:',
                            widget=forms.TextInput({'placeholder': 'Ваше Имя' }))
    phone_no = forms.CharField(max_length=10, label='Номер вашего телефона:',
                            widget=forms.TextInput({'placeholder': 'Номер вашего телефона'}))
    email = forms.EmailField(max_length=200, label='Email:',  widget=forms.TextInput({'placeholder': 'Email'}))
    description = forms.CharField(max_length=1000, widget=forms.Textarea({'placeholder': 'Описание'}), label='Описание:')
