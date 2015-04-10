# -*- coding: utf-8
from django.shortcuts import render_to_response
from multiuploader.forms import MultiUploadForm
from django.shortcuts import render_to_response, redirect
from django.http import request, HttpResponseRedirect
from supplement_registration.models import MyRegistrationSupplement
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from multiuploader.forms import MultiUploadForm
from .models import Task


@login_required(login_url='/registration/register/')
def index(request, template_name="index.html"):
    if request.POST.get['lessons-r'].checked:
        checked = 'Вопрос по урокам'

    tasks = Task.objects.all()
    return render_to_response(template_name, {
        'tasks': tasks,
        'checked': checked
    }, context_instance=RequestContext(request))


@login_required(login_url='/registration/register/')
def video_view(request, template_name="video.html", pk=None):
    tasks = Task.objects.all()
    task = Task.objects.filter(pk=pk)
    return render_to_response(template_name, {
        'tasks': tasks,
        'task_pk': task[0],
    }, context_instance=RequestContext(request))


@login_required(login_url='/registration/register/')
def private(request, template_name="private.html"):
    return render_to_response(template_name, context_instance=RequestContext(request))


def uploader_view(request, template_name="uploader.html"):
    context = {
        'uploadForm': MultiUploadForm()
    }
    return render_to_response(template_name, context_instance=context)