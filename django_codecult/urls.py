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
    url(r'^profile/(?P<user_name>\w+)$', 'django_codecult.views.profile', name='profile'),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^update_info', 'django_codecult.views.update_info', name='update_info'),
)
