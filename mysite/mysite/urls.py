"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from .sitemap import sitemaps

urlpatterns = [
    path('admin/docs/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('shop/', include('shopapp.urls')),
    path('req/', include('requestdataapp.urls')),
    path('auth/', include('myauth.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('blog/', include('blogapp.urls')),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='schema_swagger'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='schema_redoc'),
    path('api/', include('chek_restf.urls')),
    path(
        'sitemap.xml/',
        sitemap,
        {"sitemaps": sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),

]

if settings.DEBUG:
    urlpatterns.append(
        path('__debug__/', include('debug_toolbar.urls')),
    )

