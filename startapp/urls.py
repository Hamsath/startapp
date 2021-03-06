"""startapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from startapp.views import hello,current_dateTime,hours_ahead,ua_display_good1,contact,thanks

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^time/$', current_dateTime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^ua_display/$', ua_display_good1),
    url(r'^', include('books.urls')),
    url(r'^contact/$', contact),
    url(r'^contact/thanks$', thanks),

    ]
