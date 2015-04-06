from django.shortcuts import render_to_response, redirect
from django.http import request, HttpResponseRedirect, Http404
from django.template import RequestContext
#from profiles.forms import EmailUserCreationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from supplement_registration.models import MyRegistrationSupplement


@login_required(login_url='/registration/register')
def profile_settings(request, template_name="person_card.html"):
    return render_to_response(template_name, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
