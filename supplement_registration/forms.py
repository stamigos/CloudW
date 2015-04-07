# -*- coding: utf-8
from django.forms import ModelForm
from django.forms import TextInput
from django import forms
from .models import MyRegistrationSupplement
from django.contrib.auth.models import User
from registration.forms import RegistrationFormUniqueEmail


class MyRegistrationForm(ModelForm):
    class Meta:
        model = MyRegistrationSupplement
        exclude = ('username', 'email1', )

    def __init__(self, *args, **kwargs):
        super(MyRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = TextInput(attrs={
            'placeholder': u'Имя'})
        self.fields['last_name'].widget = TextInput(attrs={
            'placeholder': u'Фамилия'})
        self.fields['father_name'].widget = TextInput(attrs={
            'placeholder': u'Отчество'})
        self.fields['city'].widget = TextInput(attrs={
            'placeholder': u'Город'})
        self.fields['phone_number'].widget = TextInput(attrs={
            'placeholder': u'Телефон'})
        self.fields['username'].widget = TextInput(attrs={
            'hidden': 'hidden'
        })
        self.fields['username'].required = False
        self.fields['email2'].required = False
        self.fields['email2'].widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['autocomplete'] = 'off'


class MyRegistrationFormUniqueEmail(RegistrationFormUniqueEmail):

    def __init__(self, *args, **kwargs):
        super(MyRegistrationFormUniqueEmail, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = TextInput(attrs={
            'placeholder': u'Имя'})
        self.fields['last_name'].widget = TextInput(attrs={
            'placeholder': u'Фамилия'})
        self.fields['father_name'].widget = TextInput(attrs={
            'placeholder': u'Отчество'})
        self.fields['city'].widget = TextInput(attrs={
            'placeholder': u'Город'})
        self.fields['phone_number'].widget = TextInput(attrs={
            'placeholder': u'Телефон'})
        self.fields['username'].widget = TextInput(attrs={
            'hidden': 'hidden'
        })
        self.fields['username'].required = False
        self.fields['email2'].required = False
        self.fields['email2'].widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['autocomplete'] = 'off'

""""
class EditCustomerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditCustomerForm, self).__init__(*args, **kwargs)
        self.fields['email'].initial = self.instance.user.email
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name

    email = forms.EmailField(label=_(u"Email"))
    first_name = forms.CharField(max_length=30, required=True, label=_(u'Forname'))
    last_name = forms.CharField(max_length=30, required=True, label=_(u'Surname'))
    address = forms.CharField(max_length=255, min_length=10, required=True, label=_(u'Address'))

    class Meta:
        model = MyRegistrationSupplement
        fields = ('email', 'first_name', 'last_name', 'address')

    def clean_email(self):
        return check_email(self.cleaned_data['email'], self.instance.user.id)

    def save(self, *args, **kwargs):
        u = self.instance.user
        u.email = self.cleaned_data['email']
        u.save()
        profile = super(EditCustomerForm, self).save(*args,**kwargs)
        return profile
"""""