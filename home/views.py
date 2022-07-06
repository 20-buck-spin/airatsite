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

@csrf_protect
def contact(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    contact_form = ContactForm(data)
    if contact_form.is_valid():
        # send email
        response = {'status':True,
                    'errors': None}
        return JsonResponse(response)
    else:
        return JsonResponse({'status':False,
                          'errors': contact_form.errors})


