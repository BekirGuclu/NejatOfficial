"""NejatOfficial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from Home.views import home_view
from django.conf.urls.static import static
from django.conf import settings

from Post import views


urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', home_view, name='home'),
    url(r'^Post/', include('Post.urls')),
    url (r'^accounts/', include ('accounts.urls')),
    url (r'^about/', views.about, name= 'about'),
    url (r'^contact/', views.contact, name= 'contact'),


]

urlpatterns +=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)  #upload edilecek dosyaların url adresleri tanımlandı.
