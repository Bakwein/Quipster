from django.contrib import admin
from .models import Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_likes', 'get_comments_count', 'is_comment', 'created_at')
    list_filter = ("user", "is_comment", "created_at", "updated_at", "parent")
    search_fields = ['content']
    #prepopulated_fields = {'slug': ('title',)}

admin.site.register(Tweet, TweetAdmin)