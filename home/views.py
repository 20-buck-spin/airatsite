from django.shortcuts import render
from .forms import ContactForm
from .models import SolvedCase, SolvedCaseFile
#

def index(request):
    contact_form = ContactForm()
    context = {'contact_form': contact_form,
               'navbar_location': 'index'}
    return render(request, 'index.html', context=context)


def about_us(request):
    return render(request, 'about.html', context={
        'navbar_location': 'about'
    })


def solved_cases_list(request):
    cases = SolvedCase.objects.filter(is_published=True)
    return render(request, 'solved_cases.html', context={
        'navbar_location': 'solved_cases',
        'cases': cases
    })


def solved_case_detail(request, pk):

    try:
        case = SolvedCase.objects.get(pk=pk)
    except SolvedCase.DoesNotExist:
        return render(request, 'error_page.html', context={
            "error": {
                "code": 404,
                "message": "Страница не найдена!"
            }
        })

    if not case.is_published:
        return render(request, 'error_page.html', context={
            "error": {
                "code": 404,
                "message": "Страница не найдена!"
            }
        })

    case_files = SolvedCaseFile.objects.filter(case=case)
    return render(request, "solved_case_detail.html", context={
        'navbar_location': 'solved_cases',
        'case': case,
        'case_files': case_files
    })


