from django.conf.urls.defaults import include, patterns, url
from views import greeting_view

urlpatterns = patterns('',
    (r'^greeting/', greeting_view),
)