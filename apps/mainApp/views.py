import os
from django.shortcuts import render, redirect
from django.conf import settings
from apps.ConfigurationApp.models import Bean, Roaster, Artist, Picture

from django.views.generic import ListView

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def homePage(request):
    context = {
        "displayedRoasters": Roaster.objects.filter(isDisplayed = True),
        "pastRoasters": Roaster.objects.filter(isDisplayed = False),
        "displayedBeans": Bean.objects.filter(isDisplayed = True).order_by('priority'),
    }
    return render(request, 'mainApp/home.html', context)

def communityPage(request):
    allPictures = Picture.objects.all()
    print(settings.BASE_DIR)
    print(settings.MEDIA_ROOT)
    artistPicsPath = os.path.join(settings.MEDIA_ROOT, 'ArtistPictures')
    print(artistPicsPath)
    filesInDir = os.listdir(os.path.join(settings.MEDIA_ROOT, 'ArtistPictures'))
    print(allPictures[0].filename())
    for file in filesInDir:
        fileShouldBeDeleted = True
        fileName = os.fsdecode(file)
        for picture in allPictures:
            if fileName == picture.filename():
                fileShouldBeDeleted = False
        if fileShouldBeDeleted:
            filePath = os.path.join(artistPicsPath, fileName)
            os.remove(filePath)
    context = {
        "displayedArtists": Artist.objects.filter(isDisplayed = True),
        "pastArtists": Artist.objects.filter(isDisplayed = False),
        "displayedPictures": Picture.objects.filter(isDisplayed = True),
    }
    return render(request, 'mainApp/community.html', context)