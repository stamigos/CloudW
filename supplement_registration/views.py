from django.shortcuts import render_to_response, redirect
from django.http import request, HttpResponseRedirect, Http404
from django.template import RequestContext
#from profiles.forms import EmailUserCreationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from supplement_registration.models import MyRegistrationSupplement


@login_required(login_url='/registration/register')
def profile_settings(request, template_name="person_card.html"):
    _user = ''
    _employee = ''
    if request.POST:
        user = User.objects.get(pk=request.user.id)
        user.username = request.POST.get('user')
        user.email = request.POST.get('email')
        user.save()

        employee = MyRegistrationSupplement.objects.get(pk=request.user.pk)
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.father_name = request.POST.get('father_name')
        employee.city = request.POST.get('city')
        employee.phone_number = request.POST.get('phone_number')
        employee.save()

        _user = user
        _employee = employee

        return HttpResponseRedirect('/person_card/')

    return render_to_response(template_name, {
        'user': _user,
        'employee': _employee,

    }, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
