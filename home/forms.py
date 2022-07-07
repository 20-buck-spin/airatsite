from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


def check_forbidden_chars(value):
    forbiddenChars = ['<', '>', '{', '}', '#', '^', '~', '|', '*']
    test = (any(char in value for char in forbiddenChars)) or (value == '' or value == None) 
    if test:
        raise ValidationError('Invalid chars found')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше Имя:',
                            widget=forms.TextInput({'placeholder': 'Ваше Имя' }),
                            validators=[RegexValidator('^([a-zA-Za-яё]\s?)+$', message='Invalid Characters')])
    phone_no = forms.CharField(max_length=13, label='Номер вашего телефона:',
                            widget=forms.TextInput({'placeholder': 'Номер вашего телефона'}),
                            validators=[RegexValidator('^((8|\+7)[\- ]?)?9(\(?\d{2}\)?[\- ]?)?[\d\- ]{7,10}$', 
                            message='Invalid phone number')])
    email = forms.EmailField(max_length=200, label='Email:',  widget=forms.TextInput({'placeholder': 'Email'}), 
                            validators=[RegexValidator('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$',
                            message='Invalid Email')])
    description = forms.CharField(max_length=3000, widget=forms.Textarea({'placeholder': 'Описание'}),
                                  validators=[check_forbidden_chars], label='Описание:')
