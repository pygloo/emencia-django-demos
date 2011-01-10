# python import
import os

# django import
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^demos/', include('demos.foo.urls')),

    # zinnia urls
    url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    # url(r'^xmlrpc/$', include('django_xmlrpc.views.handle_xmlrpc')),

    # reploc urls
    (r'^locator/', include('reploc.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

# zinnia sitemap management

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,}

urlpatterns += patterns('django.contrib.sitemaps.views',
        (r'^sitemap.xml$', 'index',
            {'sitemaps': sitemaps}),
        (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
            {'sitemaps': sitemaps}),
        )

# static files

import zinnia

_zinnia_path = os.path.abspath(os.path.dirname(zinnia.__file__))

urlpatterns += patterns('django.views.static',
                        url(r'^zinnia/(?P<path>.*)$', 'serve',
                            {
                                'document_root': os.path.join(_zinnia_path, 'media', 'zinnia')
                                }
                            ),
                        )
