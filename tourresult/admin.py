from django.contrib import admin
from .models import result

# Register your models here.
# admin.site.register(result)

class resultAdmin(admin.ModelAdmin):
    search_fields = ['Subject']

admin.site.register(result, resultAdmin)