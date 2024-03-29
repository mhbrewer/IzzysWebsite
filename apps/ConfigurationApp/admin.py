from django.contrib import admin

from .models import Bean, Roaster, Artist, Picture, Food, Beverage, Hours, ContactInfo



@admin.register(Roaster)
class RoasterAdmin(admin.ModelAdmin):
    list_display = ('companyName', 'isDisplayed')
    list_editable = ('isDisplayed',)

@admin.register(Bean)
class BeanAdmin(admin.ModelAdmin):
    list_display = ('title', 'roaster', 'priority', 'isDisplayed')
    list_editable = ('priority', 'isDisplayed')

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'isDisplayed',)
    list_editable = ('isDisplayed',)

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'isDisplayed')
    list_editable = ('isDisplayed',)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'isDisplayed')
    list_editable = ('isDisplayed',)

@admin.register(Beverage)
class BeverageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'isDisplayed')
    list_editable = ('isDisplayed',)

@admin.register(Hours)
class HoursAdmin(admin.ModelAdmin):
    list_display = ('daysOfTheWeek', 'hours', 'isDisplayed')
    list_editable = ('hours', 'isDisplayed')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('contactType', 'contactInfo', 'isDisplayed')
    list_editable = ('contactInfo', 'isDisplayed')