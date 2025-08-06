from django.contrib import admin
from .models import Post, Comments, Category
from mptt.admin import MPTTModelAdmin
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id' ,'status' ,'slug', 'author')
admin.site.register(Post, AuthorAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category, CategoryAdmin)

admin.site.register(Comments, MPTTModelAdmin)