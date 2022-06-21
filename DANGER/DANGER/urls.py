"""DANGER URL Configuration

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
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from pages import views
import pages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include('api.urls')),
    path('index.html', views.index),
    path('', include('pages.urls')),
    path('', include('faq.urls')),
    path('mlmodel', include('mlmodel.urls')),
    path('', include('admins.urls')),
    path('', include('users.urls')),
    path('braceletsettings', include('braceletsettings.urls')),
    path('healthrecord', include('healthrecord.urls')),
    path('', include('members.urls')),
    path('', include('accounts.urls')),
    path('add-acc.html', views.add_acc),
    path('add-bracelet.html', views.add_bracelet),
    path('add-faq.html', views.add_faq),
    path('show-users.html', views.show_users),
    path('add-users.html', views.add_users),
    path('add.html', views.add),
    path('show.html', views.show),
    path('show-acc.html', views.show_acc),
    path('show-bracelet.html', views.show_bracelet),
    path('show-faq.html', views.show_faq),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






