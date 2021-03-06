# -*- coding: utf-8
from django.db import models
from multiuploader.models import MultiuploaderFile
from ckeditor.fields import RichTextField


#TODO: add DateField() for tasks
class Task(models.Model):
    video_multiple = models.ManyToManyField(MultiuploaderFile, blank=True, related_name='VIDEO')
    filename = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='media/')


