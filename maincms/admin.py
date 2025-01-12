from django.contrib import admin
from .models import create_Artist_profile
# Register your models here.



class create_Artist_search(admin.ModelAdmin):
    search_fields = ['Artist_name']

admin.site.register(create_Artist_profile, create_Artist_search)