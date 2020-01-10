from django.conf.urls import include, url

# from django.contrib import admin
# admin.autodiscover()

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^developers/$', views.developers, name='developers'),
    url(r'^developers/guidelines/$', views.guidelines,
        name='guidelines'),
    url(r'^developers/process/$', views.process, name='process'),
    url(r'^developers/request/$', views.request, name='request'),

    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),

    # include applications
    # url(r'^', include('app_name.urls')),
]
