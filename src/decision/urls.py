from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'decision.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^idea/(?P<ideaId>\d+)$'
        , 'decision.site.views.ideaInfo', name='idea'),
                       
    url(r'^', 'decision.site.views.master', name='master'),
    
)
