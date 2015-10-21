from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.shift_list, name='shift_list'),
    url(r'^admin/', include(admin.site.urls)),
]
