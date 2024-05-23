from django.contrib import admin
from .models import Tweet

# Register your models here.

class IsCommentFilter(admin.SimpleListFilter):
    title = 'Tweet type'
    parameter_name = 'is_comment'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Comments'),
            ('no', 'Tweets'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(parent__isnull=False)
        elif self.value() == 'no':
            return queryset.filter(parent__isnull=True)

class TweetAdmin(admin.ModelAdmin):    
    list_display = ('user', 'get_likes', 'get_comments_count', 'is_comment', 'created_at')
    list_filter = ("user", "created_at", IsCommentFilter, "updated_at", "replied_tweet")
    search_fields = ['content']
    #prepopulated_fields = {'slug': ('title',)}

admin.site.register(Tweet, TweetAdmin)