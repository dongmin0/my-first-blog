from django.contrib import admin
from .models import Post
from .model import *

# admin.site.register(Post)
# admin.site.register(EggmorningMainslide)
# admin.site.register(EggmorningUser)
# admin.site.register(AuthUser)

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']

# 검색기능 추가
admin.site.register(Post, UserAdmin)
admin.site.register(EggmorningMainslide, UserAdmin)
admin.site.register(EggmorningUser, UserAdmin)
admin.site.register(AuthUser, UserAdmin)