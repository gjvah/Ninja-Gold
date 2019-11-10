#apps/my_app/urls.py

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^profile$', views.profile),
    # url(r'^new$', views.new),
    # url(r'^create$', views.create),
    # url(r'^\d+$', views.number),
    # url(r'^\d+/edit$', views.number_edit),
    # url(r'^\d+/delete$', views.destroy),
]