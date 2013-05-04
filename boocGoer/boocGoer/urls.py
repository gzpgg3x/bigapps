from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bestsell.views.shout'),
    url(r'^shout$', 'bestsell.views.shout'),
    
    url(r'^api/shouts/new$', 'bestsell.api.new_shout'),
    url(r'^api/shouts/get$', 'bestsell.api.get_shouts'),
    
    url(r'^admin/', include(admin.site.urls)),
)
