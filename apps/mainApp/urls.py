from django.conf.urls import url

from .views import homePage, communityPage, drinkMenuPage, foodMenuPage

urlpatterns = [
    url(r'community$', communityPage),
    url(r'drinkMenu$', drinkMenuPage),
    url(r'foodMenu$', foodMenuPage),
    url(r'', homePage),
]

