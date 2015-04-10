# -*- coding: utf-8
from django.db import models
from multiuploader.models import MultiuploaderFile


#TODO: add DateField() for tasks
class Task(models.Model):
    video = models.OneToOneField(MultiuploaderFile, blank=True)
    filename = models.CharField(max_length=40, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')


