from django.contrib import admin
from .models import Post, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'published_date', 'category')
    list_display_links = ('title', 'text')
    search_fields = ('title', 'content', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
