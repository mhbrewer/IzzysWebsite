from django.conf.urls import url

from .views import testQrCodePage

urlpatterns = [
    url(r'test$', testQrCodePage),
]

