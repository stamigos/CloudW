from django.contrib import admin
from django import forms
from multiuploader.admin import MultiuploaderAdmin
from .models import Task
#from ckeditor.widgets import CKEditorWidget


class MultiuploaderTaskAdmin(MultiuploaderAdmin):
   # description = forms.CharField(widget=CKEditorWidget())
    #form = MultiuploaderAdminForm
    model = Task
    search_fields = ["filename", "key_data"]
    list_display = ["title", "description", "image"]

admin.autodiscover()
#admin.site.unregister(MultiuploaderAdmin)
admin.site.register(Task)