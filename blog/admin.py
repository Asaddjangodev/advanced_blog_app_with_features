from django.contrib import admin
from .models import Post, Comments
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status' ,'slug', 'author')

admin.site.register(Post, AuthorAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')


admin.site.register(Comments,CommentAdmin)
