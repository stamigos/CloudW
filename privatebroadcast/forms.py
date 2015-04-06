from multiuploader.forms import MultiuploaderField
from django import forms


class PostMessageForm(forms.Form):
    text = forms.CharField(label=u'Question', widget=forms.Textarea)
    uploadedFiles = MultiuploaderField(required=False)