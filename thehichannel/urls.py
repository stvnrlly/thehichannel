from django.conf.urls import include, url
from django.contrib import admin
from his import views as hi_views
from letsencrypt import views as le_views

urlpatterns = [
    url(r'^$', hi_views.all_hi),
    url(r'^user/(?P<user>\w+)', hi_views.user_hi),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('registration.backends.default.urls')),

    url(r'^.well-known/acme-challenge/(?P<id>\w+)', le_views.challenge)
]
