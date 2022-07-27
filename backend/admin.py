from django.contrib import admin

from .models import Developer, Project
# Register your models here.

# admin.site.register(Developer)

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'project', 'language')
    list_filter = ('language',)
    search_fields = ('first_name', 'last_name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',  'date_start', 'date_end', 'cost', 'developer')
    search_fields = ('name__contains',)