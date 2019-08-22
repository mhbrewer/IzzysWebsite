from django.db import models
# from django.contrib.auth.models import User


# Helper Function
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<Artist's First Name>/<filename>
    return '{0}/{1}'.format(instance.artist.firstName, filename)

class Roaster(models.Model):
    companyName = models.CharField(max_length=50)
    url = models.CharField(max_length=500, blank=True)
    isDisplayed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.companyName

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
    # objects = BeanManager()

    def __str__(self):
        return self.title

class Artist(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=50, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.firstName, self.lastName)

class Picture(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ArtistPictures')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title