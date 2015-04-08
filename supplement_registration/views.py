from django.shortcuts import render_to_response, redirect
from django.http import request, HttpResponseRedirect, Http404
from django.template import RequestContext
#from profiles.forms import EmailUserCreationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from supplement_registration.models import MyRegistrationSupplement


@login_required(login_url='/registration/register')
def profile_settings(request, template_name="person_card.html"):
    try:
        profile = MyRegistrationSupplement.objects.get(email=request.user.email)
    except ObjectDoesNotExist:
        profile = MyRegistrationSupplement(first_name='', last_name='', father_name='',
                                           city='', email='', phone_number='')

    if request.POST:
        employee = MyRegistrationSupplement.objects.get_or_create(email=request.user.email)
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.father_name = request.POST.get('father_name')
        employee.city = request.POST.get('city')
        employee.email = request.POST.get('email')
        employee.phone_number = request.POST.get('phone_number')
        employee.save()

        user = User.objects.get(pk=request.user.id)
        user.username = employee.email
        user.email = employee.email
        user.save()

        return HttpResponseRedirect('/person_card/')

    return render_to_response(template_name, {
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'father_name': profile.father_name,
        'city': profile.city,
        'email': profile.email,
        'phone_number': profile.phone_number
    }, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
