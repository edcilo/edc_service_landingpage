from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from .models import Landing


# Register your models here.
class LandingAdmin(admin.ModelAdmin):
    list_display = ('name', 'published', 'last_modified', 'created')
    search_fields = ['name']
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


admin.site.register(Landing, LandingAdmin)
