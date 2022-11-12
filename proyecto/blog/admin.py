from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly=('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly=('created', 'updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
