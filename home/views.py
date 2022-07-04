from django.shortcuts import render
from .forms import ContactForm


def index(request):
    contact_form = ContactForm()
    return render(request, 'index.html', {'contact_form': contact_form})
