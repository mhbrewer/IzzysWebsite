from django.conf.urls import url

from .views import homePage, communityPage

urlpatterns = [
    url(r'community$', communityPage),
    url(r'', homePage),
]

