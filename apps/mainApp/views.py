import os
from django.shortcuts import render, redirect
from django.conf import settings
from apps.ConfigurationApp.models import Bean, Roaster, Artist, Picture, Food, Beverage, Hours, ContactInfo

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
        if fileName == ".gitignore":
            fileShouldBeDeleted = False
        if fileShouldBeDeleted:
            filePath = os.path.join(artistPicsPath, fileName)
            os.remove(filePath)


def homePage(request):
    hoursByDay = {
        "monfri": Hours.objects.filter(daysOfTheWeek__iexact = "mf").filter(isDisplayed = True).first(),
        "sat": Hours.objects.filter(daysOfTheWeek__iexact = "sa").filter(isDisplayed = True).first(),
        "sun": Hours.objects.filter(daysOfTheWeek__iexact = "su").filter(isDisplayed = True).first(),
    }

    contactInfo = {
        "address": ContactInfo.objects.filter(contactType__iexact = "address").filter(isDisplayed = True).first(),
        "phone": ContactInfo.objects.filter(contactType__iexact = "phone").filter(isDisplayed = True).first(),
        "email": ContactInfo.objects.filter(contactType__iexact = "email").filter(isDisplayed = True).first(),
    }

    context = {
        "displayedRoasters": Roaster.objects.filter(isDisplayed = True),
        "pastRoasters": Roaster.objects.filter(isDisplayed = False),
        "displayedBeans": Bean.objects.filter(isDisplayed = True).order_by('priority'),
        "hoursByDay": hoursByDay,
        "contactInfo": contactInfo,
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