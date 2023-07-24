from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect
import json


def index(request):
    contact_form = ContactForm()
    context = {'contact_form': contact_form,
               'navbar_location': 'index'}
    return render(request, 'index.html', context=context)


def about_us(request):
    return render(request, 'about.html', context={
        'navbar_location': 'about'
    })


