from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdamin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post)
