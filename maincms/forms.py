from django import forms
from maincms.models import create_Artist_profile, test, rightholder_cr,Album

class Artist_create_form(forms.ModelForm):
    class Meta:
        model = create_Artist_profile
        fields = ['Artist_name','Artist_name_en','sex','category','Albums','Melon_ID','Apple_url','Spotify_ID','Youtube_ID','Artist_image' ]

class test_form(forms.ModelForm):
        class Meta:
            model = test
            fields = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7']

class rightholder_cr_form(forms.ModelForm):
     class Meta:
          model = rightholder_cr
          fields = ['user_id','user_name','email', 'phone','bank_name','account_number','account_holder','user_level','user_type','registration_num','contract_date','expiration_date',]

class Create_album_form(forms.ModelForm):
     class Meta:
          model = Album
          fields = ['album_code','album_title','album_title_en','album_artist','album_genre','album_Categ']