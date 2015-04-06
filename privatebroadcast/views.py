from django.shortcuts import render_to_response
from multiuploader.forms import MultiUploadForm
from django.shortcuts import render_to_response, redirect
from django.http import request, HttpResponseRedirect
from supplement_registration.models import MyRegistrationSupplement
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


@login_required(login_url='/registration/register/')
def index(request, template_name="index.html"):
    return render_to_response(template_name, context_instance=RequestContext(request))

@login_required(login_url='/registration/register/')
def private(request, template_name="private.html"):
    return render_to_response(template_name, context_instance=RequestContext(request))


def uploader_view(request, template_name="uploader.html"):
    context = {
        'uploadForm': MultiUploadForm()
    }
    return render_to_response(template_name, context, context_instance=RequestContext(request))