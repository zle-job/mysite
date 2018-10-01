from django.contrib import admin

from blog.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_time', 'last_modified_time']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
