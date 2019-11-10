#project/urls.py

"""django_project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
from django.conf.urls import url, include	# added an import!
from django.contrib import admin  # comment out, or just delete
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    url(r'^', include('apps.my_app.urls')),	# use your app_name here
    url(r'^admin/', include(admin.site.urls)),        # comment out, or just delete
    url(r'^ninja_gold/', include('apps.ninja_gold.urls')),
    # url(r'^register/', include('apps.my_app.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^media/', include('apps.my_app.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # This fixed the MEDIA ROOT issue with avatar pictures



# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
