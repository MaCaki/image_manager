"""image_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/

"""
from django.conf import settings
from django.conf.urls import (
    include,
    url
)
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(
        r'^password_reset/$',
        auth_views.password_reset,
        name='password_reset'
    ),
    url(
        r'^password_reset/done/$',
        auth_views.password_reset_done,
        name='password_reset_done'
    ),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',  # noqa
        auth_views.password_reset_confirm,
        name='password_reset_confirm'
    ),
    url(
        r'^reset/done/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'
    ),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls')),  # redirect to the core app.
]

if settings.DEV_ENV:
    # In the dev envionment we have to serve the media files directly from
    # disk.
    # https://docs.djangoproject.com/en/1.10/ref/urls/#django.conf.urls.static.static
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
