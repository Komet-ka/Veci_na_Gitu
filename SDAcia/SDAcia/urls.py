"""SDAcia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from viewer.models import Znacka, Karoserie, Komentar, Auto
from viewer.views import inzeraty, inzerat, novy_inzerat, AutoCreateView

admin.site.register(Znacka)
admin.site.register(Karoserie)
admin.site.register(Komentar)
admin.site.register(Auto)

from viewer.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', hello),
    path('inzeraty', inzeraty),
    path('inzerat/<auto_pk>', inzerat),
    path('novy_inzerat', novy_inzerat),
    path('formular', AutoCreateView.as_view(), name='auto_create')

]
