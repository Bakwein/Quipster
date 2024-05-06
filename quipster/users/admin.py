from django.contrib import admin
from .models import TwitterUser
# Register your models here.

class TwitterUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_followings', 'display_followers')

    def display_followers(self, obj):
        return ", ".join(obj.get_followers())

    #list_filter = ("status",)
    #search_fields = ['title', 'content']
    #prepopulated_fields = {'slug': ('title',)}

admin.site.register(TwitterUser, TwitterUserAdmin)