from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template

from cms.sitemaps import CMSSitemap

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/tagging/autocomplete', include('pagetags.urls')),
	#url(r'^', include('opst_plugins.urls')),
    (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    url(r'^', include('cms.urls')),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}})
)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
		(r'^static/(?P<path>.*)$', 'django.views.static.serve',                                                     
            {'document_root': settings.STATIC_ROOT}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns # + staticfiles_urlpatterns()
