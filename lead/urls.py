from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    url(r'^Admin',admin.site.urls),
    url(r'^Upload/(?P<path>.*)$',serve , {'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$',serve , {'document_root':settings.STATIC_ROOT}),
    url(r'' ,include('main.urls')),
    url(r'' ,include('etudiant.urls')),
    url(r'' ,include('article.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
