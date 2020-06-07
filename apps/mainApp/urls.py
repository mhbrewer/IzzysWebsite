from django.conf.urls import url

from .views import homePage, communityPage, beverageMenuPage, foodMenuPage

urlpatterns = [
    url(r'community$', communityPage),
    url(r'drinkMenu$', beverageMenuPage),
    url(r'foodMenu$', foodMenuPage),
    url(r'', homePage),
]

