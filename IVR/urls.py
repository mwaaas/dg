from django.conf.urls.defaults import include, patterns, url

urlpatterns = patterns('',
    (r'^greeting/', greeting_view),
)