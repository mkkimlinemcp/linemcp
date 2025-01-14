from django.db import models



# Create your models here.

class create_Artist_profile(models.Model):
    Artist_name = models.TextField()
    Artist_name_en = models.TextField(blank=True,)
    sex = models.CharField(max_length=200)
    category = models.TextField()
    Albums = models.TextField(blank=True,)
    Melon_ID = models.CharField(max_length=200, blank=True,)
    Apple_url = models.TextField(blank=True,)
    Spotify_ID = models.CharField(max_length=22,blank=True,)
    Youtube_ID = models.CharField(max_length=24,blank=True,)
    create_date = models.DateTimeField()
    Artist_ID = models.CharField(max_length=200)
    Artist_image = models.ImageField(upload_to='Artist_images', blank=True,)

    def __str__(self):
        return self.Artist_ID, self.Artist_name

class album_genres(models.Model):
    genres = models.TextField()

    def __str__(self):
        return self.genres
    
class album_Category(models.Model):
    a_Category = models.TextField()

    def __str__(self):
        return self.a_Category
    
class test(models.Model):
    test1 = models.TextField()
    test2 = models.TextField()
    test3 = models.TextField()
    test4 = models.TextField()
    test5 = models.TextField()
    test6 = models.TextField()
    test7 = models.TextField()

    def __str__(self):
        return self.test1