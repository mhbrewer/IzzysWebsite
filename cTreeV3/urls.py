"""cTreeV3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

# For the admin/configuration back-end
urlpatterns = [
    url('^admin/', admin.site.urls),
]

# For pictures
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# For the front-end customer display.
# We need the default to be at the end.
defaulturlpattern = [
    url('^qrcodes', include('apps.qrCodeApp.urls')),
    url('^', include('apps.mainApp.urls'))
]

urlpatterns.extend(defaulturlpattern)

