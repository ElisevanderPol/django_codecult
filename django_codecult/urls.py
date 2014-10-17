from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_codecult.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django_codecult.views.home', name='home'),
    url(r'^info/(?P<page_title>\w+)$', 'django_codecult.views.info', name='info'),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^login/$', 'django_codecult.views.user_login', name='login'),
)
