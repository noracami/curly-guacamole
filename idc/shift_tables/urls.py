from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.shift_table_list, name='shift_table_list'),
    url(r'^admin/', include(admin.site.urls)),
]
