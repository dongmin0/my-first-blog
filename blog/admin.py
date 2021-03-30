from django.contrib import admin
from .models import Post
from .model import *

admin.site.register(Post)
admin.site.register(EggmorningMainslide)
admin.site.register(EggmorningUser)
admin.site.register(AuthUser)
