"""cash_machine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.contrib.staticfiles.views import serve
from django.views import generic

urlpatterns = [
    re_path(r'^$', serve, kwargs={'path': 'index.html'}),
    re_path(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
        generic.RedirectView.as_view(url='/static/%(path)s', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include('cash_machine_app.urls')),
    path('', include('cash-machine-front.urls'))
]
