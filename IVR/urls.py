from django.conf.urls.defaults import include, patterns, url
from views import greeting_view, list_page, call_exotel, has_not_seen, has_not_adopted
urlpatterns = patterns('',
    (r'^greeting/', greeting_view),
    (r'^list/', list_page),
    (r'^call/', call_exotel),
    (r'^has_not_seen/', has_not_seen),
    (r'^has_not_adopted/', has_not_adopted),
)