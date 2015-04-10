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
from django.core.mail import send_mail
from .models import Task


@login_required(login_url='/registration/register/')
def index(request, template_name="index.html"):
    checked = ''
    id = ''
    textField = ''
    if request.POST:
        id = request.POST['rd']
        if id == '1':
            checked = u'Вопрос по урокам'
        if id == '2':
            checked = u'Нужда'
        if id == '3':
            checked = u'Благодарность'
        if id == '4':
            checked = u'Свидетельство'
        textField += request.POST.get('textFIELD', '')
        if textField != u'':
            send_mail(checked, textField, 'cwitnesses@gmail.com',
                      ['4izmerenie.sammit2015@gmail.com'], fail_silently=False)
    tasks = Task.objects.all()
    return render_to_response(template_name, {
        'tasks': tasks,
    }, context_instance=RequestContext(request))


@login_required(login_url='/registration/register/')
def video_view(request, template_name="video.html", pk=None):
    checked = ''
    id = ''
    textField = ''
    if request.POST:
        id = request.POST['rd']
        if id == '1':
            checked = u'Вопрос по урокам'
        if id == '2':
            checked = u'Нужда'
        if id == '3':
            checked = u'Благодарность'
        if id == '4':
            checked = u'Свидетельство'

        email = request.user.email
        textField += email + ':'
        textField += request.POST.get('textFIELD', '')
        if textField != u'':
            send_mail(checked, textField, 'cwitnesses@gmail.com',
                      ['oldtigersvoice@gmail.com'], fail_silently=False)
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