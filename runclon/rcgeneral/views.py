from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rcgeneral.models import Registration


def index_page(request):
    return render(request, 'index.html', {})


def search_page(request):
    return render(request, 'search_page.html', {})


def update_status(request):
    if request.method == 'POST':
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'reason': 'Must be a valid POST request!'})


def register(request):
    if request.method == 'POST':
        bib = request.POST.get('bib')
        try:
            Registration.register(bib)
        except Exception as exp:
            print exp
            return JsonResponse({'success': False, 'reason': exp.message})
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'reason': 'Must be a valid POST request!'})


def add(request):
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
    bib = request['bib']
    if request.method == 'GET':
        try:
            registration = Registration.get_registration_as_dict(bib)
        except Exception as exp:
            print exp
            return JsonResponse({'success': False, 'reason': exp.message})
        return JsonResponse({'success': True, 'registrations': registration})
    return JsonResponse({'success': False, 'reason': 'Must be a valid GET request!'})


def clear_all(request):
    if request.method == 'GET':
        try:
            response = Registration.truncate()
        except Exception as exp:
            print exp
            return JsonResponse({'success': False, 'reason': exp.message})
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'reason': 'Must be a valid GET request!'})


def get_registrations(request):
    if request.method == 'GET':
        try:
            registrations = Registration.get_all_registrations_as_dict()
        except Exception as exp:
            print exp
            return JsonResponse({'success': False, 'reason': exp.message})
        return JsonResponse({'success': True, 'registrations': registrations})
    return JsonResponse({'success': False, 'reason': 'Must be a valid GET request!'})


def search_last_name(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        try:
            registered, not_registered = Registration.search_by_last_name(text)
        except Exception as exp:
            print exp
            return JsonResponse({'success': False, 'reason': exp.message})
        return JsonResponse({'success': True, 'registered': registered, 'not_registered': not_registered})
    return JsonResponse({'success': False, 'reason': 'Must be a valid POST request!'})


def search_by_first_name(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        try:
            registered, not_registered = Registration.search_by_first_name(text)
        except Exception as exp:
            print exp
            return JsonResponse({'success': False, 'reason': exp.message})
        return JsonResponse({'success': True, 'registered': registered, 'not_registered': not_registered})
    return JsonResponse({'success': False, 'reason': 'Must be a valid POST request!'})