from django.contrib import admin
from multiuploader.admin import MultiuploaderAdmin
from .models import Task


class MultiuploaderTaskAdmin(MultiuploaderAdmin):
    #form = MultiuploaderAdminForm
    model = Task
    search_fields = ["filename", "key_data"]
    list_display = ["title", "description", "image"]

admin.autodiscover()
#admin.site.unregister(MultiuploaderAdmin)
admin.site.register(Task)