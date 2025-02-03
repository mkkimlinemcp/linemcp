from django.db import models
import os



# Create your models here.

class create_Artist_profile(models.Model):
    Artist_name = models.TextField()
    Artist_name_en = models.TextField(blank=True,)
    sex = models.CharField(max_length=200)
    category = models.TextField()
    Albums = models.TextField(default=list, blank=True,)
    Melon_ID = models.CharField(max_length=200, blank=True,)
    Apple_url = models.TextField(blank=True,)
    Spotify_ID = models.CharField(max_length=22,blank=True,)
    Youtube_ID = models.CharField(max_length=24,blank=True,)
    genie_url = models.TextField(blank=True,)
    bugs_url = models.TextField(blank=True,)
    flo_url = models.TextField(blank=True,)
    vibe_url = models.TextField(blank=True,)
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
    
class rightholder_cr(models.Model):
    user_id = models.TextField(blank=True,)
    user_code = models.TextField(blank=True,)
    user_name = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.TextField()
    bank_name = models.TextField(blank=True,)
    account_number = models.TextField(blank=True,)
    account_holder = models.TextField(blank=True,)
    user_level = models.TextField(blank=True,)
    user_type = models.TextField(blank=True,)
    registration_num = models.TextField(blank=True,)
    contract_date = models.TextField(blank=True,)
    expiration_date = models.TextField(blank=True,)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    albums = models.JSONField(default=list, blank=True,)
    
    def __str__(self):
        return self.user_name

class Album(models.Model):
    album_code = models.TextField()
    album_title = models.TextField()
    album_title_en = models.TextField(blank=True,)
    album_artist = models.TextField()	
    album_genre = models.TextField()
    album_Categ = models.TextField()
    album_country = models.TextField(blank=True,)	
    startdate = models.TextField()	
    opendate = models.TextField()
    service_time = models.TextField()
    album_copyright = models.TextField()
    album_publish = models.TextField()	
    service_area = models.TextField()
    excluded = models.TextField(blank=True,)
    service_lang = models.TextField()
    UPC_code = models.TextField(blank=True,)
    UCI_code = models.TextField(blank=True,)
    YT_service = models.TextField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.album_code, self.album_title, self.album_artist
    
class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    disk_no = models.IntegerField()
    track_no = models.IntegerField()
    track_code = models.TextField()
    song_title = models.TextField()
    song_artist = models.TextField()
    track_genre = models.TextField()
    track_lang = models.TextField()
    title_song = models.TextField(blank=True,)
    adult = models.TextField(blank=True,)
    tr_opendate = models.TextField()
    track_length = models.TextField()
    lyricist = models.TextField(blank=True,)
    composer = models.TextField(blank=True,)
    arranger = models.TextField(blank=True,)
    with_artist = models.TextField(blank=True,)
    featured = models.TextField(blank=True,)
    UCI = models.TextField(blank=True,)
    ISRC = models.TextField(blank=True,)

    def __str__(self):
        return self.track_no, self.song_title
    
class Accounting_base(models.Model):
    Album_code = models.IntegerField()
    rightholder_code = models.IntegerField()
    company_fees = models.FloatField()
    User_Fees = models.FloatField()
    Settlement_Status = models.BooleanField(default=False)
    Settlement_user = models.JSONField(default=list, blank=True,)
    Settlement_rate = models.JSONField(default=list, blank=True,)

    def __str__(self):
        return f"Album: {self.Album_code}, Rightholder: {self.rightholder_code}, User Fees: {self.User_Fees}, Status: {self.Settlement_Status}"
