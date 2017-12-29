"""tango_django URL Configuration

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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from registration.backends.simple.views import RegistrationView

from rango import views


# Create a new class that redirects the user to the index page
# if succesful at login
"""class MyRegistrationView(RegistrationView):
    def get_succesful_url(self, request, user):
        return '/rango/'
"""

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Maps any urls starting with rango
    # to be handled by the rango app
    url(r'^rango/', include('rango.urls')),
    url(r'^admin/', admin.site.urls),

    #Add in this url pattern to override the default pattern in accounts.
    url(r'^accounts/register/$', views.RangoRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
