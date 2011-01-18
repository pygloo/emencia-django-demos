from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^basic_test/$', "demos.uniform.views.basic_test", name='basic_test'),
    url(r'^view_helper/$', "demos.uniform.views.view_helper", name='view_helper'),
    url(r'^form_helper/$', "demos.uniform.views.form_helper", name='form_helper'),
    url(r'^layout_test/$', "demos.uniform.views.layout_test", name='layout_test'),
    url(r'^view_helper_set_action/$', "demos.uniform.views.view_helper_set_action", name='set_action_test'),
    url(r'^lacking_form_tag/$', "demos.uniform.views.lacking_form_tag", name='lacking_form_tag'),
    url(r'^message_response/$', "demos.uniform.views.message_response", name='message_response'),
    url(r'^csrf_token_test/$', "demos.uniform.views.csrf_token_test", name='csrf_token_test'),
)
