"""data_analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import login_view, logout_view, signup_view, about_view, faq_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sales.urls', namespace='sales')),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('reports/', include('reports.urls', namespace='reports')),
    path('my_profile/', include('profiles.urls', namespace='profiles')),
    path('about/', about_view, name='about'),
    path('faq/', faq_view, name='faq'),
    path('contact/', contact_view, name='contact')
]

handler404 = 'data_analysis.views.handler404'
handler500 = 'data_analysis.views.handler500'
handler403 = 'data_analysis.views.handler403'
handler400 = 'data_analysis.views.handler400'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
