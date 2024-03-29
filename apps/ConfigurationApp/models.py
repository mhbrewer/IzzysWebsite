from django.db import models
import os
# from django.contrib.auth.models import User


# Helper Function
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<Artist's First Name>/<filename>
    return '{0}/{1}'.format(instance.artist.firstName, filename)

class RoasterManager(models.Manager):
    pass
class Roaster(models.Model):
    companyName = models.CharField(max_length=50)
    url = models.CharField(max_length=500, blank=True)
    isDisplayed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = RoasterManager()

    def __str__(self):
        return self.companyName

class BeanManager(models.Manager):
    pass
class Bean(models.Model):
    title = models.CharField(max_length=50)
    blend = models.CharField(max_length=50, blank=True)
    process = models.CharField(max_length=50, blank=True)
    notes = models.CharField(max_length = 255, blank=True)
    priority = models.IntegerField()
    roaster = models.ForeignKey(Roaster, on_delete=models.CASCADE)
    isDisplayed = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = BeanManager()

    def __str__(self):
        return self.title

class ArtistManager(models.Manager):
    pass
class Artist(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=50, blank=True)
    isDisplayed = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = ArtistManager()

    def __str__(self):
        return "{0} {1}".format(self.firstName, self.lastName)

class PictureManager(models.Manager):
    pass
class Picture(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ArtistPictures')
    isDisplayed = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = PictureManager()

    def filename(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        return self.title

class FoodManager(models.Manager):
    pass
class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    isDisplayed = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = FoodManager()

    def __str__(self):
        return self.name

class BeverageManager(models.Manager):
    pass
class Beverage(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    isDisplayed = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = BeverageManager()

    def __str__(self):
        return self.name

class HoursManager(models.Manager):
    pass
class Hours(models.Model):
    hours = models.CharField(max_length=50)
    daysOfTheWeek = models.CharField(max_length=2)
    isDisplayed = models.BooleanField(default=True)
    objects = HoursManager()

    def __str__(self):
        return self.daysOfTheWeek

class ContactInfoManager(models.Manager):
    pass
class ContactInfo(models.Model):
    contactInfo = models.CharField(max_length=50)
    contactType = models.CharField(max_length=50)
    isDisplayed = models.BooleanField(default=True)
    objects = ContactInfoManager()

    def __str__(self):
        return self.contactType