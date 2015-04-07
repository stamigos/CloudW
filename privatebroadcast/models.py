# -*- coding: utf-8
from django.db import models
from multiuploader.models import MultiuploaderFile


class Task(MultiuploaderFile):
    video = models.OneToOneField(MultiuploaderFile, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
