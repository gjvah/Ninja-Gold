#apps/ninja_gold/urls.py

from django.conf.urls import url, include
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^reset$', views.reset),
    url(r'^settings$', views.settings),
    url(r'^register$', views.register),
    url(r'^defaults$', views.defaults),
    url(r'^avatar/', include('avatar.urls')),
    # url(r'^new$', views.new),
    # url(r'^create$', views.create),
    # url(r'^\d+$', views.number),
    # url(r'^\d+/edit$', views.number_edit),
    # url(r'^\d+/delete$', views.destroy),
]