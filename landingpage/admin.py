from django.contrib import admin

from .models import Landing

# Register your models here.
class LandingAdmin(admin.ModelAdmin):
    list_display = ('name', 'published', 'last_modified', 'created')
    search_fields = ['name']

admin.site.register(Landing, LandingAdmin)
