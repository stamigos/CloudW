# -*- coding: utf-8
from django.db import models
from registration.supplements import RegistrationSupplementBase
from phonenumber_field.modelfields import PhoneNumberField


class MyRegistrationSupplement(RegistrationSupplementBase):

    first_name = models.CharField(u'Имя', max_length=100) #help_text=u'Введите свое имя'
    last_name = models.CharField(u'Фамилия', max_length=30) #help_text=u'Введите свою фамилию')
    father_name = models.CharField(u'Отчество', max_length=30) #help_text=u'Введите свое отчество')
    city = models.CharField(u'Город', max_length=30) #help_text=u'Введите город')
    phone_number = PhoneNumberField(u'Телефон', max_length=30) #help_text=u'Введите свою фамилию')

    def __unicode__(self):
        # a summary of this supplement
        return "%s %s" % (self.first_name, self.last_name)