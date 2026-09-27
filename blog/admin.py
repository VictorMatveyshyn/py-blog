from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
