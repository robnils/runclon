from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rcgeneral.models import Registration


def index(request):
    return render(request, 'index.html', {})


def update_status(request):
    if request.method == 'POST':
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'reason': 'Must be a valid POST request!'})


def register(request):
    if request.method == 'POST':
        bib = request.POST.get('bib')
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        gender = request.POST.get('gender')
        age_category = request.POST.get('age_category')
        club = request.POST.get('bib')
        email = request.POST.get('email')
        number = request.POST.get('number')

        try:
            Registration.add(bib=bib, first_name=first_name, surname=surname, gender=gender, age_category=age_category, club=club,
                             email=email, number=number)
        except Exception as exp:
            print exp
            return JsonResponse({'success': False, 'reason': exp.message})

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'reason': 'Must be a valid POST request!'})


def get_customer(request):
    id = request['id']


def get_registrations(request):
    if request.method == 'GET':
        try:
            customers = Registration.get_registrations()
        except Exception as exp:
            print exp
            return JsonResponse({'success': False, 'reason': exp.message})

        return JsonResponse({'success': True, 'customers': customers})

    return JsonResponse({'success': False, 'reason': 'Must be a valid GET request!'})
