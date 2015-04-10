# -*- coding: utf-8
from django.db import models
from multiuploader.models import MultiuploaderFile
from ckeditor.fields import RichTextField


#TODO: add DateField() for tasks
class Task(models.Model):
    video = models.OneToOneField(MultiuploaderFile, blank=True )
    video_multiple = models.ManyToManyField(MultiuploaderFile, blank=True)
    filename = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='media/')


