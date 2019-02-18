from django.contrib import admin
from .models import Post, Comment

# admin.site.register(Post)
# admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'short_content', 'is_public', 'tags', 'created_at']
    list_display_links = ['title']
    list_filter = ['is_public']
    search_fields = ['title']

    def short_content(self, post):
        return post.content[:20] + "..."

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # list_diplay = ['id', 'post', 'message', 'created_at']

    # def message(self, comment):
    #     return comment.message[:20] + "..."
    pass