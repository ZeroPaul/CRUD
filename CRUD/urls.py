from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CRUD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','app_crud.views.read'),
    url(r'^agregar/$','app_crud.views.agregar'),
    url(r'^editar/(?P<id>\d+)$','app_crud.views.editar'),
    url(r'^borrar/(?P<id>\d+)$','app_crud.views.borrar'),
)
