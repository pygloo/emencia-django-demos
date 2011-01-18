# python import
import os

# django import
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# axes demo
import demos.axes.views
# gmaps demo
import demos.gmaps.views

urlpatterns = patterns('',

    # tinymce
    (r'^tinymce/', include('tinymce.urls')),

    # zinnia urls
    url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    # url(r'^xmlrpc/$', include('django_xmlrpc.views.handle_xmlrpc')),

    # axes urls
    (r'^axes/', demos.axes.views.index),

    # reploc urls
    (r'^loc/', include('reploc.urls')),

    # gmaps urls
    (r'^gmaps/', demos.gmaps.views.index),

    # photologue urls
    (r'^photologue/', include('photologue.urls')),

    # gmaps urls
    (r'^uniform/', include('demos.uniform.urls')),

    # gmaps urls
    (r'^formbuilder/', include('forms_builder.forms.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # gmapsfield: Add this to serve correct admin js
    (r'^admin/gmapsfield/admin/(?P<file>.*)$', 'gmapsfield.views.serve'),
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
import uni_form

_cur_path = os.path.abspath(os.path.dirname(__file__))
_zinnia_path = os.path.abspath(os.path.dirname(zinnia.__file__))
_uni_form_path = os.path.abspath(os.path.dirname(uni_form.__file__))

urlpatterns += patterns('django.views.static',
                        url(r'^tiny_mce/(?P<path>.*)$', 'serve',
                            {
                                'document_root': os.path.join(_cur_path, 'media', 'tiny_mce')
                                }
                            ),
                        url(r'^zinnia/(?P<path>.*)$', 'serve',
                            {
                                'document_root': os.path.join(_zinnia_path, 'media', 'zinnia')
                                }
                            ),
                        url(r'^blog/uploads/(?P<path>.*)$', 'serve',
                            {
                                'document_root': os.path.join(_cur_path, 'media', 'uploads')
                                }
                            ),
                        url(r'^reploc/(?P<path>.*)$', 'serve',
                            {
                                'document_root': os.path.join(_cur_path, 'media', 'reploc')
                                }
                            ),
                        url(r'^uniform/(?P<path>.*)$', 'serve',
                            {
                                'document_root': os.path.join(_uni_form_path, 'media', 'uni_form')
                                }
                            ),
                        )
