import os
from django.shortcuts import render, redirect
from django.conf import settings


def testQrCodePage(request):
    return render(request, 'qrCodeApp/test.html')