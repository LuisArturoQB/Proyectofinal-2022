from django.contrib import admin
from .models import zapatos

# Register your models here.

#class zapatosAdmin(admin.ModelAdmin):
    #readonly_fields=('created','updated')

admin.site.register(zapatos)
