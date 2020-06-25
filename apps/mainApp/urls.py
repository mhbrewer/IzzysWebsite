from django.conf.urls import url

from .views import homePage, communityPage, beverageMenuPage, foodMenuPage, rerouteToAdmin

urlpatterns = [
    url(r'community$', communityPage),
    url(r'drinkMenu$', beverageMenuPage),
    url(r'foodMenu$', foodMenuPage),
    url(r'admin$', rerouteToAdmin),
    url(r'', homePage),
]

