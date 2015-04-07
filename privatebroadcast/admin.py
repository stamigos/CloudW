from django.contrib import admin
from multiuploader.admin import MultiuploaderAdmin
from .models import Task


class MultiuploaderTaskAdmin(admin.ModelAdmin):
    #form = MultiuploaderAdminForm
    search_fields = ["filename", "key_data"]
    list_display = ["filename", "upload_date", "file", "title", "description", "image"]

admin.autodiscover()
#admin.site.unregister(MultiuploaderAdmin)
admin.site.register(Task, MultiuploaderAdmin)