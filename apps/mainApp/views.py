import os
from django.shortcuts import render, redirect
from django.conf import settings
from apps.ConfigurationApp.models import Bean, Roaster, Artist, Picture, Food, Beverage

from django.views.generic import ListView

def cleanPictureDirectory():
    allPictures = Picture.objects.all()
    artistPicsPath = os.path.join(settings.MEDIA_ROOT, 'ArtistPictures')
    filesInDir = os.listdir(os.path.join(settings.MEDIA_ROOT, 'ArtistPictures'))
    for file in filesInDir:
        fileShouldBeDeleted = True
        fileName = os.fsdecode(file)
        for picture in allPictures:
            if fileName == picture.filename():
                fileShouldBeDeleted = False
        if fileShouldBeDeleted:
            filePath = os.path.join(artistPicsPath, fileName)
            os.remove(filePath)


def homePage(request):
    context = {
        "displayedRoasters": Roaster.objects.filter(isDisplayed = True),
        "pastRoasters": Roaster.objects.filter(isDisplayed = False),
        "displayedBeans": Bean.objects.filter(isDisplayed = True).order_by('priority'),
    }
    return render(request, 'mainApp/home.html', context)

def communityPage(request):
    cleanPictureDirectory()
    context = {
        "displayedArtists": Artist.objects.filter(isDisplayed = True),
        "pastArtists": Artist.objects.filter(isDisplayed = False),
        "displayedPictures": Picture.objects.filter(isDisplayed = True),
    }
    return render(request, 'mainApp/community.html', context)

def beverageMenuPage(request):
    context = {
        "displayedBeverages": Beverage.objects.filter(isDisplayed = True)
    }
    return render(request, 'mainApp/beverageMenu.html', context)

def foodMenuPage(request):
    context = {
        "displayedFoods": Food.objects.filter(isDisplayed = True)
    }
    return render(request, 'mainApp/foodMenu.html', context)

def rerouteToAdmin(request):
    return redirect('/admin/')