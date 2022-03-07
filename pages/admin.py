from django.contrib import admin
from pages.models import Team
# Register your models here.

@admin.register(Team)
class TeamModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'first_name', 'last_name', 'designation', 
                    'photo', 'facebook_link', 'twitter_link', 'google_plus_link']