from django.contrib import admin
from .models import Profile
from comment.models import Comment
from posts.models import Post

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Post)