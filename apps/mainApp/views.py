from django.shortcuts import render, redirect
from apps.ConfigurationApp.models import Bean, Roaster, Artist, Picture

from django.views.generic import ListView

def homePage(request):
    context = {
        "displayedRoasters": Roaster.objects.filter(isDisplayed = True),
        "pastRoasters": Roaster.objects.filter(isDisplayed = False),
        "displayedBeans": Bean.objects.filter(isDisplayed = True).order_by('priority'),
    }
    return render(request, 'mainApp/home.html', context)

def communityPage(request):
    context = {
        "displayedArtists": Artist.objects.filter(isDisplayed = True),
        "pastArtists": Artist.objects.filter(isDisplayed = False),
        "displayedPictures": Picture.objects.filter(isDisplayed = True),
    }
    return render(request, 'mainApp/community.html', context)