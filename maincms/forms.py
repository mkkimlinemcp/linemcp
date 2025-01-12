from django import forms
from maincms.models import create_Artist_profile

class Artist_create_form(forms.ModelForm):
    class Meta:
        model = create_Artist_profile
        fields = ['Artist_name','Artist_name_en','sex','category','Albums','Melon_ID','Apple_url','Spotify_ID','Youtube_ID','Artist_image' ]