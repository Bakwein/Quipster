from django.contrib import admin
from .models import TwitterUser
# Register your models here.

class TwitterUserAdmin(admin.ModelAdmin):
    list_display = ('user',)
    #list_filter = ("status",)
    #search_fields = ['title', 'content']
    #prepopulated_fields = {'slug': ('title',)}

admin.site.register(TwitterUser, TwitterUserAdmin)