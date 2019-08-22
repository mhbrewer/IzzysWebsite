from django.contrib import admin

from .models import Bean, Roaster, Artist, Picture



@admin.register(Roaster)
class RoasterAdmin(admin.ModelAdmin):
    list_display = ('companyName', 'isDisplayed')
    list_editable = ('isDisplayed',)

@admin.register(Bean)
class BeanAdmin(admin.ModelAdmin):
    list_display = ('title', 'roaster', 'priority', 'isDisplayed')
    list_editable = ('isDisplayed',)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass
