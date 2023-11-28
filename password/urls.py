"""
URL configuration for password project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from password_generator.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('bro_html/',password_generator,name='password_generator'),
     path('register_page/',register_page,name='register_page'),
      path('next_page/',next_page,name='next_page'),
      path('logout_page/',logout_page,name='logout_page'),
      path('home/',Home,name='home'),
       path('book/',book,name='book'),
         path('profile/',profile,name='profile'),
               path('aboutus/',aboutus,name='aboutus'),
          path('contactus/',contactus,name='contactus'),
    path('admin/', admin.site.urls),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
