# main/urls.py
# Django modules
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include('keygen.urls')),
    path('admin/', admin.site.urls),
    path('django-rq/', include('django_rq.urls')),    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
