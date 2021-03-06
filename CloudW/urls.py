from django.conf.urls import patterns, include, url
from supplement_registration.forms import MyRegistrationFormUniqueEmail, MyRegistrationForm
from supplement_registration.views import logout_view
from privatebroadcast.views import video_view
from registration.views import RegistrationView
from django.contrib import admin

from django.conf.urls.static import static
import settings
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CloudW.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'privatebroadcast.views.index', name='index'),
    url(r'^video/(?P<pk>\d+)/$', 'privatebroadcast.views.video_view',
        name='video_view'),
    url(r'^profiles/logout/$', 'supplement_registration.views.logout_view', name="logout"),
    url(r'^person_card/$', 'supplement_registration.views.profile_settings', name="profile_settings"),
    url(r'^private/$', 'privatebroadcast.views.private', name="private"),
    url(r'^your_uploads/', include('multiuploader.urls')),
    url('^uploader/$', 'privatebroadcast.views.uploader_view', name='uploader_view'),
    # Add django-inspectional-registration urls. The urls also define
    # Login, Logout and password_change or lot more for handle
    # registration.
    url(r'^registration/register/$', RegistrationView.as_view(form_class=MyRegistrationFormUniqueEmail),
        name='registration_register'),
    url(r'^registration/logout/$', 'supplement_registration.views.logout_view', name='auth_logout'),
    url('^registration/', include('registration.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #url(r'^chat/', include('djangoChat.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)