from django.conf.urls import patterns, include, url
from supplement_registration.forms import MyRegistrationFormUniqueEmail
from supplement_registration.views import logout_view
from registration.views import RegistrationView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CloudW.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'privatebroadcast.views.index', name='index'),
    url(r'^profiles/logout/$', 'supplement_registration.views.logout_view', name="logout"),
    url(r'^person_card/$', 'supplement_registration.views.profile_settings', name="profile_settings"),
    url(r'^private/$', 'privatebroadcast.views.private', name="private"),
    # Add django-inspectional-registration urls. The urls also define
    # Login, Logout and password_change or lot more for handle
    # registration.
    url(r'^registration/register/$', RegistrationView.as_view(form_class=MyRegistrationFormUniqueEmail),
        name='registration_register'),
    url(r'^registration/logout/$', 'supplement_registration.views.logout_view', name='auth_logout'),
    url('^registration/', include('registration.urls')),
)
