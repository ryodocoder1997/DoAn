"""doan URL Configuration

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
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('academy/', TemplateView.as_view(template_name='academy.html')),
                  path('tutor-list', TemplateView.as_view(template_name='tutor-list.html'), name='tutor-list'),
                  path('course-list', TemplateView.as_view(template_name='course-list.html'), name='course-list'),
                  path('academy-list', TemplateView.as_view(template_name='academy-list.html'), name='academy-list'),
                  path('base', TemplateView.as_view(template_name='base.html')),
                  path('homepage', TemplateView.as_view(template_name='homepage.html')),
                  path('term-of-uses', TemplateView.as_view(template_name='term-of-uses.html')),

                  path('accounts/', include('accounts.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('', include('accounts.urls')),
                  path('user_profile/', include('polls.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
