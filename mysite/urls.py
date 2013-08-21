from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.decorators import login_required
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
   url(r'^polls/', include('polls.urls', namespace="polls")),
   url(r'^news/', include('news.urls', namespace="news")),
   url(r'^contact/', include('contact.urls', namespace="contact")),

   # User Accounts
   #url(r'^accounts/login/$', login),
   #url(r'^accounts/logout/$', logout),
   #url(r'^accounts/profile/$'),
   
   # used for email activation
   #url(r'^accounts/', include('registration.backends.default.urls')),

   url(r'^accounts/', include('registration.backends.simple.urls')),
   url(r'^accounts/profile/', login_required(TemplateView.as_view(template_name="profile.html"))),
)
