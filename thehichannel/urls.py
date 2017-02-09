from django.conf.urls import include, url
from django.contrib import admin
from his import views as hi_views
from letsencrypt import views as le_views

api_patterns = [
    url(r'^user/(?P<user>\w+)', hi_views.api_user_hi),
    url(r'^post', hi_views.api_post_hi),
]

urlpatterns = [
    url(r'^$', hi_views.all_hi),
    url(r'^user/(?P<user>\w+)', hi_views.user_hi),
    url(r'^api/', include(api_patterns)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('registration.backends.default.urls')),
    url(r'^account/profile/$', hi_views.profile),
    url(r'^account/refresh_token/$', hi_views.refresh_token),

    url(r'^.well-known/acme-challenge/(?P<id>\w+)', le_views.challenge)
]
