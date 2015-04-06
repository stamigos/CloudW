# -*- coding: utf-8
from django.forms import ModelForm
from django.forms import TextInput
from .models import MyRegistrationSupplement
from registration.forms import RegistrationFormUniqueEmail


class MyRegistrationForm(ModelForm):
    class Meta:
        model = MyRegistrationSupplement
        fields = ('first_name', 'last_name', 'father_name', 'city', 'phone_number', )

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
        self.fields['username'].required = False
        self.fields['email2'].required = False
        self.fields['email2'].widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['autocomplete'] = 'off'


class MyRegistrationFormUniqueEmail(RegistrationFormUniqueEmail):
    fields = ('first_name', 'last_name', 'father_name', 'city', 'phone_number', )
    exclude = ('username', 'email2', )

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
        self.fields['username'].required = False
        self.fields['email2'].required = False
        self.fields['email2'].widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['autocomplete'] = 'off'